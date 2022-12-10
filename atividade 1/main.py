from statistics import median
import pandas as pd

df = pd.read_csv('nomes-brasileiros-ibge/ibge-fem-10000.csv', delimiter=',')
df2 = pd.read_csv('nomes-brasileiros-ibge/ibge-mas-10000.csv', delimiter=',')

frames = [df,df2]

df3 = pd.concat(frames)

list_ibge = df3.sort_values("name").loc[:,"name"].values.tolist()

name=input("Insert some brazilian name (full caps): ")

def binary_search(list_ibge,name):
    min=0
    mid=0
    max=len(list_ibge)

    while min<=max:
        mid=(min+max)//2

        if(list_ibge[mid]<name):
            min=mid+1
        elif(list_ibge[mid]>name):
            max=mid-1
        else:
            return mid
    return "not found"

print(binary_search(list_ibge,name))