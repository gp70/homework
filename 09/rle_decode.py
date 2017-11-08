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
  
def rle_decode(l):
    temp = 0
    last_was_letter = 0
    str = ''
    for e in l:
        if type(e).__name__ == 'int':
            temp = e
            last_was_letter = 0
        if type(e).__name__ == 'str':
            if last_was_letter == 1:
                str += e
            if last_was_letter == 0:
                str += (e * temp)
                last_was_letter = 1
    return str
  
print(encode('bbbbhslll'))
print(rle_decode(encode('bbbbhslll')))
print(encode('aabcccdeeeeaaa'))
print(rle_decode(encode('aabcccdeeeeaaa')))
print(encode('$$%@@@@99999~~-$@@@'))
print(rle_decode(encode('$$%@@@@99999~~-$@@@')))
