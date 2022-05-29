import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.head(3))

df.sort_values(['Type 1', 'HP'], ascending=[1,0] )  #means type 1 is asceniiding, hp descending