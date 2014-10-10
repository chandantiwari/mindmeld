import pandas as pd, mineprep, pickle
import numpy as np, celebpred_forest

df = pd.read_csv("./data/celeb_astro_mbti.csv",sep=';')
clf = pickle.load(open('./data/forest.pkl', 'rb'))
df_t = pd.DataFrame(index=[0], columns=['mbti', 'name', 'occup', 'bday'])

def pred_mbti(x):
    df_t.loc[0,'mbti'] = 'xxx'
    df_t.loc[0,'bday'] = x
    df2_t = mineprep.astro_enrich(df_t)
    for col in df.columns:
        if col not in df2_t.columns: df2_t[col] = np.nan
    df2_t = df2_t.drop(celebpred_forest.junk_cols + celebpred_forest.letter_cols, axis=1)
    df2_t = df2_t.fillna(0)
    #print list(np.array(df2_t))
    res = clf.predict(df2_t)
    pred = pd.Series(np.ravel(res), index=celebpred_forest.letter_cols)
    pred = pred.order(ascending=False).head(4).index    
    print df_t.loc[0,'bday']
    print pred

pred_mbti('24/04/1973')
pred_mbti('5/10/1945')
pred_mbti('22/2/1949')
pred_mbti('8/1/1982')
pred_mbti('31/5/1956')
pred_mbti('19/1/1949')
