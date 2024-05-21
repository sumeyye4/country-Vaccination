import pandas as pd 
import numpy as np 

df = pd.read_csv('country_vaccination_stats.csv') 
 
min_vac = df.groupby('country')['daily_vaccinations'].min().fillna(0) 

df['daily_vaccinations'] = df.apply(lambda row: min_vac[row['country']] if np.isnan(row['daily_vaccinations']) else row['daily_vaccinations'], axis=1 ) 

print(df)