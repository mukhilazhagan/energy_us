# -*- coding: utf-8 -*-
'''

To find correlation between energy usage across distribution

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
try:
    data_aep = pd.read_csv("./dataset/hourly_energy_consumption/AEP_hourly.csv") 
except():
    print("file not found")
'''    


data_aep = pd.read_csv("./dataset/hourly_energy_consumption/AEP_hourly.csv") 
print(data_aep.head())
print(data_aep.info())
print(data_aep.describe())

print( type(data_aep) )

plt.figure(figsize = (10,10) )
plt.plot(data_aep["AEP_MW"])
## To show all objects within
#print( dir(data_aep) )



'''
Upnext develop a model that learns from past day's data
'''



