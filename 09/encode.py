def encode(s):
  l = s
  lfinal = []
  counter = 0
  for n,c in enumerate(l):
    if n != len(l) - 1:
        if l[n+1] != c:
          counter += 1
          if counter != 1:
              lfinal.append(counter)
          lfinal.append(c)
          counter = 0
        if l[n+1] == c:
          counter += 1
    elif n == len(l) - 1:
        counter += 1
        if counter != 1:
            lfinal.append(counter)
        lfinal.append(c)
  return lfinal
  
print(encode('bbbbhslll'))
print(encode('aabcccdeeeeaaa'))
print(encode('$$%@@@@99999~~-$@@@'))

