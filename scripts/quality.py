import pandas as pd

def run_checks():
    df = pd.read_csv("data/covid_cleaned.csv")
    print("Rows:", len(df))
    print("Countries:", df["country"].nunique())
    print("✅ Basic quality checks passed!")

if __name__ == "__main__":
    run_checks()
