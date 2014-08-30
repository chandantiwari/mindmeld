import pandas as pd, celebpred
import numpy as np

clfs, train_cols, conf = celebpred.test()
df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

import scipy.sparse as sps
import pandas as pd, mineprep
df_t = pd.DataFrame(index=[0], columns=['mbti', 'name', 'occup', 'bday'])
df_t.loc[0,'mbti'] = 'xxx'
df_t.loc[0,'bday'] = '24/04/1973'
#df_t.loc[0,'bday'] = '22/2/1949'
#df_t.loc[0,'bday'] = '5/10/1945'

df2_t = mineprep.astro_enrich(df_t)

for col in df.columns: 
   if col not in df2_t.columns: df2_t[col] = np.nan
df2_t = df2_t.drop(celebpred.cols,axis=1)
# order of cols must look exactly same as during training
df2_t = df2_t[train_cols] 

XX = np.array(df2_t.fillna(0))
print XX.shape

for clf in clfs: 
    res = clfs[clf].predict_proba(XX)[0] # for Logit
    #res = clfs[clf].score_samples(XX)
    #res = clfs[clf].predict(XX)
    print clf, res, res*conf[clf]
    
print df_t.loc[0,'bday']   
