import pandas as pd


def store_data(json_data, filename):
    df = pd.DataFrame(json_data)
    df.to_csv(filename, index=False)
    print(f"Data stored in {filename}")
