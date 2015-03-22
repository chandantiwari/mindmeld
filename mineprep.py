import os
from datetime import datetime
import pandas as pd
import mindmeld, numpy as np

def dates(s):
   try: return mindmeld.conv(s)
   except: return None

# now populate all astrological values using results from mindmeld.calculate
def astro(x):
   res = mindmeld.calculate(x['bday2'])
   for lew in res['lewi']: x['lewi'+str(lew)] = 1

   if res['chinese']: x['chinese'] = res['chinese']
   if res['spiller']: x['spiller'] = res['spiller']
   x['M1'] = str(res['millman'][0])
   x['M2'] = str(res['millman'][1])
   x['mills'+str(res['millman'][2])] = 1
   x['mills'+str(res['millman'][3])] = 1
   x['mills'+str(res['millman'][4])] = 1
   return x

def mm(x):
   if   'NTP' in x['mbti']: return pd.Series(['Ti','Ne'])
   elif 'NTJ' in x['mbti']: return pd.Series(['Te','Ni'])
   elif 'NFJ' in x['mbti']: return pd.Series(['Ni','Fe'])
   elif 'NFP' in x['mbti']: return pd.Series(['Ne','Fi'])
   elif 'STJ' in x['mbti']: return pd.Series(['Te','Si'])
   elif 'SFJ' in x['mbti']: return pd.Series(['Si','Fe'])
   elif 'STP' in x['mbti']: return pd.Series(['Ti','Se'])
   elif 'SFP' in x['mbti']: return pd.Series(['Se','Fi'])

def astro_enrich(df):
   df['bday2'] = df['bday'].apply(dates)

   # create (empty) grant lewi fields
   cols = []
   lewi = range(278)
   lewi = map(lambda x: 'lewi'+str(x),lewi)
   cols += lewi
   for x in cols: df[x] = np.nan
      
   # millman fields
   for i in range(10): df['mills'+str(i)] = np.nan
   df['M1'] = np.nan; df['M2'] = np.nan

   # filter out null birthdays
   df2 = df[pd.isnull(df['bday2']) == False]
   
   df3 = df2.apply(astro, axis=1)
   df3 = df3.drop(['name','occup','bday','bday2'],axis=1)

   return df3

if __name__ == "__main__": 
      
    celebs = pd.read_csv("./data/famousbday.txt", sep=':', header=None, names=['name','occup','bday','spiller','chinese'])
    os.system('cat ./data/myer-briggs.txt ./data/myer-briggs-app.txt > /tmp/myer-briggs.txt')    
    celeb_mbti = pd.read_csv("/tmp/myer-briggs.txt",header=None,sep=':',names=['mbti','name'])
    df = pd.merge(celeb_mbti,celebs)
    df2 = astro_enrich(df)
    df2[['mbti1','mbti2']] = df2.apply(mm, axis=1)
    df2.to_csv('./data/celeb_astro_mbti.csv',sep=';',index=None)
