Calculation of

Grant Lewi Numbers (based on decans)

Dan Millman Numerology

Jan Spiller Moon North Node Astrology

Chinese Astrology

Myers-Briggs Test

using open source Python code

Example:

import mindmeld
print mindmeld.calculate('19401010')

The result will look like:

{'lewi': [83, 154, 159, 189, 227, 243, 256, 259, 264], 'spiller':
'Libra', 'millman': [16, 7, 1, 6, 7], 'chinese': 'Dragon', 'cycle': 9}

The calculation of Lewi numbers is the most beneficial part of this
package, doing the same calculation by hand is very time
consuming. The decan information required for this calculation are
taken from SwissEph package. We wrapped this library with some Java
code found under jlewi directory. 

All details for sign, number explanations can be found under
doc/details folder. For Spiller sign Taurus explanation for example
see under doc/details/spiller/Taurus.html

A Myers-Briggs Test can be found under doc folder. Its output is not
interfaced with Python code yet. There is only simple Javascript
checks performed on the input.

Myers-Briggs and Astrology Connection

I was curious about how scientific astrology could be; so I performed
a test using machine learning. I scraped celebrity data from
celebritytypes.com site for their MBTI types. Seperately I downloaded
celebrity birthdays from another site and generated their Lewi,
Millman, Chinese, Spiller sign data. I connected the two, so I had a
data source of ~300 data points which had both scientific and
astrologic data to play with.

For each data point, I made it held-out test data, I trained a
classifier using the rest, and testing the success on the held-out
record. The aim was trying to predict letters of MBTI type, I or E, N
or S, etc.

The result I obtained was %56 which indicates the presence of a
pattern. Since the dimensionality of this data is high, the classifier
would benefit greatly from presence of more data.

