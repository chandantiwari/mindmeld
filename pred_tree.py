from scipy.io import mmread
import pandas as pd, celebpred, sys, os
sys.path.append('%s/Downloads/xgboost/python' % os.environ['HOME'])
import xgboost as xgb
import numpy as np, celebpred_tree
import scipy.sparse as sps
import pandas as pd, mineprep

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

conf = celebpred_tree.train()

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
data = xgb.DMatrix( XX )
bst = xgb.Booster()

for letter in celebpred.letter_cols:
   bst.load_model( '/tmp/tree_%s.model' % letter )
   res = bst.predict(data)
   print letter, res, conf[letter]*res

print df_t.loc[0,'bday']   
