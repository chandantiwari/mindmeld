import os
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
from sha import sha
df2['S'] = df2['S'].map(lambda x: sha(x).hexdigest())
df2['C'] = df2['C'].map(lambda x: sha(x).hexdigest())
df2.to_csv("/tmp/out.csv",sep=';',index=None)
