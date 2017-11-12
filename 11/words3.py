from collections import Counter
from collections import defaultdict
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import re
def rp(w):
    """
    input: w - string representing a "word"
    output: the string with (most) non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha() or l =='\'':
            result = result + l
    return result

def bwcd(wordlist):
    d=defaultdict(list)
    for n,w in enumerate(wordlist):
        if n <= len(wordlist) - 2:
            d.setdefault((w,wordlist[n+1]),[])
        if n <= len(wordlist) - 3:
            d[(w,wordlist[n+1])].append(wordlist[n+2])
    return dict(d)

def bwcff(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occurs
    """
    text = open(f).read()
    l=[]
    for w in re.split('\s+|--|',text):
        '''
        This is throwing a warning at me because I'm splitting on whitespace
        - turns out it does this whenever a split could result in empty strings.
        However, re.split() currently ignores possible empty string matches.
        Called a FutureWarning because they plan to fix the fact that it ignores
        empty strings later, apparently.
        Doesn't matter either way, because I specifically ignore empty strings.
        UPDATE: Figured out how to suppress it.
        '''
        w = w.lower()
        w = rp(w)
        if w != '': #There were random empty strings so here's me lazily taking care of that
            l.append(w)
    d = bwcd(l)
    return d

d = bwcff(('hamlet.txt'))
for i in range(len(d) - 1):
    print(str(list(d.keys())[i]) + ': ' + str(list(d.values())[i]))