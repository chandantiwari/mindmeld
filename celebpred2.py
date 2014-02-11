'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters.
'''
import scipy.sparse.linalg as slin
import scipy.sparse as sps
import numpy.linalg as lin
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import naive_bayes 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.lda import LDA
import random

#clf = DecisionTreeClassifier(max_depth=5) 
#clf = naive_bayes.BernoulliNB() 
#clf = GradientBoostingClassifier(n_estimators=8)
#clf = RandomForestClassifier(n_estimators=4)
#clf = KNeighborsClassifier(n_neighbors=1,metric=euclidian)
clf = svm.SVC(kernel='rbf'); 
#clf = LDA(n_components=6)
#clf = linear_model.LogisticRegression(class_weight='auto')
print clf

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
#df = df.reindex(np.random.permutation(df.index))
total = 0
predsum = 0
for idx in df.index:
   letter = random.choice(['I','N','T','P'])
   for i in ['x']:
   #for letter in ['I','N','T','P']:
      X = df.copy()
      X = X.fillna(0)
      y = df[letter]*1
      testrow = X.ix[idx]
      testres = X.ix[idx][letter]
      X = X.drop(idx)
      y = y.drop(idx)
      cols = ['I','N','T','P','mbti','name','occup','bday','bday2']
      X = X.drop(cols,axis=1)

      try:
         U,Sigma,V=lin.svd(X)
         Sigma = np.diag(Sigma)
         k = 3
         Sigma = Sigma[:k,:k]
         U = U[:,:k]
         V = V[:,:k]
         res=clf.fit(U,y)

         testrow2=testrow.drop(cols)
         testrow2=np.dot(np.dot(lin.inv(Sigma),V.T),testrow2)
         pred = clf.predict(testrow2)

         total += 1
         if pred == testres: predsum += 1
         if total % 5 == 0:
            print df.ix[idx]['name']
            print 'pred',predsum, 'total', total, predsum/float(total)*100
      except: pass
      
print 'pred',predsum, 'total', total, predsum/float(total)*100
