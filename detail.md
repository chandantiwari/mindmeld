##Statistical Analysis

If there were enough information, maybe it would be possible to
predict a person's MBTI type given their base astrological
information. We could use celebrity birthdates and MBTI types (since
both are known for some celebrities) to train the model, and then
using simple birthdate, we would attempt to predict an MBTI
output. Good resuls obtained here could prove that a pseudoscience -
science connection exists, and that could mean pseudoscience might not
be so pseudo after all.

Unfortunately we do not have enough data for this. If we had, we
already have an idea how to go about modeling this data:

In the input data for each person, the top two functions would be (and
are, see `mineprep.py`) 1-hot encoded, INTP for example has both Ti
and Ne as 1. In order to identify an MBTI type, top two functions are
sufficient, for example NTP can be predicted if we know Ne and Ti are
top two functions. The only remaining task is predicting introversion
or extroversion which only _changes_ the order of the top two
functions -- ENTP has Ne and Ti whereas INTP is Ti and Ne. We did not
put much emphasis on predicting introversion or extroversion. This way
prediction of using functions, instead of letters is much more in line
with the logic of MBTI. Functions are at the core of the character
make-up, not the individual letters.

Anyway; we did run a simple logistic regression on Ti being 1/0 for
example against spiller, chinese, and millman, almost all variables
were insignificant. Adjusted R^2 was around 10%, but we were not
satisfied with this.

## Data

All data files required for ML are under 'data' folder. If you want to
recreate the main file used for training on celebrities, simply rerun
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

