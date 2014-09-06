import pandas as pd, celebpred
import numpy as np, pickle


def pred_mbti(a):
   '''    
   Here we convert numeric predictions into mbti predictions. We
   predict the fact that a single functions is in top two or not, as
   well as combination of functions in two, and if these are at top
   two.

   Since make MBTI prediction for a single day (which is a birthday),
   it's important to list options. Predicting a single MBTI result for
   one day would not make sense -- lots of babies are born each day,
   and on one single day, for example, each baby born must be NTP?
   It's more likely that babies born in the same day would have
   different MBTI types, but also, it is likely there is a small list
   of types a person could be that day. For example some days could
   favor STP more, others STJs. On an STJ day, a baby nurtured
   appropiately, could maybe later become an NTJ.

   As an option we present negatives: we make a negative prediction
   and positive prediction for each label, for NeFi, 0.117 for
   negative, 0.067 for positive for example. We create a dataframe out
   of these as well. Then we sort for least negative letter, and also
   for the highest positive. After each of these sortings we pick three
   from lowest negative, and hree from highest positive. By picking
   lowest negative, we are looking at the _opposite of the least
   likely_ MBTI type. If NeFi negative is smallest, its opposite MBTI,
   STJ would be likely.
   '''    
   
   opp = { 'NeFi': 'STJ',  'NeTi': 'SFJ',  'NiTe': 'SFP', 'NiFe': 'STP', 'SiTe': 'NFP',  'SiFe': 'NTP',  'SeFi': 'NTJ',  'SeTi': 'NFJ'}
   map = {'NeFi': 'NFP', 'NeTi': 'NTP', 'NiTe': 'NTJ', 'NiFe': 'NFJ',  'SiTe': 'STJ', 'SiFe': 'SFJ', 'SeFi': 'SFP', 'SeTi': 'STP'}

   opp1 = { 'Ne': 'Si',  'Si': 'Ne',  'Fe': 'Ti', 'Ti': 'Fe',
            'Se': 'Ni', 'Ni': 'Se', 'Te': 'Fi', 'Fi': 'Te'}
   
   res1 = []
   res = []
   for (mbti,neg,pos) in a:
      # only look at 2 letter MBTI labels skip others, i.e. Fi,Te,etc
      if len(mbti) == 2:
         res1.append([mbti, opp1[mbti], neg[1], pos[1]] )
      # only look at 4 letter MBTI labels skip others, i.e. NeFi
      if len(mbti) == 4:
         res.append([map[mbti], opp[mbti], neg[1], pos[1]] )
         
   df = pd.DataFrame(res, columns=['mbti','opp','neg','pos'])
   print df.sort_index(by='pos',ascending=False).head(3)['mbti']
   print df.sort_index(by='neg',ascending=True).head(3)['opp']

   df = pd.DataFrame(res1, columns=['mbti','opp','neg','pos'])
   print df.sort_index(by='pos',ascending=False).head(3)['mbti']

if __name__ == "__main__": 
 
   clfs, train_cols, conf = celebpred.train()
   df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')

   import scipy.sparse as sps
   import pandas as pd, mineprep
   df_t = pd.DataFrame(index=[0], columns=['mbti', 'name', 'occup', 'bday'])
   df_t.loc[0,'mbti'] = 'xxx'
   df_t.loc[0,'bday'] = '24/04/1973'
   #df_t.loc[0,'bday'] = '22/2/1949'
   #df_t.loc[0,'bday'] = '5/10/1945'
   #df_t.loc[0,'bday'] = '8/1/1982'
   #df_t.loc[0,'bday'] = '31/5/1956'
   #df_t.loc[0,'bday'] = '19/1/1949'
   df_t.loc[0,'bday'] = '9/6/1954' # dk

   df2_t = mineprep.astro_enrich(df_t)

   for col in df.columns: 
      if col not in df2_t.columns: df2_t[col] = np.nan
   df2_t = df2_t.drop(celebpred.cols,axis=1)
   df2_t = df2_t[train_cols] # order of cols must look same as during training

   XX = np.array(df2_t.fillna(0))
   print XX.shape

   a = []
   for clf in clfs: 
       res = clfs[clf].predict_proba(XX)[0] # for Logit
       #res = clfs[clf].score_samples(XX)
       #res = clfs[clf].predict(XX)
       a.append( (clf, res, res*conf[clf]) ) # mult score with conf

   pred_mbti(a)
   print df_t.loc[0,'bday']   

