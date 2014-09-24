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

def train():

   num_round = 65
   param = {}
   # use logistic regression loss, use raw prediction before logistic transformation
   # since we only need the rank
   param['objective'] = 'binary:logitraw'
   # scale weight of positive examples
   param['scale_pos_weight'] = 8.
   param['bst:eta'] = 0.4
   param['bst:max_depth'] = 4
   param['eval_metric'] = 'auc'
   param['silent'] = 1
      
   df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
   aucs = {}

   for letter in celebpred.letter_cols:
      X = df.copy()
      X = X.fillna(0)
      y = X[letter]
      X = X.drop(celebpred.cols,axis=1)

      fout = open("/tmp/celeb_feats.txt", "w")
      for i,col in enumerate(X.columns):
         if col == 'diversity': 
            fout.write("%d\t%s\tq\n" % (i,col))
         else: 
            fout.write("%d\t%s\ti\n" % (i,col))
      fout.close()

      Xs = sps.csr_matrix(X)
      a_train, a_test, y_train, y_test = train_test_split(Xs, y, test_size=0.10,random_state=42)
      dtrain = xgb.DMatrix( a_train )
      dtrain.set_label(y_train)
      dtest = xgb.DMatrix( a_test )
      dtest.set_label(y_test)
      evallist  = [(dtest,'eval'), (dtrain,'train')]

      bst = xgb.train( param, dtrain, num_round, evallist )
      preds = bst.predict( dtest )
      labels = dtest.get_label()
      fpr, tpr, thresholds = roc_curve(y_test, preds)
      roc_auc = auc(fpr, tpr)
      print("%s AUC : %f" % (letter,roc_auc))
      aucs[letter] = roc_auc

      bst.dump_model('/tmp/dump_%s.raw.txt' % letter, '/tmp/celeb_feats.txt')
      bst.save_model('/tmp/tree_%s.model' % letter)

   print '\nAverage AUC: %f \n' % np.array(aucs.values()).mean()
   return aucs, X.columns

if __name__ == "__main__": 
   train()   

