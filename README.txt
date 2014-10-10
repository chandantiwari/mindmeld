## Installation

sudo pip install sklearn

## Calculates

Grant Lewi Numbers (based on decans)

Dan Millman Numerology

Jan Spiller Moon North Node Astrology

Chinese Astrology

Myers-Briggs Test

using open source Python code

Example:

```
import mindmeld

res =  mindmeld.calculate(mindmeld.conv("10/3/1968"))
print mindmeld.describe(res)

```

The result will look like:

```
{'millman': [28, 10, 2, 8, 1, 0], 'chinese': 'Monkey', 'sun':
11.0, 'moon': 3.0, 'lewi': [136, 161, 163, 183, 196, 199, 211, 214,
216, 235, 243, 246, 272, 276], 'spiller': 'Aries', 'cycle': 2}
```

The calculation of Lewi numbers is the most beneficial part of this
package, doing the same calculation by hand was very time
consuming. The decan information required for this calculation are
taken from SwissEph package. We wrapped this library with some Java
code found under jlewi directory. 

All details for sign, number explanations can be found under
doc/details folder. For Spiller sign Taurus explanation for example
see under doc/details/spiller/Taurus.html

A 70 question Myers-Briggs Test can be found under doc folder. Its
output is not interfaced with the evaluator Python code yet. There is
only simple Javascript checks performed on the input.

A list of URLs that point to details of each reading can also be
generated, by using the describe function,

```
import mindmeld
res =  mindmeld.calculate(mindmeld.conv("10/3/1968"))
print mindmeld.describe(res)
```

##Lewi Files

All code pertaining to Lewi number generation are under jlewi
subfolder. This is a Java project, see its README for further info. 

##Machine Learning

Script celebpred.py demonstrate some machine learning techniques on
the data. ML code attempts to predict a person's MBTI type given their
base astrological information. Good resuls obtained here would prove
that a pseudoscience - science connection exists, and that could mean
pseudoscience might not be so pseudo after all. On ~400 records with
10% random test split we are able to get a total of 54% AUC on the
test set , for predicting top two MBTI functions (NeTi,NiTe,
etc). More data would definitely make a positive difference.

In the input data for each person, the top two functions are 1-hot
encoded, INTP for example has both Ti and Ne as 1. Each of these
columns become labels during training. We train a different classifier
for each function.

Previously we were trying to predict each letter of the MBTI type,
such as the four letters of I,N,T,P for INTP. Using the new way we
have 2 prediction tasks instead of 4, we predict only the top two
functions, and disregarding the order of those functions, so INTP and
ENTP are the same. The reason for that shortcut is that in order to
identify an MBTI type, top two functions are sufficient, for example
NTP can be predicted if we know Ne and Ti are top two functions. The
only remaining task is predicting introversion or extroversion which
only _changes_ the order of the top two functions -- ENTP has NeTi
whereas INTP TiNe. We did not put much emphasis on predicting I or E,
even though it is one of the prediction tasks in the code, but we dont
use it for full blown MBTI determination.

Predicting all combination of top two functions, effectively reduces
the prediction task to 1. 

This way prediction is an easier task, and is much more in line with
the logic of MBTI. Functions are at the core of the character make-up,
not the individual letters.

All data files required for ML are under 'data' folder. If you want to
recreate the main file used for training, simply rerun
mineprep.py.

Script scrape.py will get celebrity mbti types from a known Web site,
and write its output under /tmp. We already ran this once, copied its
output under data so you dont have to run it. This is the main data we
used to train the classifier. The file is data/myer-briggs.txt, when
mineprep.py ran it creates the necessary file.

Your manual additions to celebrity MBTIs can go under
data/myer-briggs-app.txt - everything in this file will be appended to
the original file before training file is created by mineprep.

File celebpred_tree.py uses Gradient Boosted Regression Trees. We used
xgboost package on Github. In order to use this package, download the
code under your $HOME/Downloads/xgboost and compile it following its
directions.

## Code

In the code we convert numeric predictions into mbti predictions. We
predict the fact that an MBTIfunction is in top two or not, as well as
combination of functions, in twos, are in the top two as well.

Also, since we are making an MBTI prediction for a single day (which
is a birthday), it's important to list options. Predicting a single
MBTI result for one day would not make sense -- lots of babies are
born each day, and on one single day, for example, each baby born must
be NTP?  It's more likely that babies born in the same day would have
different MBTI types, but also, it is likely there is a small list of
types a person could be that day. For example some days could favor
STP more, others STJs. On an STJ day, a baby nurtured appropiately,
could maybe later become an NTJ.


## MBTI Test

You can take the MBTI test under doc/mbti_en.html and once answering
all questions, hit Evaluate and the -1,0,+1 results will be
displayed. These results can be copied to clipboard, and from there 

```ans = ":1:-1:-1:1:0:0:0:1:0:-1:0:0:-1:-1:1:-1:0:0:1:1:-1:1:1:1:0:0:0:-1:1:0:1:1:0:0:0:0:0:1:-1:-1:1:1:1:1:1:1:-1:1:1:1:0:-1:-1:-1:-1:1:0:0:0:0:-1:0:0:-1:0:-1:-1:-1:0:0"
ans = ans.split(":")[1:]
print mindmeld.calculate_mb(ans)
```

would give the answer of the questionaire. 
