
# DataFrame Dive 1

## Plain DataFrame
```python
import numpy as np
import pandas as pd

empty_df = pd.DataFrame()
empty_df
    Empty DataFrame
    Columns: []
    Index: []

type(empty_df)
    <class 'pandas.core.frame.DataFrame'>


df = pd.DataFrame({"name": ['a1', 'a2', 'a3'], "vol": [10, 20, 30]})

df
    name  vol
    0   a1   10
    1   a2   20
    2   a3   30

type(df)
<class 'pandas.core.frame.DataFrame'>

```

## Columns and Index

```python
df.columns
    Index(['name', 'val'], dtype='object')

df.index
    RangeIndex(start=0, stop=3, step=1)

empty_df.columns
    RangeIndex(start=0, stop=0, step=1)

empty_df.index
    RangeIndex(start=0, stop=0, step=1)


for c in df.columns: print(type(c), c)
    <class 'str'> name
    <class 'str'> vol

for c in df.index: print(type(c), c)
    <class 'int'> 0
    <class 'int'> 1
    <class 'int'> 2

```

## Selection and Series

Select column data using the column name
```python
df['name']
    0    a1
    1    a2
    2    a3
    Name: name, dtype: object

type(df['name'])
<class 'pandas.core.series.Series'>

df['vol']
    0    10
    1    20
    2    30
    Name: vol, dtype: int64

type(df['vol'])
    <class 'pandas.core.series.Series'>

```

Select rows by eveluating a membership expression

```python
PublicSectorBanks = [
    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6",
    "B7",
]

df = pd.DataFrame({"name": ['a1', 'B1', 'a2', 'a3', 'B2', 'B3', 'a4', 'B7'], "vol": [10, 1111, 20, 30, 2222, 3333, 40, 7777]})

# membership mask
ps_mask = df.isin(PublicSectorBanks)

ps_maask
        name    vol
    0  False  False
    1   True  False
    2  False  False
    3  False  False
    4   True  False
    5   True  False
    6  False  False
    7   True  False

type(ps_mask)
    <class 'pandas.core.frame.DataFrame'>
```
Notice the mask indicates column values, *name*, and *vol*, included and excluded in the result set by the membership test.

It is interesting to that 'ps_mask' *is a* DataFrame.

A mask is used to select rows in which the column values are True:

```python
df[ps_mask]
    name  vol
    0  NaN  NaN
    1   B1  NaN
    2  NaN  NaN
    3  NaN  NaN
    4   B2  NaN
    5   B3  NaN
    6  NaN  NaN
    7   B7  NaN
```
We can see that the 'name' column for public sector banks B1, B2, B3, and B7 bears meaning; others show NaN values. Therefore, it makes sense to see if we can filter the rows with non-NaN values from the original dataframe.

**🛈 Predicates *all* and *any***
```python
all([True, True, True])
    True

all([True, True, True, False])
    False

any([False, True, False])
    True

any([False, False, False])
    False

```

pandas yells at us if we try to apply the mask to a series. This makes sense because it is not meaningful to apply a dataframe to another dataframe if their shapes don't match.

```python
df['name'][ps_mask]
    TypeError: Indexing a Series with DataFrame is not supported, use the appropriate DataFrame column

df['name'].shape
    (8,)

ps_mask.shape
    (8, 2)

df.shape
    (8, 2)

df[ps_mask]
    name  vol
    0  NaN  NaN
    1   B1  NaN
    2  NaN  NaN
    3  NaN  NaN
    4   B2  NaN
    5   B3  NaN
    6  NaN  NaN
    7   B7  NaN

```

The solution involves obtaining a series that matches the shape of the target data and selecting the values.

Can we make sense of the following expressions?

```python
ps_mask.any(axis=1)
    0    False
    1     True
    2    False
    3    False
    4     True
    5     True
    6    False
    7     True

ps_mask.any(axis=0)
    name     True
    vol     False
    dtype: bool

```

So equipped with this information, we can try the following:

```python
df[ps_mask.any(axis=1)]
    name   vol
    1   B1  1111
    4   B2  2222
    5   B3  3333
    7   B7  7777

df['name'][ps_mask.any(axis=1)]
    1    B1
    4    B2
    5    B3
    7    B7
    Name: name, dtype: object

df['vol'][ps_mask.any(axis=1)]
    ???

df['name'][ps_mask.any(axis=0)]
    ???

df['vol'][ps_mask.any(axis=0)]
    ???
```
