from datetime import datetime
import pandas as pd
import numpy as np

lewi = pd.read_csv('./app/lewi.dat',names=['date','lewis'],sep=' ')

def calculate_lewi(date):
   tmp=np.array(lewi[lewi['date']==int(date)]['lewis'])
   return tmp[0].split(':')

def calculate_millman(date):
    millman = []
    sum1 = 0; sum2 = 0
    for s in date: sum1+=int(s)
    for s in str(sum1): sum2+=int(s)
    millman.append(sum1)
    millman.append(sum2)
    for s in str(sum1)+str(sum2): millman.append(int(s))      
    res = []
    res.append(str(millman[0])+str(millman[1]))
    for x in millman[2:]:
      if x not in res:
        res.append(x)
    return res

spiller = pd.read_csv("./app/spiller",names=['from','to','sign'])
print spiller[:3]


