from array import array
from statistics import median
from threading import Thread
import pandas as pd

listFem = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')
listMasc = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')

listM = listMasc.sort_values("name").loc[:,"name"].values.tolist()
listF = listFem.sort_values("name").loc[:,"name"].values.tolist()

def binarySearch(list_ibge, name):
    lenght = len(list_ibge)
    left = 0
    right = lenght - 1

    while(left <= right):
        middle = int ((left + right)/2)
        if list_ibge[middle] == name:
            print(name)
            return name
            break
        if name < list_ibge[middle]:
            right = middle -1
        if name > list_ibge[middle]:
            left = middle + 1
        else:
            print("name not found")

nameF = input("Insert a feminine name: ")
nameM = input("Insert a masculine name: ")

x1 = Thread(target=binarySearch(listM, nameM))
x2 = Thread(target=binarySearch(listF, nameF))

x1.start()
x2.start()

x1.join()
x2.join()