import pandas as pd
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import naive_bayes 
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import random
from sklearn.lda import LDA
from sklearn.qda import QDA
import numpy.linalg as lin

# classifier that tries to predict MBTI from astrological parameters
# this classifier would benefit greatly from more data, because the
# dimensionality of the data is high. feel free to scrape
# celebritytypes.com

#clf = KNeighborsClassifier(n_neighbors=5)
#clf = linear_model.LogisticRegression(penalty='l2',class_weight='auto',tol=0.2) 
#clf = naive_bayes.BernoulliNB() 
#clf = svm.SVC(kernel='rbf',gamma=0.2,tol=0.3); #55
clf = svm.SVC(kernel='rbf',gamma=0.5,tol=0.35); #55
#clf = RandomForestClassifier()
#clf = LDA(n_components=4) # 55
#clf = LDA(n_components=4) # 
#clf = svm.SVC(gamma=2, C=1.0)
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
       X=X.fillna(0)
       X = X.apply(lambda x: x / np.sqrt(np.sum(np.square(x))+1e-16), axis=1)
       clf.fit(X,y)   

       testrow=testrow.drop(cols)
       total += 1
       naive = random.choice([0,1])
       pred = clf.predict(testrow)
       if pred == testres: predsum += 1
       if naive == testres: naivesum += 1
       print 'pred',predsum, 'naive', naivesum, 'total', total, naivesum/float(total)*100, predsum/float(total)*100

