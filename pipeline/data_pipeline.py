import pandas as pd

def run_pipeline():
    
    df = pd.read_csv("data/raw_dataset.csv")

    # Encode categorical variables
    df["country"] = df["country"].astype("category").cat.codes
    df["device"] = df["device"].astype("category").cat.codes

    # Save processed data
    df.to_csv("data/processed_dataset.csv", index=False)

    print("Data pipeline finished!")

if __name__ == "__main__":
    run_pipeline()