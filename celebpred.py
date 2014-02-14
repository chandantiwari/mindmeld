'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters. Utilizes leave-one-out approach to test
results. One data point is left out of training whose data is used for
prediction, and verification.

SVD->SVM approach is used to predict.
'''
import scipy.sparse.linalg as slin
import scipy.sparse as sps
import numpy.linalg as lin
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import svm
import random

k = 10

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
df = df.reindex(np.random.permutation(df.index))

total = 0
predsum = 0
for idx in df.index:
   clf = svm.SVC(kernel='rbf')
   letter = random.choice(['I','N','T','P'])
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
      Xs = sps.coo_matrix(X)
      U,Sigma,V=slin.svds(Xs,k=k)

      # disable this if you want
      U1 = U[y==1]
      U0 = U[y==0]
      fig = plt.figure()
      ax = Axes3D(fig)
      ax.view_init(elev=10., azim=20)
      ax.plot(U1[:,k-1],U1[:,k-2],U1[:,k-3],'b.')
      plt.hold(True)
      ax.plot(U0[:,k-1],U0[:,k-2],U0[:,k-3],'r.')
      print Sigma
      print letter
      plt.show()

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
