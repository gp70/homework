def encode_letter(c,r):
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
    return list[(list.index(c) + r + 26) % len(list)]

def encode_string(s,r):
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

def full_encode(s):
    list = []
    for i in range(0,26):
        list.append(encode_string(s,i))
    nlist ='\n'.join(list)
    return nlist

print(encode_letter('a',5))
print(encode_string('A test string', 5))
print(full_encode('I\'m convinced that mattress/furniture stores exist in a quantum'\
                  ' superposition of grand opening and going out of business sale.'))