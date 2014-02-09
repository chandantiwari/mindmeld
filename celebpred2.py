import scipy.sparse as sp
import scipy.linalg as lin
import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import nimfa
from sklearn import linear_model
from sklearn import naive_bayes 
from sklearn import svm
import random
from sklearn.lda import LDA
from sklearn.qda import QDA
import numpy.linalg as lin

# classifier that tries to predict celebrity MBTI from astrological parameters
# we used celebrities because both their MBTI type and bday is known 
# this classifier would benefit greatly from more data, because the
# dimensionality of the data is high. feel free to scrape
# celebritytypes.com

# tried bunch of different classifiers, highest pred rate is 53.
#clf = KNeighborsClassifier(n_neighbors=10)
#clf = linear_model.LogisticRegression(penalty='l2',class_weight='auto')
#clf = naive_bayes.BernoulliNB() 
#clf = svm.SVC(kernel='rbf',gamma=0.2,tol=0.3);
#clf = svm.SVC(kernel='rbf',gamma=0.5,tol=0.35); 
#clf = RandomForestClassifier()
#clf = GradientBoostingClassifier()
clf = DecisionTreeClassifier(max_depth=10)
#clf = LDA(n_components=2) 
print clf

np.random.seed(1234)
random.seed(1234)

def __fact_factor(X):
    return X.todense() if sp.isspmatrix(X) else X

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
df = df.reindex(np.random.permutation(df.index))
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
   
   X=X.fillna(0)
   #X=X.div(X.sum(axis=0), axis=1)
   #X=X.apply(lambda x: x / np.sqrt(np.sum(np.square(x))+1e-16), axis=1)

   fctr = nimfa.mf(np.array(X),
                   seed = "nndsvd", 
                   rank = 40, 
                   method = "bmf", 
                   max_iter = 40, 
                   initialize_only = True,
                   lambda_w = 1.1,
                   lambda_h = 1.1)

   res = nimfa.mf_run(fctr)
   thres = 0.2
   X = __fact_factor(res.basis())       
   X = np.abs(np.round(X - 0.5 + thres))
   XB = __fact_factor(res.coef())
   XB = np.abs(np.round(XB - 0.5 + thres))
   XB = XB.astype(bool)
   
   res=clf.fit(X,y)
   print clf.score(X,y) 

   testrow=testrow.drop(cols)
   total += 1
   naive = random.choice([0,1])

   testrow = testrow.reshape((len(testrow),1)).astype(bool)
   #testrow2 = np.dot(lin.pinv(XB.T),testrow)
   testrow2,x,x,x = lin.lstsq(XB.T,testrow)
          
   pred = clf.predict(testrow2.T[0]*1)
   if pred == testres: predsum += 1
   if naive == testres: naivesum += 1
   print 'pred',predsum, 'naive', naivesum, 'total', total, naivesum/float(total)*100, predsum/float(total)*100

