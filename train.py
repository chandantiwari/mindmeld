import pandas as pd, numpy as np, pickle
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso, LinearRegression

s = 0.30
depth = 4

letter_cols = ['Si','Ti','Ne','Fe','Te','Ni','Se','Fi']
junk_cols = ['mbti','name','occup','bday','bday2']

def train():
   df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
   df = df.drop(junk_cols,axis=1)
   df = df.fillna(0)
   print df.shape
   y = df[letter_cols]
   str_cols = ['mbti','name','occup','bday','bday2']
   df2 = df.drop(letter_cols, axis=1)
   df2 += 1e-7
   Xs = np.array(df2)
   print Xs.shape

   #x_train, x_test, y_train, y_test = train_test_split(Xs, y, test_size=s, random_state=55)
   x_train, x_test, y_train, y_test = train_test_split(Xs, y, test_size=s)
   
   #clf = RandomForestRegressor(max_depth=depth,n_estimators=2,random_state=42)
   clf = DecisionTreeRegressor(max_depth=depth)
   #clf = Lasso()
   #clf = LinearRegression()
   clf.fit(x_train,y_train)
   res = clf.predict(x_test)
   hit_arr = []

   for i in range(len(x_test)):
      pred = pd.Series(res[i, :], index=letter_cols).order(ascending=False).head(4).index
      real = pd.Series(y_test[i, :], index=letter_cols).order(ascending=False).head(2).index
      hits = len([x for x in real if x in pred]) / float(len(real))
      print list(pred), list(real), hits
      hit_arr.append(hits)
   print 'pred',np.mean(np.array(hit_arr))

   # display most important features
   if 'RandomForest' in str(type(clf)): 
      imps = pd.Series(list(clf.feature_importances_),index=df2.columns)
      imps = imps.order(ascending=False).head(15)
      print 'important features'
      print np.array(imps.index)
   
   pickle.dump(clf, open( './data/forest.pkl', "wb" ) )

if __name__ == "__main__": 
   train()
