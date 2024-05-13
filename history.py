# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Apr  2 14:12:26 2024)---
import numpy as np
np.__version__
ar1 = np.array([1, 2, 3, 4, 5])
ar1
pip install numpy
type(ar1)
ar2=np.array([[10,20,30],[40,50,60]])
ar2
ar3=np.arange(1,11,2)
ar3
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
ar4
ar4 = np.array([1,2,3,4,5,6]).reshape((2,3))
ar4
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
ar4
ar5=np.zeros((2,3))
ar5
ar6=ar2[0:2, 0:2]
ar6
ar7=ar2[0,:]
ar7
ar8=ar1+10
ar8
ar1+ar8
ar8-ar1
ar1*2
ar1/2
ar9=np.dot(ar2,ar4)
ar9
pip install pandas
import pandas as pd
pd.__version__
data1=[10,20,30,40,50]
data1
data2=['1반','2반','3반','4반','5반']
data2
sr1 = pd.Series(data1)
sr1
sr2=pd.Series(data2)
sr2
sr5=pd.Series(data1,index=[1000,1001,1002,1003,1004])
sr5
sr6=pd.Series(data1,index=data2)
sr6
sr7=pd.Series(data2,index=data1)
sr7
sr1+sr3
sr3=pd.Series([101,102,103,104,105])
sr1+sr3
df2=pd.DataFrame([[89.2, 92.5, 90.8],[92.8, 89.9, 95.2]],index=['중간고사','기말고사'],columns=data2[0:3])
df2
pip install matplorlib

## ---(Thu Apr  4 11:06:18 2024)---
pip install matplotlib
runfile('C:/Users/STORY/.spyder-py3/temp.py', wdir='C:/Users/STORY/.spyder-py3')
runcell(0, 'C:/Users/STORY/.spyder-py3/temp.py')
runfile('C:/Users/STORY/.spyder-py3/temp.py', wdir='C:/Users/STORY/.spyder-py3')

## ---(Thu Apr 18 12:08:43 2024)---
a=['쓰','레','기','통']
a.reverse()
a
>>> dic = {'year': 2020, 'mm': 12, 'dd': 31, 'day': 'Thursday', 'weather': 'snow'}
dic.keys()
dic.values()
        
for i in range(1, 6):
    for j in range(i):
        print("*",end="")
    print()
    
runfile('C:/Users/STORY/.spyder-py3/temp.py', wdir='C:/Users/STORY/.spyder-py3')

## ---(Thu Apr 18 12:39:26 2024)---
def avg(*args):
    if len(args) == 0:
        print("No arguments provided.")
        return
        
runcell(0, 'C:/Users/STORY/.spyder-py3/temp.py')
runfile('C:/Users/STORY/.spyder-py3/temp.py', wdir='C:/Users/STORY/.spyder-py3')
import pandas as pd
df = pd.DataFrame([[500, 450, 520, 610], [690, 700, 820, 900], 
                   [1100, 1030, 1200, 1380], [1500, 1650, 1700, 1850], 
                   [1990, 2020, 2300, 2420], [1020, 1600, 2200, 2550]], 
                  index = ['2015', '2016', '2017', '2018', '2019', '2020'], 
                  columns=['1분기', '2분기', '3분기', '4분기'])
df
df.to_csv('Users', header = 'False')
