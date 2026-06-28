using System.Text.Json;

if (args.Length != 4 || args[0] != "--model" || args[2] != "--test")
{
    Console.Error.WriteLine("Usage: --model <model.json> --test <cases.json>");
    return 2;
}

var jsonOptions = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
var model = JsonSerializer.Deserialize<OptionModel>(File.ReadAllText(args[1]), jsonOptions)
    ?? throw new InvalidOperationException("Option model is empty.");
var suite = JsonSerializer.Deserialize<TestSuite>(File.ReadAllText(args[3]), jsonOptions)
    ?? throw new InvalidOperationException("Test suite is empty.");

var modelErrors = ValidateModel(model);
if (modelErrors.Count > 0)
{
    foreach (var error in modelErrors) Console.Error.WriteLine($"MODEL: {error}");
    return 1;
}

var failed = 0;
foreach (var test in suite.Cases)
{
    var result = Resolve(model, test.Overrides);
    var valid = result.Errors.Count == 0;
    var normalized = test.Normalized.All(pair =>
        result.Values.TryGetValue(pair.Key, out var value) && value == pair.Value);
    var warningsMatch = result.Warnings.Count == test.WarningCount;

    if (valid != test.Valid || !normalized || !warningsMatch)
    {
        failed++;
        Console.Error.WriteLine($"FAIL: {test.Name}");
        foreach (var error in result.Errors) Console.Error.WriteLine($"  {error}");
        Console.Error.WriteLine($"  Expected {test.WarningCount} warning(s), received {result.Warnings.Count}.");
    }
    else
    {
        Console.WriteLine($"PASS: {test.Name}");
    }
}

Console.WriteLine($"{suite.Cases.Count - failed}/{suite.Cases.Count} cases passed.");
return failed == 0 ? 0 : 1;

static List<string> ValidateModel(OptionModel model)
{
    var errors = new List<string>();
    if (string.IsNullOrWhiteSpace(model.ContractVersion)) errors.Add("contractVersion is required.");
    if (string.IsNullOrWhiteSpace(model.TemplateShortName)) errors.Add("templateShortName is required.");

    var names = model.Options.Select(option => option.Name).ToHashSet(StringComparer.Ordinal);
    if (names.Count != model.Options.Count) errors.Add("Option names must be unique.");

    foreach (var option in model.Options)
    {
        if (option.Values.Count == 0) errors.Add($"{option.Name} has no allowed values.");
        if (!option.Values.Contains(option.Default)) errors.Add($"{option.Name} default is not allowed.");
    }

    foreach (var rule in model.Rules)
    {
        if (!names.Contains(rule.When.Option)) errors.Add($"Rule references unknown option {rule.When.Option}.");
        if (!names.Contains(rule.Target)) errors.Add($"Rule references unknown target {rule.Target}.");
        if (rule.Kind is not ("normalize" or "require" or "warn")) errors.Add($"Unknown rule kind {rule.Kind}.");
        if (rule.Kind == "normalize" && string.IsNullOrWhiteSpace(rule.Value)) errors.Add("Normalize rule requires value.");
        if (rule.Kind == "require" && rule.Allowed.Count == 0) errors.Add("Require rule needs allowed values.");

        var source = model.Options.SingleOrDefault(option => option.Name == rule.When.Option);
        var target = model.Options.SingleOrDefault(option => option.Name == rule.Target);
        if (source is not null && rule.When.Values.Any(value => !source.Values.Contains(value)))
            errors.Add($"Rule for {rule.When.Option} contains an invalid condition value.");
        if (target is not null && rule.Kind == "normalize" && !target.Values.Contains(rule.Value!))
            errors.Add($"Normalize rule for {rule.Target} contains an invalid value.");
        if (target is not null && rule.Kind == "require" && rule.Allowed.Any(value => !target.Values.Contains(value)))
            errors.Add($"Require rule for {rule.Target} contains an invalid allowed value.");
    }

    return errors;
}

static Resolution Resolve(OptionModel model, Dictionary<string, string> overrides)
{
    var options = model.Options.ToDictionary(option => option.Name, StringComparer.Ordinal);
    var values = options.Values.ToDictionary(option => option.Name, option => option.Default, StringComparer.Ordinal);
    var errors = new List<string>();

    foreach (var pair in overrides)
    {
        if (!options.TryGetValue(pair.Key, out var option))
        {
            errors.Add($"Unknown option {pair.Key}.");
        }
        else if (!option.Values.Contains(pair.Value))
        {
            errors.Add($"Invalid value {pair.Value} for {pair.Key}.");
        }
        else
        {
            values[pair.Key] = pair.Value;
        }
    }

    for (var pass = 0; pass < model.Rules.Count; pass++)
    {
        var changed = false;
        foreach (var rule in model.Rules.Where(rule => rule.Kind == "normalize" && Matches(rule.When, values)))
        {
            if (values[rule.Target] != rule.Value)
            {
                values[rule.Target] = rule.Value!;
                changed = true;
            }
        }
        if (!changed) break;
    }

    foreach (var rule in model.Rules.Where(rule => rule.Kind == "require" && Matches(rule.When, values)))
    {
        if (!rule.Allowed.Contains(values[rule.Target])) errors.Add(rule.Message);
    }

    var warnings = model.Rules
        .Where(rule => rule.Kind == "warn" && Matches(rule.When, values))
        .Select(rule => rule.Message)
        .ToList();

    return new Resolution(values, errors, warnings);
}

static bool Matches(Condition condition, Dictionary<string, string> values) =>
    values.TryGetValue(condition.Option, out var value) && condition.Values.Contains(value);

sealed record OptionModel(string ContractVersion, string TemplateShortName, List<OptionDefinition> Options, List<Rule> Rules);
sealed record OptionDefinition(string Name, string Default, List<string> Values);
sealed record Rule(string Kind, Condition When, string Target, string? Value, List<string> Allowed, string Message);
sealed record Condition(string Option, List<string> Values);
sealed record TestSuite(List<TestCase> Cases);
sealed record TestCase(string Name, Dictionary<string, string> Overrides, bool Valid, Dictionary<string, string> Normalized, int WarningCount = 0);
sealed record Resolution(Dictionary<string, string> Values, List<string> Errors, List<string> Warnings);
