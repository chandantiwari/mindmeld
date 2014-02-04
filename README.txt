Calculation of

Grant Lewi Numbers (based on decans)

Dan Millman Numerology

Jan Spiller Moon North Node Astrology

Chinese Astrology

Myers-Briggs Test

using Python code

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

All details for all sign, number explanations can be found under
doc/details folder. For Spiller sign Taurus explanation for example
see under doc/details/spiller/Taurus.html

Myers-Briggs Test can be found under doc folder. Its output is not
interfaced with Python code yet. There is only simple Javascript
checks performed on the input.

