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

