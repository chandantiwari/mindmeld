import os
from datetime import datetime
import pandas as pd
import mindmeld, numpy as np

# now populate all astrological values using results from mindmeld.calculate
def f(x):
    res = mindmeld.calculate(str(int(x['bday'])))
    for lew in res['lewi']: x['lewi'+str(lew)] = 1
    if res['chinese']: x['chinese'] = res['chinese']
    if res['spiller']: x['spiller'] = res['spiller']
    if res['millman']:
        x['mill0'] = res['millman'][0]
        x['mill1'] = res['millman'][1]
    return x

df = pd.read_csv("./data/lewi.dat", sep=' ', names=['bday','rest','chinese','spiller','mill0','mill1'])
df['bday'] = df['bday'].map(lambda x: int(x))
df = df[df['bday'] > 19400101]
df = df[:100]

for x in map(lambda x: 'lewi'+str(x),range(278)): df[x] = np.nan
df2 = df.apply(f, axis=1)
df2 = df2.drop('rest',axis=1)
#df3, _, _ = one_hot_dataframe(df2,['spiller','chinese'], replace=True)
df2.to_csv("/tmp/out.csv",sep=';',index=None)
