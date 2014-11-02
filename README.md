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
`doc/details` folder. For Spiller sign Taurus explanation for example
see under `doc/details/spiller/Taurus.html`

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

Script `train.py` and `pred.py` demonstrate some machine learning
techniques on the data. ML code attempts to predict a person's MBTI
type given their base astrological information. Good resuls obtained
here would prove that a pseudoscience - science connection exists, and
that could mean pseudoscience might not be so pseudo after all. We see
promising results on a test set with known MBTI values, predicting the
top function gives an AUC %70. More data would definitely make a
positive difference as the data is high dimensional.

In the input data for each person, the top two functions are 1-hot
encoded, INTP for example has both Ti and Ne as 1. Then we try to
predict an 8 dimensional output (each dimension represents a function)
using a multi-output regressor using 300+ columns as input. The
benefit of using multi-output regressor is any relation between output
variables is captured as well as the relation between input and output.

Previously we were trying to predict each letter of the MBTI type,
training one classifier for each, such as the four letters of I,N,T,P
for INTP. Using the new way a single (multi-output) prediction task is
used instead of 4. Since we predict the top two functions, we are
disregarding the order of those functions -- INTP and ENTP become the
same prediction. This generalized the problem hence increasing the
amount of data for each type of output. The reason this works is that
in order to identify an MBTI type, top two functions are sufficient,
for example NTP can be predicted if we know Ne and Ti are top two
functions. The only remaining task is predicting introversion or
extroversion which only _changes_ the order of the top two functions
-- ENTP has Ne and Ti whereas INTP is Ti and Ne. We did not put much
emphasis on predicting introversion or extroversion.

This way prediction of using functions, instead of letters is much
more in line with the logic of MBTI. Functions are at the core of the
character make-up, not the individual letters.

Another point: since we are making an MBTI prediction for a single day
(which is a birthday), it's important to list options. Predicting only
two functions would not make sense -- lots of babies are born each
day, and on one single day, for example, each baby born must be NTP?
It's more likely that babies born in the same day would have different
MBTI types, but also, it is likely there is a small list of types a
person could be that day. For example some days could favor STP more,
others STJs. On an STJ day, a baby nurtured appropiately, could maybe
later become an NTJ. That's why pred.py will show 4 top functions,
listed in the order of importance.

The training / testing scheme: once the regressor is trained, four
choices are made to predict top two functions. The number of matches
between prediction and reality, which we call "hits" are averaged over
the test set and become the final score.

Feel free to play with the hyperparameters, or code and do let us know
of your results!

## Data

All data files required for ML are under 'data' folder. If you want to
recreate the main file used for training, simply rerun
`mineprep.py`.

Script `scrape.py` will get celebrity mbti types from a known Web
site, and write its output under /tmp. We already ran this once,
copied its output under data so you dont have to run it. This is the
main data we used to train the regressor. The file is
`data/myer-briggs.txt`, when mineprep.py ran it creates the necessary
file.

Your manual additions to celebrity MBTIs, if there is any, should go
under `data/myer-briggs-app.txt` - everything in this file will be
appended to the original file before training file is created by
mineprep.


## MBTI Test

You can take the MBTI test under `doc/mbti_en.html` and once answering
all questions, hit Evaluate and the -1,0,+1 results will be displayed
in a messagebox. Copy these results to clipboard, and from there paste
it in code, as such

```
ans = ":1:-1:-1:1:0:0:0:1:0:-1:0:0:-1:-1:1:-1:0:0:1:1:-1:1:1:1:0:0:0:-1:1:0:1:1:0:0:0:0:0:1:-1:-1:1:1:1:1:1:1:-1:1:1:1:0:-1:-1:-1:-1:1:0:0:0:0:-1:0:0:-1:0:-1:-1:-1:0:0"
ans = ans.split(":")[1:]
print mindmeld.calculate_mb(ans)
```

would give the answer of the questionaire. 


