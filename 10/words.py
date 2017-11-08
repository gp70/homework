def rp(w): #Removes Punctuation
    result="" #Empty result string
    for l in w: #For letter in word w
        if l.isalpha() or l == '\'': #Checks if letter l is alphanumeric
            result = result + l #Adds l to result string if it's a number or letter
    return result #Returns result

def bwcd(wordlist):
    d={} #Sets d to empty dictionary
    for w in wordlist: #For each word in the list
        d.setdefault(w,0) #Assigns each word to a dictionary, wtih 0 to be returned if key is not found
        d[w] = d[w] + 1 #Adds 1 to key of item in dictionary
    return d #Returns dictionary

def bwcff(f):
    '''
    Input: f, string representing a filename
    Output: A dictionary with keys for words and
            values of the number of times each word occurs
    '''
    f = open(f).read() #Opens file f and makes it a string f
    l=[] #Initializes list l
    for w in f.split(): #Splits f into words, called w
        w = w.lower() #Makes word w lowercase
        w = rp(w) #Executes rp on w, which removes any non alphanumeric characters
        l.append(w) #Adds word to list
    d = bwcd(l) #Executes bwcd on l and assigns the result to d, a dictionary consisting of each word with a key matching its frequency
    return d #Returns d


d = bwcff("hamlet.txt")
v = list(d.values())
v.sort()
d2 = bwcff('sonnets.txt')
v2=list(d2.values())
v2.sort()
print(d)
print(v)
print(d2)
print(v2)

for key in d2:
    if d2[key] >= 150:
        print(key + ' : ' + str(d2[key]))
        
l = [k for k in d2 if d2[k] > 200]
print(l)

l = [k.upper() for k in d2 if d2[k] > 50 and d2[k] < 100]
print(l)

'''
Easy way to do list comprehension
NOT for a in b:
        if ______:
            l.append(___)
NOT for x in range(#):
        l.append(x)
YES l = [x for x in range #]
Makes list of #s 0 to #
[x*x for x in range #]
List from 0 to # of x^2
'''

# Assignment: Make a dictionary which is a list of keys (words in a text file), which are linked to a list of the words which appear after them