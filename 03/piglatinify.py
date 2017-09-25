def piglatinify(s):
    if (s[0] == 'a') or (s[0] == 'e') or (s[0] == 'i') or (s[0] == 'o') or (s[0] == 'u'):
        return s + 'ay'
    else:
        return s[1:len(s)] + s[0] + 'ay'
    
print(piglatinify('hello'))
print(piglatinify('test'))
print(piglatinify('extravagant'))
print(piglatinify('orb'))