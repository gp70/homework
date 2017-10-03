import math

def build_frequency_vector(s):
    # count letters in string
    s = s.lower()
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        v.append(s.count(letter) / num_letters)
    return v

def encode_letter(c,r):
    # shifts letter c by value r
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
    return list[(list.index(c) + r + 26) % len(list)]

def encode_string(s,r):
    # shifts letters in string s by value r
    slist = list(s)
    for i,c in enumerate(slist):
        if c in 'abcdefghijklmnopqrstuvwxyz':
            slist[i] = encode_letter(c,r)
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            slist[i] = c.lower()
            slist[i] = encode_letter(slist[i],r)
            slist[i] = slist[i].upper()
    news = ''.join(slist)
    return news

def distance(l1,l2):
    # euclidean distance between l1 and l2; if lengths are different, higher dimensions are ignored
    length = len(l1)
    if length > len(l2):
        length = len(l2)
    sum = 0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d

real_stats = [.08167,.01492,.02782,.04253,.12702,.02228,.02015,.06094,.06966,.00153,.00772,.04025,.02406,
              .06749,.07507,.01929,.00095,.05987,.06327,.09056,.02758,.00978,.02360,.00150,.01974,.00074]
             # the real deal, right here - actual frequencies of letters in english, on average

def decode(s):
    # attempts to decode rotated string
    freq_list = []
    dist_list = []
    temp = 1
    for i in range(26):
        # building frequency (stats) list of each version
        freq_list.append(build_frequency_vector(encode_string(s,i)))
    for j in freq_list:
        # building list of distances from each version's stats to real stats
        dist_list.append(distance(real_stats,j))
    for k in dist_list:
        # finding lowest value in distances
        if k < temp:
            temp = k
    for l,m in enumerate(dist_list):
        # getting correct index (this could probably have been done in the last loop but I'm tired and this works)
        if temp == m:
            temp = l
    temp = int(temp)
    # making this an int so that python doesn't get mad at me
    return encode_string(s,temp)

test = 'I\'m convinced that mattress/furniture stores exist in a quantum '\
       'superposition of grand opening and going out of business sale.'
        # this will always be my go-to test string
test2 = 'SIR I AM NOT A COMPUTER PERSON AND YOU ARE REFUSING TO HELP ME SO I AM GOING TO HANG UP NOW'
        # also a great test string
test3 = 'Zebras quiz zyzzyvas'
        # wondering how this works with something unusual

print(test)
testcode = encode_string(test,6)
print(testcode)
print(decode(testcode))

print()

print(test2)
testcode2 = encode_string(test2,40)
print(testcode2)
print(decode(testcode2))

print()

print(test3)
testcode3 = encode_string(test3,4)
print(testcode3)
print(decode(testcode3))
# well, it's not an infallible system