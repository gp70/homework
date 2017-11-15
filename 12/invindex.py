'''
Inverted index - List of words and documents in which they appear
(Document can be part of a document, too)
Ex) one	 : if you prick us do we not bleed
    two	 : if you tickle us do we not laugh
    three: if you poison us do we not die and
    four	: if you wrong us shall we not revenge
    
    if:[one,two,three,four]
    you:[one,two,three,four]
    prick:[one]
    us:[one,two,three,four]
    do:[one,two,three]
    ...

'''
import csv

# Turns csv into list of dictionaries
def readoff(s):
    l=[]
    f = open(s)
    csvdread = csv.DictReader(f)
    for line in csvdread:
        line.popitem()
        line = dict(line)
        l.append(line)
    f.close()
    return l

def invindex(l):
    index = {'God':(),'pray':(),'heaven':(),'Lord':(),'love':(),'sorry':(),'None':()}
    for i in index:
        temp = []
        for d in l:
            if i.lower() in d['Last Statement'].lower():
                temp.append(d['TDCJ Number'])
        index[i] = tuple(temp)
    return index

l = readoff('offenders-clean.csv')
print(invindex(l))

