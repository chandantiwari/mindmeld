Calculation of

Grant Lewi Numbers (based on decans)

Dan Millman Numerology

Jan Spiller Moon North Node Astrology

Chinese Astrology

Myers-Briggs Test

using open source Python code

Example:

import mindmeld
print mindmeld.calculate('19410326')

The result will look like:

{'millman': [26, 8, 2, 6, 8], 'chinese': 'Snake', 'sun': 0.0, 'moon':
11.0, 'lewi': [12, 155, 156, 205, 208, 214, 221, 222, 227, 243, 252],
'spiller': 'Libra', 'cycle': 9}

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

Myers-Briggs and Astrology Connection

I was curious about how _scientific_ astrology and numerology was; so
I performed a test using machine learning. I scraped celebrity data
from celebritytypes.com site for their MBTI types, seperately I
downloaded celebrity birthdays from another site, generated their
Lewi, Millman, Chinese, Spiller signs then I connected the two. So the
dataset (of around 300 points) had both scientific and astrologic data
in the same record. Then, for each data point, in a loop, I made it
held-out test data, trained a classifier on the rest, then tested the
result on the held-out record.

The classification aim was trying to predict individual letters of
MBTI type, seperately on each, such as N or S, T or F, J or P. So each
classifier was a two-label classifier. For each test we would only try
to predict one letter at a time.

The average success rate I obtained using this method was %59.5 which
might indicate the presence of a pattern. The naive classifier (random
choice between two labels) would give, unsurprisingly, around 50%. The
dimensionality of this data is high, so this problem can benefit from
more data.
