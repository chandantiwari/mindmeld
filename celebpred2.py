import nimfa
import numpy.linalg as lin
import scipy.sparse as sp
import scipy.linalg as lin
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import random

def __fact_factor(X):
    return X.todense() if sp.isspmatrix(X) else X

clf = DecisionTreeClassifier(max_depth=8)
print clf

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
naivesum = 0
total = 0
predsum = 0
for idx in df.index:
   print df.ix[idx]['name']
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
   
   fctr = nimfa.mf(np.array(X),
                   seed = "nndsvd", 
                   rank = 30, 
                   method = "bmf", 
                   max_iter = 40, 
                   initialize_only = True,
                   lambda_w = 1.1,
                   lambda_h = 1.1)

   res = nimfa.mf_run(fctr)
   thres = 0.3
   X = __fact_factor(res.basis())       
   X = np.abs(np.round(X - 0.5 + thres))
   XB = __fact_factor(res.coef())
   XB = np.abs(np.round(XB - 0.5 + thres))
   
   res=clf.fit(X,y)
   print clf.score(X,y) 

   testrow=testrow.drop(cols)
   total += 1
   naive = random.choice([0,1])

   XB = XB.astype(bool)
   testrow = testrow.reshape((len(testrow),1)).astype(bool)
   testrow2 = np.dot(lin.pinv(XB.T),testrow)

   print testrow2.T[0]
   pred = clf.predict(testrow2.T[0])
   if pred == testres: predsum += 1
   if naive == testres: naivesum += 1
   print 'pred',predsum, 'naive', naivesum, 'total', total, naivesum/float(total)*100, predsum/float(total)*100

