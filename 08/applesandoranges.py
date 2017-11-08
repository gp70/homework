# s, t = range in which house is
# a = location of apple tree
# b = location of orange tree
# m = # of apples
# n = # of oranges
# list l1 = distance for each apple
# list l2 = distance for each orange

def ao(s,t,a,b,m,n,l1,l2):
    adist=[]
    odist=[]
    acount = 0
    ocount = 0
    for i in l1:
        adist.append(a+i)
    for i in l2:
        odist.append(b+i)
    for i in adist:
        if i in range(s,t):
            acount += 1
    for i in odist:
        if i in range(s,t):
            ocount += 1
    print(acount)
    print(ocount)
    
ao(7,11,5,15,3,2,[-2,2,1],[5,-6])
ao(4,15,3,16,1,2,[-5,4,8,-1],[6,9,13,-3])
