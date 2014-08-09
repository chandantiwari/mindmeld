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
import pandas as pd
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

cols = ['I','N','T','P','mbti','name','occup','bday','bday2']
for letter in ['I','N','T','P']:
   #clf = LogisticRegression(penalty='l1')
   clf = LinearSVC()

   print letter
   X = df.copy()
   X = X.drop(cols,axis=1)
   X = X.fillna(0)
   Xs = sps.csr_matrix(X)
   y = df[letter]
   a_train, a_test, y_train, y_test = train_test_split(Xs, y, test_size=0.40,random_state=42)
   clf.fit(a_train, y_train)
   #y_pred = clf.predict_proba(a_test)[:,1]
   y_pred = clf.predict(a_test)   
   fpr, tpr, thresholds = roc_curve(y_test, y_pred)
   roc_auc = auc(fpr, tpr)
   print("AUC : %f" % roc_auc)
   
