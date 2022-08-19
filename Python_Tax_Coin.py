import csv
import pandas as pd
import pprint
from pandas import *
from collections import defaultdict
from datetime import datetime

##coin_csv = read_csv('Sample_ARPA.csv', header=0)
coin_csv = read_csv('Sahar_Coin2021.csv', header=0)
size_unit = coin_csv['size unit'].tolist()
date=coin_csv['created at'].tolist()
for i in range(len(date)):
    date[i]=date[i].split('T')[0]
    date[i]=datetime.strptime(date[i], '%Y-%m-%d').strftime('%m/%d/%Y')
list_size_unit = sorted(list(set(size_unit)))
list_size =coin_csv['size'].tolist()
fees = coin_csv['fee'].tolist()
total =coin_csv['total'].tolist()
side = coin_csv['side'].tolist()
list_side = list(set(side))

##############################################

u_list = list(enumerate(size_unit)) #tuple of units and their indices
s_list = list(enumerate(side)) #tuple of sides and their indices


unit_indices = defaultdict(list)
for k, v in u_list:
        unit_indices[v].append(k)
##print('unit_indices', unit_indices)
side_indices = defaultdict(list)
for k, v in s_list:
        side_indices[v].append(k)

##print('side_indices', side_indices)
data = {k: [] for k in list_size_unit} 
for n in list_size_unit:
    unit_index = unit_indices.get(n) #getting the ist of ndices from the dictionary
    BUY_index = side_indices.get('BUY')
    SELL_index= side_indices.get('SELL')
    index1=list(set(unit_index).intersection(BUY_index))
    index2=list(set(unit_index).intersection(SELL_index))
    size = sum([list_size[i] for i in index1])
    description = str(size)+ n 
    cost = abs(sum([total[i] for i in index1]))
    fee = sum([fees[i] for i in index2])
    sell = sum([total[i] for i in index2])
    proceed = sell-fee
    max_index = max(index2)
    data[n].extend([description, date[max_index], proceed, cost])

print("----description", "----date", "----proceed", "----cost")
for key, value in data.items():
##    print(key, ' : ', value)
    print(key, ' : ', '[%s]'%', '.join(map(str, value)))


    
#################################################side

##print('side_ind_BUY', side_ind_BUY)
