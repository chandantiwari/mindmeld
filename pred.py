import pandas as pd, celebpred
import numpy as np, pickle

clfs, train_cols, conf = celebpred.test()
df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

import scipy.sparse as sps
import pandas as pd, mineprep
df_t = pd.DataFrame(index=[0], columns=['mbti', 'name', 'occup', 'bday'])
df_t.loc[0,'mbti'] = 'xxx'
df_t.loc[0,'bday'] = '24/04/1973'
#df_t.loc[0,'bday'] = '22/2/1949'
#df_t.loc[0,'bday'] = '5/10/1945'
#df_t.loc[0,'bday'] = '8/1/1982'

df2_t = mineprep.astro_enrich(df_t)

for col in df.columns: 
   if col not in df2_t.columns: df2_t[col] = np.nan
df2_t = df2_t.drop(celebpred.cols,axis=1)
# order of cols must look exactly same as during training
df2_t = df2_t[train_cols] 

XX = np.array(df2_t.fillna(0))
print XX.shape

a = []
for clf in clfs: 
    res = clfs[clf].predict_proba(XX)[0] # for Logit
    #res = clfs[clf].score_samples(XX)
    #res = clfs[clf].predict(XX)
    print clf, res, res*conf[clf]
    a.append( (clf, res, res*conf[clf]) )
#pickle.dump(a, open( '/tmp/out.pkl', "wb" ) )    

opp = { 'NeFi': 'STJ',  'NeTi': 'SFJ',  'NiTe': 'SFP', 'NiFe': 'STP', 'SiTe': 'NFP',  'SiFe': 'NTP',  'SeFi': 'NTJ',  'SeTi': 'NFJ'}
map = {'NeFi': 'NFP', 'NeTi': 'NTP', 'NiTe': 'NTJ', 'NiFe': 'NFJ',  'SiTe': 'STJ', 'SiFe': 'SFJ', 'SeFi': 'SFP', 'SeTi': 'STP'}

res = []
for (mbti,neg,pos) in a: 
   if len(mbti) == 4: 
       res.append([map[mbti], opp[mbti], neg[1], pos[1]] )
df = pd.DataFrame(res, columns=['mbti','opp','neg','pos'])

print df.sort_index(by='pos',ascending=False).head(1)['mbti']
print df.sort_index(by='neg',ascending=True).head(3)['opp']


print df_t.loc[0,'bday']   
