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
import random

# kernel='rbf',degree=4,gamma=0.2) 58.1
# kernel='rbf',gamma=0.1) 58.6
# kernel='sigmoid',gamma=0.1) 59.7
clf = svm.SVC(kernel='sigmoid',gamma=0.1)
print clf

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
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
      k = 2
      try:
         Xs = sps.coo_matrix(X)
         U,Sigma,V=slin.svds(Xs,k=k)
         Sigma = np.diag(Sigma)
         res=clf.fit(U,y)
         testrow2=testrow.drop(cols)
         testrow2=np.dot(np.dot(lin.inv(Sigma),V),testrow2)
         pred = clf.predict(testrow2)
         total += 1
         if pred == testres: predsum += 1
         if total % 5 == 0:
            print df.ix[idx]['name']
            print 'pred',predsum, 'total', total, predsum/float(total)*100
      except Exception, e:
         print e
         pass
      
print 'pred',predsum, 'total', total, predsum/float(total)*100
