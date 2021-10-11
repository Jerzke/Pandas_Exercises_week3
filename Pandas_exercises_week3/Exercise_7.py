import pandas as pd
df = pd.read_csv("C:\Users\Jerzke\Pandas_exercises_week3\Automobile_data.csv")
df = df.sort_values(by=['price','horsepower'], acending=False)
df.head(5)