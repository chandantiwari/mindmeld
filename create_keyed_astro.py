from sha import sha
import os
from sklearn.feature_extraction import DictVectorizer
from datetime import datetime
import pandas as pd
import mindmeld, numpy as np

def f(x):
    res = mindmeld.calculate(str(int(x['bday'])))
    for lew in res['lewi']: x['L'+str(lew)] = 1
    if res['chinese']: x['C'] = res['chinese']
    if res['spiller']: x['S'] = res['spiller']
    if res['millman']:
        x['M0'] = res['millman'][0]
        x['M1'] = res['millman'][1]
    return x

df = pd.read_csv("./data/lewi.dat", sep=' ', names=['bday','rest','C','S','M0','M1'])
df['bday'] = df['bday'].map(lambda x: int(x))
df = df[df['bday'] > 19400101]
df = df[:100]

for x in map(lambda x: 'L'+str(x),range(278)): df[x] = np.nan
df2 = df.apply(f, axis=1)
df2 = df2.drop('rest',axis=1)
df2['S'] = df2['S'].map(lambda x: sha(x).hexdigest())
df2['C'] = df2['C'].map(lambda x: sha(x).hexdigest())
df2['M0'] = df2['M0'].map(lambda x: str(x))
df2['M1'] = df2['M1'].map(lambda x: str(x))

def one_hot_dataframe(data, cols, replace=False):
    vec = DictVectorizer()
    mkdict = lambda row: dict((col, row[col]) for col in cols)
    res = data[cols].apply(mkdict, axis=1)
    vecData = pd.DataFrame(vec.fit_transform(res).toarray())
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return (data, vecData, vec)


df3, _, _ = one_hot_dataframe(df2,['S','C','M0','M1'],True)

df3.to_csv("/tmp/out.csv",sep=';',index=None)
