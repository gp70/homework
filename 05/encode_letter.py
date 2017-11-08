def encode_letter(c,r):
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
    return list[(list.index(c) + r + 26) % len(list)]

print(encode_letter('a',0))
print(encode_letter('a',1))
print(encode_letter('q',16))