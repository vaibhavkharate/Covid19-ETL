import pandas as pd
import os

def extract_data():
    os.makedirs("data", exist_ok=True)
    url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
    df = pd.read_csv(url)
    df.to_csv("data/covid_raw.csv", index=False)
    print("✅ Data extracted and saved to data/covid_raw.csv")

if __name__ == "__main__":
    extract_data()
