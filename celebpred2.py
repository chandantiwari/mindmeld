'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters.
'''
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
import rbm
from sklearn import svm
import random

# svm.SVC(kernel='rbf',degree=4,gamma=0.2) # 56.8
# svm.SVC(kernel='rbf') # 57.1
clf = svm.SVC(kernel='rbf',gamma=0.1) # 58.3
# DecisionTreeClassifier(max_depth=7) #57.7

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
      r = rbm.RBM(num_visible = X.shape[1], num_hidden = 10)
      X = X.applymap(lambda x: int(x))
      r.train(np.array(X), max_epochs = 40)
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
