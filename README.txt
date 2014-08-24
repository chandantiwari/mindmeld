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
print mindmeld.calculate('19410326')
```

The result will look like:

```
{'millman': [26, 8, 2, 6, 8], 'chinese': 'Snake', 'sun': 0.0, 'moon':
11.0, 'lewi': [12, 155, 156, 205, 208, 214, 221, 222, 227, 243, 252],
'spiller': 'Libra', 'cycle': 9}
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
res = mindmeld.calculate('19410326')
print mindmeld.describe(res)
```

##Lewi Files

All code pertaining to Lewi number generation are under jlewi
subfolder. This is a Java project, see its README for further info. 

##Machine Learning

Script celebpred.py demonstrate some machine learning techniques on
the data. ML code attempts to predict a person's MBTI type given their
base astrological information. This, if can be done, would prove a
direct pseudoscience - science connection. On ~400 records with 4%
random test split we are able to get a total of 60% AUC on the test
set, for predicting top two MBTI functions (Ne,Ti,etc). These results
are promising. More data would definitely make a positive difference.

In the input data, the top two functions of people are 1-hot encoded,
INTP for example has both Ti and Ne as 1, and they become labels
during training. We train a different classifier for each
function.

Previously we were trying to predict each letter of the MBTI type, but
with this new way we have 2 prediction tasks instead of 4, so it is an
easier task, and this style of prediction of much more in line with
the logic of MBTI. Functions are at the core of the character
make-up. Our experiments with logistic regression and bernoulli rbm
have shown good results. A neural network with two outputs (so two
labels) could give more accurate prediction.

All data files required for ML are under 'data' folder. If you want to
recreate the main file used for training, simply rerun
mineprep.py. Script scrape.py will get celebrity mbti types from a
known Web site, and write its output under /tmp. We already ran this
once, it is the file we used to train the classifier. This output file
needs to be copied manually under data, then mineprep.py would have to
be executed again.


