Calculation of

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
