import scipy.sparse as sps
import pandas as pd, os
import numpy as np, mineprep
import pandas as pd, sys
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
sys.path.append('%s/Downloads/xgboost/python' % os.environ['HOME'])
from scipy.io import mmread
import xgboost as xgb
import celebpred

num_round = 10
param = {'bst:max_depth':2,  'silent':1, 'objective':'binary:logitraw'} 

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
aucs = []

for letter in ['Si','Ti','Ne','Fe','Te','Ni','Se','Fi']:
   X = df.copy()
   X = X.fillna(0)
   y = X[letter]
   X = X.drop(celebpred.cols,axis=1)

   fout = open("./data/celeb_feats.txt", "w")
   for i,col in enumerate(X.columns):
      fout.write("%d\t%s\ti\n" % (i,col))
   fout.close()
   
   Xs = sps.csr_matrix(X)
   a_train, a_test, y_train, y_test = train_test_split(Xs, y, test_size=0.02,random_state=42)
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
   print("%s AUC : %f" % (letter,roc_auc))
   aucs.append(roc_auc)

   bst.dump_model('./data/dump_%s.raw.txt' % letter, './data/celeb_feats.txt')


print '\nAverage AUC', np.array(aucs).mean()

