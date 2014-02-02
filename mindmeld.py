from datetime import datetime
import pandas as pd
import numpy as np
import mapping, itertools

lewi = pd.read_csv('./app/lewi.dat',names=['date','lewis'],sep=' ')
decans = pd.read_csv('./app/decans.dat',names=['date','decans'],sep=' ')
spiller = pd.read_csv("./app/spiller",names=['from','to','sign'])
chinese = pd.read_csv("./app/chinese",names=['from','to','sign'])
planets = ['sun','mo','mer','ven','mar','ju','sa','ur','ne','pl']
smap = mapping.init()

sun_moon_table = np.array(range(144)).reshape((12,12)) + 1

def get_lewi(date):
   tmp=np.array(lewi[lewi['date']==int(date)]['lewis'])
   res = tmp[0].split(':')
   return res[:-1]

def get_decans(date):
   tmp=np.array(decans[decans['date']==int(date)]['decans'])
   res = tmp[0].split(':')   
   res = res[:-1]
   res = map(int, res)
   return res

def calculate_millman(date):
    millman = []
    sum1 = 0; sum2 = 0
    for s in date: sum1+=int(s)
    for s in str(sum1): sum2+=int(s)
    millman.append(sum1)
    millman.append(sum2)
    for s in str(sum1)+str(sum2): millman.append(int(s))
    res = []
    res = [x for x in millman[2:] if x not in res]
    res.append(str(millman[0])+str(millman[1]))
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

   step_signs = ['*', 'sq', 'tri', 'opp', 'tri', 'sq', '*']
   steps = np.array([6,9,12,18,24,27,30])
   decans = np.array(decans)
   print 'decans',decans,'\n'
   for planet in planets:
      decan = decans[planets.index(planet)]
      print 'planet',planet,'at decan', decan
      relpos = steps + decan; relpos = map(lambda x: x % 36,relpos)
      print 'relpos',relpos
      for pos,step_sign in itertools.izip(relpos,step_signs):
         matches = np.array(range(10))[decans == pos]
         pls = np.array(planets)[decans == pos]
         if len(matches)>0:
            #print matches,pls,step_sign
            for match,p in itertools.izip(matches,pls):
               print 'from',planet,'to',p,step_sign,match
               if not pd.isnull(smap.ix[planet,step_sign]) and (p in smap.ix[planet,step_sign]):
                  print smap.ix[planet,step_sign][p]
                  res.append(smap.ix[planet,step_sign][p])


   print 'self matches---'
   for i,dec in enumerate(decans):
      matches = np.array(range(10))[decans==dec]
      if len(matches) > 1:
         print 'matches',matches
         for x in matches:
            if i<x:
               print planets[i],'matches',planets[x]
               if not pd.isnull(smap.ix[planets[i],'tick']) and (planets[x] in smap.ix[planets[i],'tick']):
                  res.append(smap.ix[planets[i],'tick'][planets[x]])
            
                  
   return sorted(res)


# grant lewi
print calculate_lewi([8,11,10,4,7,32,30,26,10,8])
print get_lewi('19020608')
print 'from book 28,154,163,174,181,188,189,209,220,231'

#print calculate_lewi(get_decans('19730424'))
#print get_lewi('19730424')

# book sample 61
#print calculate_lewi([17,1,19,22,10,11,28,2,16,12])

