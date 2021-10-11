import pandas as pd
df = pd.read_csv("C:\Users\Jerzke\Pandas_exercises_week3\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
