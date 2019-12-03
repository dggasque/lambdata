"""
Utility functions for working with DataFrames
"""

import pandas
import numpy as np


TEST_DF = pandas.DataFrame([1, 2, 3, 4, 5, 6])


def train_val_test_split(
        df,
        train_per=0.60,
        val_per=0.20,
        test_per=0.20,
        Random_State=None):
    """Train/*validate*/test split function for a dataframe"""
    np.random.seed(Random_State)
    percent = train_per + val_per
    train, validate, test = np.split(
        df.sample(frac=1), [int(train_per * len(df)), int(percent * len(df))])
    return train, validate, test


class Processor:
    """Processor for dataframes"""

    def __init__(self):
        pass

    def missing_values(self, df):
        """Function for finding columns with missing values."""

        for col in df.columns:
            null_sum = df[col].isnull().sum()
            if null_sum > 0:
                print(f'{col} has {null_sum} missing values')

    def datetime_split(self, df, column):
        """#Function to split dates ("MM/DD/YYYY", etc.) into multiple columns."""
        if df[column].dtype == 'datetime64[ns]' or '<M8[ns]':
            df['year'] = df[column].dt.year
            df['month'] = df[column].dt.month
            df['day'] = df[column].dt.day

        else:
            return 'WARNING: Series must be datetime data format!'
