'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters. Utilizes leave-one-out approach to test
results. One data point is left out of training whose data is used for
prediction, and verification.

Pure RBM is used to predict celebrity MBTI letters. 
'''
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
import rbm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import random
    
clf = svm.SVC(kernel='rbf',gamma=0.1) 

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
df = df.reindex(np.random.permutation(df.index))
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
      hidden = 20
      r = rbm.RBM(num_visible = X.shape[1], num_hidden = hidden)
      X = X.applymap(lambda x: int(x))
      r.train(np.array(X), max_epochs = 30)
      X = r.run_visible(np.array(X))
      res=clf.fit(X,y)
      testrow2=testrow.drop(cols)
      testrow2 = testrow2.map(lambda x: int(x))
      testrow2 = np.array([testrow2])
      testrow2 = r.run_visible(testrow2)
      pred = clf.predict(testrow2[0])
      total += 1
      if pred == testres: predsum += 1
      if total % 5 == 0:
         print df.ix[idx]['name']
         print 'pred',predsum, 'total', total, predsum/float(total)*100
         
print 'pred',predsum, 'total', total, predsum/float(total)*100
