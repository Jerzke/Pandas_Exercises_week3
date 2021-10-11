import pandas as pd
df = pd.read_csv("C:\Users\Jerzke\Pandas_exercises_week3\Automobile_data.csv")
car_Crtr = df.groupby('company')
toyota = car_Crtr.get_group('toyota')
toyota