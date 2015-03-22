## What it is

Mindmeld aims to combine all working parts of numerology, psychology
and astrology (yes!). The methods we utilize here are mostly unknown
to the general public; most people know about sun signs (Capricorn,
Taurus, blah) which has 1 out of 12 possibilities. The method here
(Lewi) uses all sun and moon combinations which has 12x12 = 144
character possibilities. Lewi method also looks at other planet
combinations, that will supply additional character info. Jan Spiller
method looks at moon readings differently, and the result is another
in-depth character reading. The accuracy of this reading can shock
you. Finally Millman numerology, another extremely detailed method to
analyze people.

Example:

```
import mindmeld

res =  mindmeld.calculate(mindmeld.conv("10/3/1968"))
print mindmeld.describe(res)
```

The result will look like:

``` {'millman': [28, 10, 2, 8, 1, 0], 'chinese': 'Monkey', 'lewi':
[136, 161, 163, 183, 196, 199, 211, 214, 216, 235, 243, 246, 272,
276], 'spiller': 'Aries', 'cycle': 2} ```

Simply lookup these results under the `doc/details` folder. For
Millman you would find `millman/2810.txt`, for Chinese
`chinese/Monkey.html`, so on..

Cycle is the Millman period your life is on; according to his method
life proceeds in 9 year cycles, 1 is time to start something 9 to
enjoy its fruits (and not start something new). Here is an interesting
exercise; starting from the cycle you are at go back in time, per
year, If cycle says 4 for example, and the current year is 2015,

```
2015 4
2014 3
2013 2
2012 1
2011 9
2010 8
...
```

and try to remember the state of your life at those moments in
time. The results should be revealing. 

## MBTI Test

You can also take the MBTI test under `doc/mbti_en.html` and once
answering all questions, hit Evaluate and the -1,0,+1 results will be
displayed in a messagebox. Copy these results to clipboard, and from
there paste it in code, as such

```
ans = ":1:-1:-1:1:0:0:0:1:0:-1:0:0:-1:-1:1:-1:0:0:1:1:-1:1:1:1:0:0:0:-1:1:0:1:1:0:0:0:0:0:1:-1:-1:1:1:1:1:1:1:-1:1:1:1:0:-1:-1:-1:-1:1:0:0:0:0:-1:0:0:-1:0:-1:-1:-1:0:0"
ans = ans.split(":")[1:]
print mindmeld.calculate_mb(ans)
```

would give the answer of the questionaire. 


##Lewi Files

There are some base files that mindmeld uses from the subproject
`jlewi`; Mindmeld already has a ustable Lewi file, so no regeneration
is necessary. If one wants to regenerate this lewi file though,
everything required is in this subfolder. This is a Java project, see
its README for further info.

The calculation of Lewi numbers is the most beneficial part of this
package, doing the same calculation by hand was very time consuming
(The decan information required for this calculation are calculated
through SwissEph package which we wrapped with the Java code found
under jlewi directory, whose output is already under `data` folder).

## Summary

The features of this package are the calculation of:

Grant Lewi Numbers (based on decans)

Dan Millman Numerology

Jan Spiller Moon North Node Astrology

Chinese Astrology

Myers-Briggs Test

