import numpy as np
import pandas as pd

data = pd.read_csv('KK52-14B563-ZD.csv')

data.head()

tmp = data.columns
data.columns = ['column1']
data['column1'][1]

def containAllWord(text, words):
    for oneWord in words:
        if oneWord not in text:
            return False
    return True

for i in range(73):
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

for i in range(73):
    print(data['column1'][i])
data.columns = tmp

data.to_csv('out.csv')