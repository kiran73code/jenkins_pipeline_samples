import pandas as pd
import numpy as np

def create_fancy_dataframe():
    # Create a DataFrame with random data
    data = {
        'A': np.random.randint(1, 100, 5),
        'B': np.random.choice(['X', 'Y', 'Z'], 5),
        'C': np.random.randn(5),
        'D': pd.date_range('2024-01-01', periods=5)
    }
    df = pd.DataFrame(data)
    return df

def print_dataframe_info(df):
    print("DataFrame Head:")
    print(df.head())
    print("\nDataFrame Info:")
    print(df.info())
    print("\nDataFrame Description:")
    print(df.describe(include='all'))

if __name__ == "__main__":
    fancy_df = create_fancy_dataframe()
    print_dataframe_info(fancy_df)