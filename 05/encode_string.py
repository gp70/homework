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

print(encode_string('Ocean man, take me by the hand, '\
                    'lead me to the land that you understand.', 0))
print(encode_string('Ocean man, take me by the hand, '\
                    'lead me to the land that you understand.', 1))
            
        