import pandas as pd
from sqlalchemy import create_engine

def load_data():
    df = pd.read_csv("data/covid_cleaned.csv")

    # SQLite DB connection
    engine = create_engine("sqlite:///data/covid.db")

    df.to_sql("covid_data", con=engine, if_exists="replace", index=False)
    print("✅ Data loaded into sqlite database at data/covid.db")

if __name__ == "__main__":
    load_data()
