def suggest_fixes(test_name, df):
    test_data = df[df["test"] == test_name]
    if test_data["time_variability"].mean() > 0.3:
        return f"Add retry logic for {test_name} due to unstable execution time."
    if test_data["status"].value_counts().get("FAIL", 0) > 1:
        return f"Investigate race conditions in {test_name}."
    return "No clear mitigation; review test logic."