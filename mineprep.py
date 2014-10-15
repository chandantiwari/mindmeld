import os
from datetime import datetime
import pandas as pd
import mindmeld, numpy as np
from sklearn.feature_extraction import DictVectorizer

def one_hot_dataframe(data, cols):
    vec = DictVectorizer()
    mkdict = lambda row: dict((col, row[col]) for col in cols)
    vecData = pd.DataFrame(vec.fit_transform(data[cols].to_dict(outtype='records')).toarray())
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    data = data.drop(cols, axis=1)
    data = data.join(vecData)
    return data

def Si(x):
   if 'ISTJ' in x['mbti']: return 1
   if 'ISFJ' in x['mbti']: return 1
   if 'ESTJ' in x['mbti']: return 0.8
   if 'ESFJ' in x['mbti']: return 0.8
   if 'ENFP' in x['mbti']: return 0.1
   if 'ENTP' in x['mbti']: return 0.1
   if 'INFP' in x['mbti']: return 0.1
   if 'INTP' in x['mbti']: return 0.1

def Ti(x):
   if 'ESTP' in x['mbti']: return 1
   if 'ENTP' in x['mbti']: return 1
   if 'ISTP' in x['mbti']: return 0.8
   if 'INTP' in x['mbti']: return 0.8
   if 'INFJ' in x['mbti']: return 0.1
   if 'ISFJ' in x['mbti']: return 0.1
   if 'ENFJ' in x['mbti']: return 0.1
   if 'ESFJ' in x['mbti']: return 0.1

def Ne(x):
   if 'ENTP' in x['mbti']: return 1
   if 'ENFP' in x['mbti']: return 1
   if 'INTP' in x['mbti']: return 0.8
   if 'INFP' in x['mbti']: return 0.8
   if 'ISFJ' in x['mbti']: return 0.1
   if 'ISTJ' in x['mbti']: return 0.1
   if 'ESFJ' in x['mbti']: return 0.1
   if 'ESTJ' in x['mbti']: return 0.1
   
def Fe(x):
   if 'ISFJ' in x['mbti']: return 0.8
   if 'INFJ' in x['mbti']: return 0.8
   if 'ESFJ' in x['mbti']: return 1
   if 'ENFJ' in x['mbti']: return 1
   if 'ENTP' in x['mbti']: return 0.1
   if 'ESTP' in x['mbti']: return 0.1
   if 'INTP' in x['mbti']: return 0.1
   if 'ISTP' in x['mbti']: return 0.1

def Te(x):
   if 'ISTJ' in x['mbti']: return 0.8
   if 'INTJ' in x['mbti']: return 0.8
   if 'ESTJ' in x['mbti']: return 1
   if 'ENTJ' in x['mbti']: return 1
   if 'ENFP' in x['mbti']: return 0.1
   if 'ESFP' in x['mbti']: return 0.1
   if 'INFP' in x['mbti']: return 0.1
   if 'ISFP' in x['mbti']: return 0.1

def Ni(x):
   if 'INTJ' in x['mbti']: return 1
   if 'INFJ' in x['mbti']: return 1
   if 'ENTJ' in x['mbti']: return 0.8
   if 'ENFJ' in x['mbti']: return 0.8
   if 'ESFP' in x['mbti']: return 0.1
   if 'ESTP' in x['mbti']: return 0.1
   if 'ISFP' in x['mbti']: return 0.1
   if 'ISTP' in x['mbti']: return 0.1

def Se(x):
   if 'ESTP' in x['mbti']: return 1
   if 'ESFP' in x['mbti']: return 1
   if 'ISTP' in x['mbti']: return 0.8
   if 'ISFP' in x['mbti']: return 0.8
   if 'INFJ' in x['mbti']: return 0.1
   if 'INTJ' in x['mbti']: return 0.1
   if 'ENFJ' in x['mbti']: return 0.1
   if 'ENTJ' in x['mbti']: return 0.1

