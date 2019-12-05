# Lambdata
Lambdata-dggasque is a collection of data science helper functions.

# Installation 

## Dependencies

Python (>= 3.7)
Numpy (>=1.16.5)
Pandas (>=0.25.1)

## User installation

```
pip install -i https://test.pypi.org/simple/ lambdata-dggasque
```
# Contents

## Sample Dataframes

### Ones

```python
lambdata_dggasque.ONES
```
A 10x1 dataframe of ones.

#### Example
```python
import lambdata_dggasque as lambdata


df = lambdata.ONES
```
### Zeros

```python
lambdata_dggasque.ZEROS
```
A 50x1 dataframe of zeros.

#### Example

```python
import lambdata_dggasque as lambdata


df = lambdata.ZEROS
```

### Test Dataframe

```python
lambdata_dggasque.df_utils.TEST_DF
```
A 6x1 dataframe used for testing functions.

#### Example
```python
from lambdata_dggasque import df_utils


df = df_utils.TEST_DF
```

## Modules, Classes and Functions

### Test, Validation, Test Split

```python
lambdata_dggasque.df_utils.train_val_test_split(data, train_per=0.60, val_per=0.20, test_per=0.20, Random_State=None)
```
A function that randomly splits a dataframe into training, validation, and test datasets.

```data```: Dataframe object to be split 
```train_per``: Float between 0 and 1, default = 0.60
                Percentage of dataframe to reserve for training set
```val_per``: Float between 0 and 1, default = 0.20
                Percentage of dataframe to reserve for validation set
```test_per``: Float between 0 and 1, default = 0.20
                Percentage of dataframe to reserve for test set
```Random_State``: int or None, default = None
                   Sets random seed, use for reproducability

#### Example

```python
from lambdata_dggasque import df_utils

df = df_utils.TEST_DF

train, val, test = train_val_test_split(df, Random_State=1)
```

### Processor

```python
lambdata_dggasque.df_utils.Processor
```
A class instance for the purpose of this assignment but really it is more like a module.

#### Functions

```python
missing_values(self, df)
```
Takes an input of a dataframe and prints out columns with missing values and the number of missing values in the column. 

```python
datetime_split(self, df, column)
```
Inputs:
```df``` Dataframe object
```column``` Name of column that is in datetime format

Outputs:
Splits datetime column parses the year month and day into three new columns ['year','month','day'] and adds them to the dataframe

#### Example

```python
from lambdata_dggasque.df_utils import Processor

df = df_utils.TEST_DF

proc = Processor()

# missing values
proc.missing_values(df)
```