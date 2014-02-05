import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
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
#clf = KNeighborsClassifier(n_neighbors=29)
#clf = linear_model.LogisticRegression(penalty='l2',tol=0.1,class_weight='auto')
#clf = naive_bayes.BernoulliNB() 
#clf = svm.SVC(kernel='rbf',gamma=0.2,tol=0.3);
#clf = svm.SVC(kernel='rbf',gamma=0.5,tol=0.35); 
clf = RandomForestClassifier()
#clf = LDA(n_components=2) 
print clf

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
df = df.reindex(np.random.permutation(df.index))
naivesum = 0
total = 0
predsum = 0
for idx in df.index:
   for letter in ['I','N','T','P']:
       X = df.copy()
       X = X.fillna(0)
       y = df[letter]
       testrow = X.ix[idx]
       testres = X.ix[idx][letter]
       X = X.drop(idx)
       y = y.drop(idx)
       cols = ['I','N','T','P','mbti','name','occup','bday','bday2']
       X = X.drop(cols,axis=1)
       #X=X.fillna(0)
       X.div(X.sum(axis=1), axis=1)
       
       clf.fit(X,y)   

       testrow=testrow.drop(cols)
       total += 1
       naive = random.choice([0,1])
       pred = clf.predict(testrow)
       if pred == testres: predsum += 1
       if naive == testres: naivesum += 1
       print 'pred',predsum, 'naive', naivesum, 'total', total, naivesum/float(total)*100, predsum/float(total)*100

