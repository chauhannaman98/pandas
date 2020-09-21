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
