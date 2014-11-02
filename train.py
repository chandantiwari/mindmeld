from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
import pandas as pd, numpy as np, pickle
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso, Ridge, LinearRegression

s = 0.02

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

   x_train, x_test, y_train, y_test = train_test_split(Xs, y, test_size=s)
   #x_train, x_test, y_train, y_test = train_test_split(Xs, y, test_size=s, random_state=22)

   train_ys = pd.DataFrame(y_train, columns=letter_cols)
   top = train_ys.sum().order(ascending=False).head(4).index
      
   #clf = RandomForestRegressor(max_depth=4,n_estimators=5)
   clf = ExtraTreesRegressor(max_depth=4,n_estimators=10)
   #clf = DecisionTreeRegressor(max_depth=4)
   #clf = Lasso()
   #clf = Ridge()

   # we flatten the output and prediction and set main function to 1
   # on test labels and interpret the regression results as if they
   # are probability assignments to that func being 1. We calculate
   # AUC based on that.
   clf.fit(x_train,y_train)
   tmp_test = y_test.copy(); tmp_test[tmp_test < 1.0] = 0.0
   y_pred = clf.predict(x_test)
   fpr, tpr, thresholds = roc_curve(np.ravel(tmp_test), np.ravel(y_pred))
   roc_auc = auc(fpr, tpr)
   print 'AUC', roc_auc
   
   res = clf.predict(x_test)
   pred_arr = []
   top_arr = []

   for i in range(len(x_test)):
      pred = pd.Series(res[i, :], index=letter_cols).order(ascending=False).head(4).index
      real = pd.Series(y_test[i, :], index=letter_cols).order(ascending=False).head(2).index
      hits = len([x for x in real if x in pred]) / float(len(real))
      print list(pred), list(real), hits
      pred_arr.append(hits)
      hits = len([x for x in real if x in top]) / float(len(real))
      top_arr.append(hits)
   print 'naive',np.mean(np.array(top_arr))
   print 'pred',np.mean(np.array(pred_arr))

   # display most important features
   if 'RandomForest' in str(type(clf)) or 'DecisionTree' in str(type(clf)): 
      imps = pd.Series(list(clf.feature_importances_),index=df2.columns)
      imps = imps.order(ascending=False).head(15)
      print 'important features'
      print np.array(imps.index)
      
   pickle.dump(clf, open( './data/train.pkl', "wb" ) )

if __name__ == "__main__": 
   train()
