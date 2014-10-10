import pandas as pd, numpy as np, pickle
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor

s = 0.02
depth = 5

letter_cols = ['Si','Ti','Ne','Fe','Te','Ni','Se','Fi']
junk_cols = ['mbti','name','occup','bday','bday2','NeFi','NeTi','NiTe','NiFe','SiTe','SiFe','SeFi','SeTi']

def train():
   df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
   df = df.drop(junk_cols,axis=1)
   df = df.fillna(0)
   print df.shape
   y = df[letter_cols]
   str_cols = ['mbti','name','occup','bday','bday2']
   Xs = df.drop(letter_cols, axis=1)
   Xs += 1e-7
   Xs = np.array(Xs)
   print Xs.shape

   x_train, x_test, y_train, y_test = train_test_split(Xs, y, test_size=s, random_state=42)
   
   clf = RandomForestRegressor(max_depth=depth,n_estimators=30,random_state=42)
   clf.fit(x_train,y_train)
   res = clf.predict(x_test)
   hit_arr = []

   for i in range(len(x_test)):
      pred = pd.Series(res[i, :], index=letter_cols).order(ascending=False).head(3).index    
      real = pd.Series(y_test[i, :], index=letter_cols).order(ascending=False).head(2).index    
      hits = len([x for x in real if x in pred]) / float(len(real))
      print list(pred), list(real), hits
      hit_arr.append(hits)
   print 'pred',np.mean(np.array(hit_arr))

   pickle.dump(clf, open( './data/forest.pkl', "wb" ) )

if __name__ == "__main__": 
   train()
