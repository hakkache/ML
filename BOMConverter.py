#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:56:18 2018

@author: hakkache
"""
import numpy as np
import pandas as pd

data = pd.read_csv('KK52-14B563-ZD.csv',error_bad_lines=False)

data.head()

tmp = data.columns
data.columns = ['column1']
data['column1'][1]

def containAllWord(text, words):
    for oneWord in words:
        if oneWord not in text:
            return False
    return True

for i in range(len(data.index)):
    if (containAllWord(data['column1'][i],['99999ITEM', ' Wire'])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','5ITEM')
    if (containAllWord(data['column1'][i],['99999ITEM', ' Terminal'])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','5ITEM')
    if (containAllWord(data['column1'][i],['99999ITEM', 'Connector '])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','30ITEM')
    if (containAllWord(data['column1'][i],['99999ITEM', 'Clip'])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','30ITEM')
    if (containAllWord(data['column1'][i],['99999ITEM', 'Tape'])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','30ITEM')
    if (containAllWord(data['column1'][i],['99999ITEM', 'Other'])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','30ITEM')
    if (containAllWord(data['column1'][i],['99999ITEM', 'Tube'])):
            data['column1'][i] =data['column1'][i].replace('99999ITEM','30ITEM')

for i in range(len(data.index)):
    print(data['column1'][i])
data.columns = tmp

data.to_csv('hakkache.csv')

