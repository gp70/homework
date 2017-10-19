from collections import Counter

testboard1='RBYYBR' # Should fail
testboard2='BYYBRR' # Should fail
testboard3='B_BYYB' # Should succeed
testboard4='BBYYRR' # Should succeed

def ladybug(n,s):
    gamelist = list(s)
    dictionary = dict(Counter(gamelist))
    print(dictionary)
    
    # Test for single element
    for e in dictionary:
        test = dictionary[e]
        if (test == 1) & (e in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            print('NO')
            return
        
    # Test for blank
    for e in dictionary:
        if e == '_':
            print('YES')
            return
                
    # Test for separate items in full list
    for i,e in enumerate(s):
        if i == 0:
            if e != s[i+1]:
                print('NO')
                return
        if i == (len(s) - 1):
            if e != s[i-1]:
                print('NO')
                return
        if (i != 0) & (i != (len(s) - 1)):
            if (e != s[i-1]) & (e != s[i+1]):
                print('NO')
                return
    print('YES')
    
ladybug(6,testboard1)
ladybug(6,testboard2)
ladybug(6,testboard3)
ladybug(6,testboard4)