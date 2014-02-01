from datetime import datetime
import pandas as pd
import numpy as np

lewi = pd.read_csv('./app/lewi.dat',names=['date','lewis'],sep=' ')
decans = pd.read_csv('./app/decans.dat',names=['date','decans'],sep=' ')
spiller = pd.read_csv("./app/spiller",names=['from','to','sign'])
chinese = pd.read_csv("./app/chinese",names=['from','to','sign'])

sun_moon_table = np.array(range(144)).reshape((12,12)) + 1
planets = ['sun','mo','mer','ven','mar','ju','sat','ur','nep','pl']
mapping = pd.DataFrame(index=planets,columns=['tick','*','sq','tri','opp'])

mapping.ix['mo','tick'] = {'sun':245,'mer':145,'ven':146,'mar':147,'ju':148,'sa':149,'ur':150,'ne':151,'pl':254}
mapping.ix['mo','tri'] = {'sun':246,'mer':152,'ven':153,'mar':154,'ju':155,'sa':156,'ur':157,'ne':158,'pl':255}
mapping.ix['mo','*'] = {'sun':246,'mer':152,'ven':153,'mar':154,'ju':155,'sa':156,'ur':157,'ne':158,'pl':255}
mapping.ix['mo','sq'] = {'sun':247,'mer':159,'ven':160,'mar':161,'ju':162,'sa':163,'ur':164,'ne':165,'pl':256}
mapping.ix['mo','opp'] = {'sun':247,'mer':159,'ven':160,'mar':161,'ju':162,'sa':163,'ur':164,'ne':165,'pl':256}
mapping.ix['ur','tick'] = {'ne':242,'pl':272}
mapping.ix['ur','tri'] = {'ne':243,'pl':273}
mapping.ix['ur','*'] = {'ne':243,'pl':273}
mapping.ix['ur','sq'] = {'ne':244,'pl':274}
mapping.ix['ur','opp'] = {'ne':244,'pl':274}
mapping.ix['ur','tick'] = {'mer':166,'ven':167,'mar':168,'ju':169,'sa':170,'ur':171,'ne':172,'pl':251}

def get_lewi(date):
   tmp=np.array(lewi[lewi['date']==int(date)]['lewis'])
   res = tmp[0].split(':')
   return res[:-1]

def get_decans(date):
   tmp=np.array(decans[decans['date']==int(date)]['decans'])
   res = tmp[0].split(':')
   return res[:-1]

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

def get_spiller(date):
   res = spiller.apply(lambda x: int(date) >=int(x['from']) and int(date) < int(x['to']),axis=1)
   return np.array(spiller[res])[0][2]
   
def get_chinese(date):
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
   return {'chinese':get_chinese(date), 'spiller':get_spiller(date),'millman':calculate_millman(date),'lewi':get_lewi(date)}

def calculate_lewi(decans):
   res = []
   res.append(sun_moon_table[int(float(decans[0])/3),int(float(decans[1])/3)])
   
   angle_locs = [6,9,12,18,24,27,30]
   decans = np.array(decans)
   for planet in planets:
      decan = decans[planets.index(planet)]
      print 'planet',planet,'decan', decan
      shifted = decans + decan
      shifted = map(lambda x: x % 36,shifted)
      print 'shifted',shifted
      break
      
   return res


# grant lewi
# 28,154,163,174,181,188,189,209,220,231
print calculate_lewi([8,11,10,4,7,32,30,26,10,8])
# book sample 61
#print calculate_lewi_decan([17,1,19,22,10,11,28,2,16,12])

#res =  mindmeld.calculate('19020608') 

#print get_lewi('19730424') 
print calculate('19730424') 
#print get_decans('19020608') 
