import scipy.sparse as sps
import pandas as pd
import numpy as np
import pandas as pd, sys
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
sys.path.append('/home/burak/Downloads/xgboost/python')
from scipy.io import mmread
import xgboost as xgb

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
num_round = 20
param = {'bst:max_depth':10,  'silent':1, 'objective':'binary:logitraw'} 

cols = ['I','N','T','P','mbti','name','occup','bday','bday2']
for letter in ['I','N','T','P']:
   print letter
   X = df.copy()
   X = X.drop(cols,axis=1)
   X = X.fillna(0)
   Xs = sps.csr_matrix(X)
   y = df[letter]
   a_train, a_test, y_train, y_test = train_test_split(Xs, y, test_size=0.40,random_state=42)
   dtrain = xgb.DMatrix( a_train )
   dtrain.set_label(y_train)
   dtest = xgb.DMatrix( a_test )
   dtest.set_label(y_test)

   evallist  = [(dtest,'eval'), (dtrain,'train')]

   bst = xgb.train( param, dtrain, num_round, evallist )
   preds = bst.predict( dtest )
   labels = dtest.get_label()
   print ('error=%f' % (  sum(1 for i in range(len(preds)) if int(preds[i]>0.5)!=labels[i]) /float(len(preds))))
   fpr, tpr, thresholds = roc_curve(y_test, preds)
   roc_auc = auc(fpr, tpr)
   print("AUC : %f" % roc_auc)
