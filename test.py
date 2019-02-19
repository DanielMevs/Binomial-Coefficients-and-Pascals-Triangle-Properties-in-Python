def bicoef(n,  m, memory={}):
    """
    find the binary coefficient C(n,m)
    using the recursive Pascal's identity:
    C(n,m) = C(n-1,m-1) + C(n-1,m)

    Note: this is not an efficient method because
    the recursive function calls result in duplication
    of many calculations.
    """
    #base cases
    if(n < 0):
        return 0
    if(m < 0):
        return 0
    if(m > n):
        return 0
    if(n == 0):
        return 1
    if(m == 0):
        return 1
    if(m == n):
        return 1
    #to store the previous computed values of n and m to update n and m for next computation
    if (n,m) in memory.keys():
        #print("a ",memory.keys())
        #print("b ",memory)
        return memory[(n,m)]
    #print("c ",bicoef(n-1,m-1, memory))
    #print("d ",bicoef(n-1,m,memory))
    memory[(n,m)]=bicoef(n-1,m-1, memory)+bicoef(n-1,m,memory)
    #print("e ", memory)
    return memory[(n,m)]
N = 30


##def left_hs(m):
##    ls = []
##    s = 0
##    i = 0
##    while((m-i) >= i):
##        s += bicoef((m-i),i)
##        i += 1 
##    return s
##
##    
##bin_arr = [[bicoef(n,m) for m in range(N+1)] for n in range(N+1)]
##ls = []
##for m in range(13):
##    ls.append(x(m))
##print(ls)
##
val_ls = [1,2,3,4,5,10,16,22,29]

F_s = [1 for i in range(len(val_ls))]
F = [1 for i in range(N)]
for i in range(2,N):
    F[i] = F[i-2] + F[i-1]
    if F[i] in val_ls:
        F.append(F[i])
    
##print(F)

##def const_arr(n,m):
##    return [bicoef(n,m) for n in range(m, n+1)]
##
##n = 27
##m = 5
##s = 0
##bin_arr = const_arr(n,m)
##
##for i in range(len(bin_arr)):
##    s += bin_arr[i]

def left_hs(val_ls):
    ls = []
    s = 0
    i = 0
    for m in val_ls:
        while((m-i) >= i):
            s += bicoef((m-i),i)
            i += 1
        ls.append(s)
        s = 0
        i = 0
    return ls



ls = left_hs(val_ls)
print(ls)
print(F_s)
##for m in val_ls:
##    print(F[m])
##print(ls)



#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

##                                      1
##                                   1     1
##                                1     2     1
##                             1     3     3     1
##                          1     4     6     4     1
##                       1     5    10    10     5     1
##                    1     6    15    20    15     6     1
##                 1     7    21    35    35    21     7     1
##              1     8    28    56    70    56    28     8     1
##           1     9    36    84   126   126    84    36     9     1
