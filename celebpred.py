import scipy.sparse as sp
import scipy.linalg as lin
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import svm
import random

# Classifier that tries to predict celebrity MBTI letter from
# astrological parameters. We used celebrity data because usually both
# their MBTI type and bday is known. This classifier would benefit
# greatly from more data. The prediction success is already at %57
# which indicates a connection between science (psychology,
# Myers-Briggs) and astrology / numerology.

#clf = DecisionTreeClassifier(max_depth=7) # 
clf = GradientBoostingClassifier(n_estimators=4) # 55
#clf = svm.SVC(kernel='rbf',gamma=0.5,tol=0.35); #gamma=0.5,tol=0.35,54
print clf

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
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
      #X=X.apply(lambda x: x / np.sqrt(np.sum(np.square(x))+1e-16), axis=1)
      res=clf.fit(X,y)
      print clf.score(X,y) 

      testrow2=testrow.drop(cols)
      total += 1
      naive = random.choice([0,1])

      pred = clf.predict(testrow2)
      if pred == testres: predsum += 1
      if naive == testres: naivesum += 1
      print 'pred',predsum, 'naive', naivesum, 'total', total, naivesum/float(total)*100, predsum/float(total)*100

