def freq(n,l):
    count = 0
    for i in l:
        if i == n:
            count += 1
    return count
def min(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min
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

list = [1,2,2,3,3,3]
for i in range(len(list)):
    print(freq(i,list))
print(min(list))
print(mode(list))

print()

list = [14,3,6,3,5,7,2,3,5,4,2,3,9,7,4]
for i in range(len(list)):
    print(freq(i,list))
print(min(list))
print(mode(list))