def Fi(x):
   if 'ESFP' in x['mbti']: return 0.8
   if 'ENFP' in x['mbti']: return 0.8
   if 'ISFP' in x['mbti']: return 1
   if 'INFP' in x['mbti']: return 1
   if 'INTJ' in x['mbti']: return 0.1
   if 'ISTJ' in x['mbti']: return 0.1
   if 'ENTJ' in x['mbti']: return 0.1
   if 'ESTJ' in x['mbti']: return 0.1
   

'''
Processes birthday field on each row of the dataframe, adding 
astrological parameters, returns the result
'''
def astro_enrich(df_arg):
   df = df_arg.copy()
   # change format of the date
   def f(s):
      try:
          return mindmeld.conv(s)
      except:
          return None
   df['bday2'] = df['bday'].apply(f)

   # create (empty) grant lewi fields
   cols = []
   lewi = range(278)
   lewi = map(lambda x: 'lewi'+str(x),lewi)
   cols += lewi
   for x in cols: df[x] = np.nan
      
   # millman fields
   for i in range(10): df['mills'+str(i)] = np.nan
   df['M1'] = np.nan; df['M2'] = np.nan

   # filter out null birthdays
   df2 = df[pd.isnull(df['bday2']) == False]

   # now populate all astrological values using results from mindmeld.calculate
   def f(x):
      res = mindmeld.calculate(x['bday2'])
      x['sun'] = res['sun']
      x['moon'] = res['moon']
      for lew in res['lewi']: x['lewi'+str(lew)] = 1
      if res['chinese']: x['chinese'] = res['chinese']
      if res['spiller']: x['spiller'] = res['spiller']
      x['M1'] = str(res['millman'][0])
      x['M2'] = str(res['millman'][1])
      x['mills'+str(res['millman'][2])] = 1
      x['mills'+str(res['millman'][3])] = 1
      x['mills'+str(res['millman'][4])] = 1
      return x
   df3 = df2.apply(f, axis=1)

   df4 = one_hot_dataframe(df3,['spiller','chinese','M1','M2'])
   df4 = df4.replace(0.0,np.nan)

   # diversity is the number of 1-hot encoded attributes that are '1',
   # this is used to see how "crowded" a user's profile is. this could
   # be a useful information, if a person has too many attributes (from
   # too many lewi numbers) this could mean they are getting pulled into
   # many directions all at once and that could mean something.
   df5 = df4.drop(['mbti','name','occup','bday','bday2'],axis=1)
   df5 = df5.fillna(0)
   df4['diversity'] = df5.sum(axis=1)

   # the mapping below assigns a 'function' such as Ne, Ti a 1 value
   # if it is at the top two level of a person's MBTI make-up. So an
   # ISTJ would have Te and Si set to 1. We aimed simplifying and
   # training and prediction; because if you can guess top two
   # functions of a person, you can determine their MBTI type.
   df4['Si'] = np.nan;df4['Ti'] = np.nan;df4['Ne'] = np.nan;df4['Fe'] = np.nan
   df4['Te'] = np.nan;df4['Ni'] = np.nan;df4['Se'] = np.nan;df4['Fi'] = np.nan   
   df4['Si'] = df4.apply(Si, axis=1)
   df4['Ti'] = df4.apply(Ti, axis=1)
   df4['Ne'] = df4.apply(Ne, axis=1)
   df4['Fe'] = df4.apply(Fe, axis=1)
   df4['Te'] = df4.apply(Te, axis=1)
   df4['Ni'] = df4.apply(Ni, axis=1)
   df4['Se'] = df4.apply(Se, axis=1)
   df4['Fi'] = df4.apply(Fi, axis=1)
   
   return df4

if __name__ == "__main__": 
 
    celebs = pd.read_csv("./data/famousbday.txt", sep=':', header=None, 
                         names=['name','occup','bday','spiller','chinese'])

    os.system('cat ./data/myer-briggs.txt ./data/myer-briggs-app.txt > /tmp/myer-briggs.txt')
    
    celeb_mbti = pd.read_csv("/tmp/myer-briggs.txt",header=None,sep=':',
                             names=['mbti','name'])

    df = pd.merge(celeb_mbti,celebs)
    df4 = astro_enrich(df)
    df4.to_csv('./data/celeb_astro_mbti.csv',sep=';',index=None)
