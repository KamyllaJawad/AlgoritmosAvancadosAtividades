from statistics import median
import pandas as pd

df = pd.read_csv('nomes-brasileiros-ibge/ibge-fem-10000.csv', delimiter=',')
df2 = pd.read_csv('nomes-brasileiros-ibge/ibge-mas-10000.csv', delimiter=',')

frames = [df,df2]

df3 = pd.concat(frames)

dictionary = df3.sort_values("name").reset_index().loc[:,"name"].to_dict()

reverse_dictionary = dict(map(reversed, dictionary.items()))

name=input("Insert some brazilian name (full caps): ")

print(reverse_dictionary.get(name))
