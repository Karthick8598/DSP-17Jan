# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:59:54 2021

@author: vikas
"""

import pandas as pd


!pip install pydataset


#import pydataset

from pydataset import data

data('')

df = data('mtcars')

type(df)

df.to_csv('D:\\ML-Lab\\DSP-17Jan\\mtcars.csv')

df



import pandas as pd

df1 = pd.read_csv('mtcars.csv')

df1

df1.head()

df1.head(10)

df1.tail()
df1.tail(10)

df.shape[0]

s1 = pd.Series(range(100,100+df1.shape[0]))

s1

df1.set_index(s1)


ps2 = pd.Series([1,4,8,33,22], dtype='float')
ps2


ps3 = pd.Series([1,4,8,33,22], dtype='int')
ps3

ps3.index
ps3.values


ps4 = pd.Series([1,4,5,6,8], index=['a','b','c','d','e'])
ps4

ps5 = pd.Series([1,4,5,6,8], index=['a','a','c','e','e'])
ps5

ps5[0]
ps5[3]
ps5['a']


ps6 = pd.Series([1,4,5,6,8], index=[3,4,5,6,7])

ps6[3]

ps6.loc[3]
ps6.iloc[3]


pd7 = pd.Series({'a':10,'b':20, 'c':30,'d':50,'e':60})

pd7

pd7['b':'d']

pd7['c':]

pd7[['c', 'e']]


pd7>35

pd7[pd7>35]

pd7[(pd7>25) & (pd7<60)]


course = pd.Series(['B.Tech', 'MTech', 'MBA', 'PHD'])
strength = pd.Series([100, 20, 200, 10])
fees = pd.Series([1,1.5,2, 0.5])
course
strength
fees

pd1 = pd.DataFrame([course, strength, fees])
pd1


pd1 = pd.DataFrame({'Course':course, 'Strength':strength, 'Fees':fees})
pd1

df.columns
pd1.columns

pd1.values

import numpy as np
np.mean(pd1['Strength'].values)

pd1.index


pd1['Course']

pd1.Course

pd1.loc[0]

pd1

pd1.iloc[0]


pd1

pd1['Course']=='MBA'

pd1[pd1['Course']=='MBA']

pd1[pd1['Fees']>1.0]



import numpy as np
import pandas as pd

arr = np.random.randint(100, 200, size= 100)
arr

s1 = pd.Series(arr)
s1

arr = np.random.randint(100, 200, size= (10,10))
arr

s1 = pd.DataFrame(arr)

s1



#missing Value Identification

p1 = pd.Series([None, np.nan, None, 100])

p1
p1.isna()

sum(p1.isna())




pd3 = pd.DataFrame({'course':course, 'strength':strength, 'fees':fees, 'placed':p1})
pd3

pd3.isnull()

pd3.notnull()
pd3
pd3.dropna()

pd3
pd3.dropna(axis=0)

pd3.dropna(axis=1)

pd3.dropna(axis='rows')

pd3.dropna(axis='columns')


pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000, None], ['Vikas', None, None, None, None], ['kanika', 28, None, 5000, None], ['tanvi', 20, 'F', None, None], ['poonam',45,'F',None,None],['upen',None,'M',None, None]])
pd4

pd4.dropna(axis='rows')

pd4.dropna(axis='columns')
pd4
pd4.dropna(axis='rows', how ='all')

pd4.dropna(axis='columns', how ='all')

pd4.dropna(axis='columns', how ='any')

pd4
pd4.dropna(axis='columns', thresh=3)




placed= pd.Series([1,2, None, 5, None, None, 8])
placed

placed.fillna(0)

placed.fillna(method='ffill')

placed.fillna(method='bfill')


pd4
pd4.fillna(0)
pd4
pd4.fillna(method ='ffill', axis=0)
pd4
pd4.fillna(method ='ffill', axis=1)




df =pd.read_csv('invoice.csv')

df.fillna(method='ffill')




grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }

grades1

df1 = pd.DataFrame(grades1)
df1

grades2 = {'subject3': ['A1','B1','A2','A3'],'subject4': ['A2','A1','B2','B3']}

df2 = pd.DataFrame(grades2)
df2


df1
df2
pd.concat([df1,df2])

pd.concat([df1,df2], axis = 0)

pd.concat([df1,df2], axis = 1)

pd.concat([df1,df2], axis = 0, ignore_index=True)




import pandas as pd

rollno = pd.Series(range(1,11))


L1 = []

for i in range(1,11):
    L1.append('Student'+str(i))

L1


L2 = ['Student'+str(i) for i in range(1,11)]

name = pd.Series(L1)
name

genderlist = ['M','F']

import numpy as np

gender = np.random.choice(genderlist, size=10)

gender



pd5 = pd.DataFrame({'rollno':rollno, 'name':name, 'gender':gender})

pd5



marks1 = np.random.randint(0,100, size=10)
marks2 = np.random.randint(0,100, size=10)

pd6 = pd.DataFrame({'rollno':rollno, 'marks1':marks1, 'marks2':marks2})
pd6

pd.concat([pd5,pd6], axis=1, keys='rollno')



course = np.random.choice(a=['BBA','MBA','BTECH'], size=10)
course


pd6 = pd.DataFrame({'rollno':rollno, 'course':course, 'marks1':marks1,'marks2':marks2})
pd6
pd5


pd7 = pd.merge(pd5,pd6)
pd7






rollno = pd.Series(range(1,11))

L2 = ['Student'+str(i) for i in range(1,11)]

name = pd.Series(L1)
name

import numpy as np
genderlist = ['M','F']
gender = np.random.choice(genderlist, size=10)
gender

pd5 = pd.DataFrame({'rollno':rollno, 'name':name, 'gender':gender})
pd5



marks1 = np.random.randint(0,100, size=10)
marks2 = np.random.randint(0,100, size=10)

rollno1 = pd.Series(range(6,16))

course = np.random.choice(a=['BBA','MBA','BTECH'], size=10)
course

pd6 = pd.DataFrame({'rollno':rollno1, 'course':course, 'marks1':marks1,'marks2':marks2})
pd6
pd5


pd7 = pd.merge(pd5,pd6)
pd7

pd8 = pd.merge(pd5,pd6, how='outer')
pd8

pd9 = pd.merge(pd5,pd6, how='left')
pd9

pd9 = pd.merge(pd5,pd6, how='right')
pd9

pd10 = pd.merge(pd5,pd6, on='rollno')
pd10



pd6 = pd.DataFrame({'rollno1':rollno1, 'course':course, 'marks1':marks1,'marks2':marks2})
pd6
pd5

pd10 = pd.merge(pd5,pd6, left_on='rollno', right_on='rollno1')
pd10


pd6 = pd.DataFrame({'rollno':rollno, 'course':course, 'marks1':marks1,'marks2':marks2})

pd11 = pd.merge(pd5, pd6)
pd11

fee = pd.Series({'BTECH':'1L', 'MBA':'1.5L', 'BBA':'0.75L'})

fee = pd.DataFrame({'fee':fee})
fee

pd11
fee

pd12 = pd.merge(pd11, fee, left_on='course',right_index= True )

pd12.to_csv('MergedData.csv')


pd12.columns
pd12.describe
pd12.drop_duplicates()
pd12.sort_index()
pd12.sort_values(by = 'marks1', ascending= True)
pd12.values
pd12.dtypes
pd12.isna()
pd12.isnull()

pd12.nunique()
pd12.shape
pd12.size







































































































































