from datetime import datetime
import pandas as pd
import numpy as np

lewi = pd.read_csv('./app/lewi.dat',names=['date','lewis'],sep=' ')
spiller = pd.read_csv("./app/spiller",names=['from','to','sign'])
chinese = pd.read_csv("./app/chinese",names=['from','to','sign'])
print spiller[:3]

def calculate_lewi_decan(decans):
   print decans

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

def calculate_spiller(date):
   res = spiller.apply(lambda x: int(date) >=int(x['from']) and int(date) < int(x['to']),axis=1)
   return np.array(spiller[res])[0][2]
   
def calculate_chinese(date):
   res = chinese.apply(lambda x: int(date) >=int(x['from']) and int(date) < int(x['to']),axis=1)
   return np.array(chinese[res])[0][2]
   
def calculate_cycle(d):
    birth_date = datetime.strptime(d, '%Y%m%d').date()
    str_d = birth_date.strftime('%d %B %Y')
    now_year = datetime.now().year      
    cs = str(birth_date.day)+"/"+str(birth_date.month)+"/"+str(now_year)
    cycle_date = datetime.strptime(cs, '%d/%m/%Y').date()  
    str_cycle_date = cycle_date.strftime('%Y%m%d')
    millman = calculate_millman(str_cycle_date)
    res = str(millman[0])
    res = res[0:2]
    total = int(res[0]) + int(res[1])
    if total > 9: 
        res = str(total)
        total = int(res[0]) + int(res[1])
    return total

def calculate(date):
   return [calculate_chinese(date), calculate_spiller(date), calculate_millman(date), 
           calculate_lewi(date), calculate_cycle(date)]


print calculate_lewi_decan([8,11,10,4,7,32,30,26,10,8])

