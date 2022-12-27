import numpy as np
import pandas as pd


# s = pd.Series([1, 2, 3, np.nan, 5], dtype='float32')
# print(s)

# dates = pd.date_range("20220828", periods=6)
# print(dates)

'''
listtest = list("ABCDEF")
print(listtest)
'''

# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)
"""
df2 = pd.DataFrame(
    {
        'A': 1.0,
        'B': pd.Timestamp('20220828'),
        'C': np.nan,
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['Auto', 'Bus', 'Zug', 'Flugzeug']),
        'F': pd.Series(1, index=[1, 2, 3, 4], dtype='float32')
    }, index=[1, 2, 3, 5]
)

print(df2)
"""

list = list((range(5)))
print(list, type(list))
print(list[len(list)-1])