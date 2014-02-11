'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters.
'''
import scipy.sparse as sp
import scipy.linalg as lin
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
import rbm

clf = DecisionTreeClassifier(max_depth=9) #
#clf2 = naive_bayes.BernoulliNB() 
clf2 = GradientBoostingClassifier(n_estimators=2)
clf3 = RandomForestClassifier(n_estimators=4)
#clf3 = KNeighborsClassifier(n_neighbors=2)
#clf3 = svm.SVC(kernel='sigmoid'); 
#clf2 = LDA(n_components=6)
print clf

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
df = df.reindex(np.random.permutation(df.index))
naivesum = 0
total = 0
predsum = 0
for idx in df.index:
   print df.ix[idx]['name']
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
      res=clf.fit(X,y)
      res2=clf2.fit(X,y)
      res3=clf3.fit(X,y)

      testrow2=testrow.drop(cols)
      total += 1
      naive = random.choice([0,1])

      pred = clf.predict(testrow2)
      pred2 = clf2.predict(testrow2)
      pred3 = clf3.predict(testrow2)
      pred = (pred and pred2) or (pred2 and pred3) or (pred and pred3)
      if pred == testres: predsum += 1
      if naive == testres: naivesum += 1
      print 'pred',predsum, 'naive', naivesum, 'total', total, naivesum/float(total)*100, predsum/float(total)*100

