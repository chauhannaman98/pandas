import pandas as pd
import numpy as np

data = {
  'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
  'temperature': [32,np.nan,28,24,32,np.nan],
  'windspeed':[6,7,np.nan,np.nan,4,2],
  'event': ['Rain','Sunny','Snow',np.nan,'Rain','Sunny']
  }

df = pd.DataFrame(data=data)
print(df)

# ---- fillna ----
# print('\nfillna\n')
# df_filled = df.fillna({
#   'temperature': 0,
#   'windspeed': 0,
#   'event': 'no event'
# })
# print(df_filled)

# ---- carry forward ----
# new_df = df.fillna(method='ffill', limit=1)
# print(new_df)

# ---- back fill ----
# new_df = df.fillna(method='bfill', axis='columns')
# print(new_df)

# ---- interpolate ----
# new_df = df.interpolate()
# print(new_df)

# ---- dropna ----
# new_df = df.dropna()

# drop where all NaN
# all_drop = df.dropna(how='all')

# atleast 1 valid value
# new_df = df.dropna(threshold=1)
# print(new_df)
