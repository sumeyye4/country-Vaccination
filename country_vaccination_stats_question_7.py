import pandas as pd 
import numpy as np 

df = pd.read_csv('country_vaccination_stats.csv')  
df['date'] = pd.to_datetime(df['date'], format = '%d/%m/%Y')
 
min_vac = df.groupby('country')['daily_vaccinations'].min().fillna(0) 

df['daily_vaccinations'] = df.apply(lambda row: min_vac[row['country']] if np.isnan(row['daily_vaccinations']) else row['daily_vaccinations'], axis=1 ) 

target_date = pd.to_datetime('01/06/2021', format = '%d/%m/%Y') 
total_vac = df[df['date'] == target_date]['daily_vaccinations'].sum() 

print(total_vac)
                            