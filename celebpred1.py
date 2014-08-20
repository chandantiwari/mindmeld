'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters. Utilizes leave-one-out approach to test
results. One data point is left out of training whose data is used for
prediction, and verification.

SVD->SVM approach is used to predict.
'''
import scipy.sparse as sps
import pandas as pd
import numpy as np
import pandas as pd, mineprep
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.neural_network import BernoulliRBM

cols = ['mbti','name','occup','bday','bday2','Si','Ti','Ne','Fe','Te','Ni','Se','Fi']

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

res = []
for letter in ['Si','Ti','Ne','Fe','Te','Ni','Se','Fi']:
   clf = LogisticRegression(penalty='l2')
   #clf = LinearSVC()
   #clf = BernoulliRBM(n_components=2)
            
   X = df.copy()
   X = X.fillna(0)
   y = X[letter]
   X = X.drop(cols,axis=1)
   Xs = sps.csr_matrix(X)
   Xs = X
   a_train, a_test, y_train, y_test = train_test_split(Xs, y, test_size=0.02,random_state=42)
   clf.fit(a_train, y_train)
   y_pred = clf.predict_proba(a_test)[:,1]
   #y_pred = clf.predict(a_test)   
   #y_pred = clf.score_samples(a_test)
   fpr, tpr, thresholds = roc_curve(y_test, y_pred)
   roc_auc = auc(fpr, tpr)
   print("%s AUC : %f" % (letter, roc_auc))
   res.append(roc_auc)

print 'Avg AUC', np.array(res).mean()
   
