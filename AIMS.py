import pandas as pd
import numpy as np

data = {'Sex': ['male', 'female', 'male', 'male', 'female'],
        'age': [20, 34, 67, 78, 45]}

df = pd.DataFrame(data)


# Ordinal encoding

for i in df.columns:
    if df[i].dtype == 'object':
        b = df[i].unique()
        for index, value in enumerate(b):
            df.loc[df[i] == value, i] = index
print(df)

# One hot encoding

for i in df.columns:
    if df[i].dtype == 'object':
        b = df[i].unique()
        for k in b:
            df[k] = 0

        for j in range(df.shape[0]):
            for m in b:
                if df.loc[j, i] == m:
                    df.loc[j, m] = 1

print(df)

