from collections import Counter
from itertools import groupby
import random
import re
from collections import defaultdict
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
    for w in wordlist:
        d.setdefault(w,[])
    for n,w in enumerate(wordlist):
        if n != len(wordlist) - 1:
            d[w].append(wordlist[n+1])
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
        '''
        w = w.lower()
        w = rp(w)
        if w != '': #There were random empty strings so here's me lazily taking care of that
            l.append(w)
    d = bwcd(l)
    return d

def freq(n,l):
    count = 0
    for i in l:
        if i == n:
            count += 1
    return count

def mode(l):
    l.sort()
    freqlist = []
    for i in l:
        freqlist.append(freq(i,l))
    maxfreq = 0
    modenum = 0
    for i in freqlist:
        if i > maxfreq:
            maxfreq = i
    modenum = freqlist.index(maxfreq)
    return l[modenum]

def sentence(d): #A little side function for fun, expects the output of bwcd - kind of wanted to make it pick randomly from multiple modes, but that was too hard
    s = []
    m = mode(list(d.values())[0])
    s.append(m)
    for _ in range(30):
        m = mode(d[m])
        s.append(m)
    str = ' '.join(s)
    print(str)

d = bwcff("hamlet.txt")
print(d)
print()
sentence(d)