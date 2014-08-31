from scipy.io import mmread
import pandas as pd, celebpred, sys, os
sys.path.append('%s/Downloads/xgboost/python' % os.environ['HOME'])
import xgboost as xgb, pred
import numpy as np, celebpred_tree
import scipy.sparse as sps
import pandas as pd, mineprep

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

conf, ocols = celebpred_tree.train()

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
df2_t = df2_t[ocols] # order of cols must look same as during training

XX = np.array(df2_t.fillna(0))
data = xgb.DMatrix( XX )
bst = xgb.Booster()

a = []
for letter in celebpred.letter_cols:
   bst.load_model( '/tmp/tree_%s.model' % letter )
   res = bst.predict(data)
   # negate for neg cols, because all we have is one output
   a.append([letter,[-1*res[0], -1*conf[letter]*res[0]],[res[0], conf[letter]*res[0]]  ])

pred.pred_mbti(a)
