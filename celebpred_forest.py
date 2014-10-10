'''
Classifier that tries to predict celebrity MBTI letter from
astrological parameters. Utilizes leave-one-out approach to test
results. One data point is left out of training whose data is used for
prediction, and verification.

SVD->SVM approach is used to predict.
'''
import scipy.sparse as sps
import pandas as pd
import numpy as np
import pandas as pd, mineprep
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
import statsmodels.api as sm
from sklearn import cross_validation
from sklearn.neural_network import BernoulliRBM
import collections

cols = ['mbti','name','occup','bday','bday2']

letter_cols = ['Si','Ti','Ne','Fe','Te','Ni','Se','Fi','E','I',
               'NeFi','NeTi','NiTe','NiFe','SiTe','SiFe','SeFi','SeTi']

cols = cols + letter_cols

def train():

   df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')


if __name__ == "__main__": 
   train()
