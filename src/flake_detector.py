import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def detect_flaky_tests(log_file):
    df = pd.read_json(log_file)
    df["flaky_score"] = df.groupby("test")["status"].transform(lambda x: x.eq("FAIL").mean())
    df["time_variability"] = df.groupby("test")["time"].transform("std")

    X = df[["flaky_score", "time_variability"]].fillna(0)
    model = RandomForestClassifier().fit(X, df["is_flaky_label"])  # Pre-trained or dummy labels
    df["flaky_prediction"] = model.predict(X)
    return df[df["flaky_prediction"] == 1]["test"].unique()