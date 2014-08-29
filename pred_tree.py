from scipy.io import mmread
import pandas as pd, celebpred, sys, os
sys.path.append('%s/Downloads/xgboost/python' % os.environ['HOME'])
import xgboost as xgb
import numpy as np

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

import scipy.sparse as sps
import pandas as pd, mineprep
df_t = pd.DataFrame(index=[0], columns=['mbti', 'name', 'occup', 'bday'])
df_t.loc[0,'mbti'] = 'xxx'
df_t.loc[0,'bday'] = '24/04/1973'

df2_t = mineprep.astro_enrich(df_t)

for col in df.columns: 
   if col not in df2_t.columns: df2_t[col] = np.nan
df2_t = df2_t.drop(celebpred.cols,axis=1)

#df2_t = df2_t[ocols] 

XX = np.array(df2_t.fillna(0))
print 'XX', XX.shape
data = xgb.DMatrix( XX )
bst = xgb.Booster()

for letter in celebpred.letter_cols:
   bst.load_model( '/tmp/tree_%s.model' % letter )
   res = bst.predict(data)
   print letter, res
