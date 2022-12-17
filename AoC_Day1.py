# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:29:43 2022

@author: brend
"""

import numpy as np

f = open("AoC_Day1.txt", "r")

data = f.read()
data_into_list = data.replace('\n', ' ').split('  ')

sep_dat=[]
for i in data_into_list:
    i = i.split(' ')
    sep_dat.append(i)

for i in sep_dat:
    for j in i:
        if j == '':
            i.remove(j)

new_data_list = [[int(x) for x in f] for f in sep_dat]
    
summed_list = [sum(each) for each in new_data_list]

print(max(summed_list))
summed_list = np.sort(summed_list)
print(sum(summed_list[-3:]))
    

        



    
    