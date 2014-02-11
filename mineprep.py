import pandas as pd
import mindmeld, numpy as np

celebs = pd.read_csv("./data/famousbday.txt",sep=':',header=None, 
names=['name','occup','bday','spiller','chinese','milla','millb','sun','moon'])
celeb_mbti = pd.read_csv("./data/myer-briggs.txt",header=None,sep=':',\
names=['mbti','name'])
df = pd.merge(celeb_mbti,celebs)

from datetime import datetime
def f(s):
   try:
      return datetime.strptime(s, '%d/%m/%Y').date().strftime('%Y%m%d')
   except: 
      return None
df['bday2'] = df['bday'].apply(f)
df.to_csv('/tmp/out.csv',sep=';')

import os
cols = []
lewi = os.listdir('./doc/details/lewi')
lewi = map(lambda x: 'lewi'+x.replace('.html',''),lewi)
cols += lewi
for x in cols: df[x] = np.nan
for i in range(10): df['mills'+str(i)] = np.nan

import mindmeld;reload(mindmeld)
df2 = df[pd.isnull(df['bday2']) == False]
def enrich(x):
   res = mindmeld.calculate(x['bday2'])
   for lew in res['lewi']: x['lewi'+str(lew)] = 1
   if res['chinese']: x['chinese'] = res['chinese']
   if res['spiller']: x['spiller'] = res['spiller']
   x['sun'] = str(res['sun'])
   x['moon'] = str(res['moon'])
   x['milla'] = str(res['millman'][0])
   x['millb'] = str(res['millman'][1])
   x['mills'+str(res['millman'][2])] = 1
   x['mills'+str(res['millman'][3])] = 1
   x['mills'+str(res['millman'][4])] = 1
   return x
df3 = df2.apply(enrich, axis=1)
df3.to_csv('/tmp/out3.csv',sep=';')

from sklearn.feature_extraction import DictVectorizer
def one_hot_dataframe(data, cols, replace=False):
    vec = DictVectorizer()
    mkdict = lambda row: dict((col, row[col]) for col in cols)
    tmp = data[cols].apply(mkdict, axis=1)
    vecData = pd.DataFrame(vec.fit_transform(tmp).toarray())
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return (data, vecData, vec)

df4, _, _ = one_hot_dataframe(df3,['spiller','chinese','milla','millb','sun'], \
                              replace=True)
df4 = df4.replace(0.0,np.nan)

df4['I'] = df4.apply(lambda x: 1 if x['mbti'][0] == 'I' else 0, axis=1)
df4['N'] = df4.apply(lambda x: 1 if x['mbti'][1] == 'N' else 0, axis=1)
df4['T'] = df4.apply(lambda x: 1 if x['mbti'][2] == 'T' else 0, axis=1)
df4['P'] = df4.apply(lambda x: 1 if x['mbti'][3] == 'P' else 0, axis=1)

df4.to_csv('./data/celeb_astro_mbti.csv',sep=';',index=None)
