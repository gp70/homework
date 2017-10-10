def buildstats(f):
    text = open(f).read().lower()
    countlist = []
    num_letters = 0
    for l in 'abcdefghijklmnopqrstuvwxyz':
        num_letters += text.count(l)
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        countlist.append(round(text.count(letter) / num_letters,6))
    fullcount = 0
    for n in countlist:
        fullcount += n
    for i in countlist:
        i = i / fullcount
    return countlist

real_stats = [.08167,.01492,.02782,.04253,.12702,.02228,.02015,.06094,.06966,.00153,.00772,.04025,.02406,
              .06749,.07507,.01929,.00095,.05987,.06327,.09056,.02758,.00978,.02360,.00150,.01974,.00074]
print(real_stats)
print(buildstats('holmes.txt'))

alph = list('abcdefghijklmnopqrstuvwxyz')
for n,c in enumerate(real_stats):
    print(alph[n], ': ', c, buildstats('holmes.txt')[int(n)])
    
print(round(sum(real_stats),6),round(sum(buildstats('holmes.txt')),6))