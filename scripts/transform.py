import pandas as pd

def transform_data():
    df = pd.read_csv("data/covid_raw.csv")

    # columns ko lowercase karo
    df.columns = [c.lower() for c in df.columns]

    # naya column: active cases
    df["active"] = df["confirmed"] - df["recovered"] - df["deaths"]

    # missing values ko fill karo
    df.fillna(0, inplace=True)

    df.to_csv("data/covid_cleaned.csv", index=False)
    print("✅ Data transformed and saved to data/covid_cleaned.csv")

if __name__ == "__main__":
    transform_data()
