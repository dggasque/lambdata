"""
utility functions for working with DataFrames
"""

import pandas
import numpy as np

TEST_DF = pandas.DataFrame([1,2,3,4,5,6])

# Function to check for nulls 

def missing_values(dataframe):
    for col in dataframe.columns:
        null_sum = dataframe[col].isnull().sum()
        if null_sum > 0:
            print(f'{col} has {null_sum} missing values')

# Train/*validate*/test split function for a dataframe

def train_val_test_split(df, train_per=0.60, val_per=0.20, test_per=0.20, Random_State=None):
    np.random.seed(Random_State)
    percent = train_per + val_per
    train, validate, test = np.split(df.sample(frac=1), [int(train_per*len(df)), int(percent*len(df))])
    return train, validate, test

# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

def datetime_split(df, column):
    if df[column].dtype == 'datetime64':
        df['year'] = df[column].dt.year
        df['month'] = df[column].dt.month
        df['day'] = df[column].dt.day

    else:
        return 'WARNING: Series must be data type datetime64!'    