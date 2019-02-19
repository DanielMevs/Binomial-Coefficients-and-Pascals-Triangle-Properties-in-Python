import math

"""
Daniel Mevs
Homework 6
"""

def bicoef(n,  m, memory={}):
    """
    find the binary coefficient C(n,m)
    using the recursive Pascal's identity:
    C(n,m) = C(n-1,m-1) + C(n-1,m)

    Note: this is not an efficient method because
    the recursive function calls result in duplication
    of many calculations.
    """
    
    """
    Tracing it out for 4choose2:
    bicoef(4,2)=   bicoef(3,1,_)                +               bicoef(3,2,_)
                    /        \                                 /             \
            bicoef(2,0)       bicoef(2,1)              bicoef(2,1)            bicoef(2,2)
    does not get added            /  \                  /      \                     |
    as a key because    bicoef(1,0) bicoef(1,1)   bicoef(1,0)  bicoef(1,1)           | 
    base-case is reached       /        \                /         \                 | 
                 /            /          \              /           \                |    
                1    +       1       +     1     +     1       +      1     +        1      = 6                   
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

#constructs an array consisting of the nth row of pascal's triangle
#used for every problem except 5 and 6
def const_arr_row(n):
    return [bicoef(n,m) for m in range(n+1)]

#constructs a two-dimensional array of pascal's triangle
#with the first dimension as the row and the second dimension as the column
#used for number 5
def const_arr_pas(N):
    return [[bicoef(n,m) for m in range(N+1)] for n in range(N+1)]

#n choose k summation that will return the same value as the mth term of the fibonacci sequence
#used for number 6
def left_hs(N):
    ls = []
    s = 0
    i = 0
    for m in range(N+1):
        while((m-i) >= i):
            s += bicoef((m-i),i)
            i += 1
        ls.append(s)
        s = 0
        i = 0
    return ls

#1
N = 24
bin_arr = const_arr_row(N)
s = 0
for i in range(len(bin_arr)):
    s += bin_arr[i]
print("1) sum: ", s, ", 2**n: ", 2**N)

#2
s= 0
N = 29
bin_arr = const_arr_row(N)
one = -1
for i in range(len(bin_arr)):
    s += ((one)**i)*bin_arr[i]
print("2) sum: ", s, ", 0: ", 0)

#3
s = 0
N = 24
bin_arr = const_arr_row(N)
for i in range(len(bin_arr)):
    s += (i*bin_arr[i])        
print("3) sum: ", s, ", n2^n-1: ", N*(2)**(N-1))

#4
s = 0
N = 15
bin_arr = const_arr_row(N)
for i in range(len(bin_arr)):
    s += (2**i)*bin_arr[i]      
print("4) sum: ", s, ", 3^n: ", 3**N)

#5
#we will build a matrix consisting of entries of pascal's triangle and work with that


N = 27
m = 5
s = 0
bin_arr = const_arr_pas(N)

for i in range(m, len(bin_arr)):
    s += bin_arr[i][m]
       
print("5) (for m = 5) sum: ", s, ", n+1 choose m+1: ", bicoef(N + 1, m+1))

s = 0
m = 11
bin_arr = const_arr_pas(N)

for i in range(m, len(bin_arr)):
    s += bin_arr[i][m]
     
print("5) (for m = 11) sum: ", s, ", n+1 choose m+1: ", bicoef(N + 1, m+1))

s = 0
m = 17
bin_arr = const_arr_pas(N)

for i in range(m, len(bin_arr)):
    s += bin_arr[i][m]
    
print("5) (for m = 17) sum: ", s, ", n+1 choose m+1: ", bicoef(N + 1, m+1))

#6

N = 30

ls = []
    
F = [1 for i in range(N)]
for i in range(2,N):
    F[i] = F[i-2] + F[i-1]
#print(F)

ls = left_hs(N)

for m in range(1,6):
    print("6) (for m = ", m, ") sum: ", ls[m], ", fibonacci_m: ", F[m])
m = 10
print("6) (for m = ", m, ") sum: ", ls[m], ", fibonacci_m: ", F[m])
m = 16
print("6) (for m = ", m, ") sum: ", ls[m], ", fibonacci_m: ", F[m])
m = 22
print("6) (for m = ", m, ") sum: ", ls[m], ", fibonacci_m: ", F[m])
m = 29
print("6) (for m = ", m, ") sum: ", ls[m], ", fibonacci_m: ", F[m])


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



    
        

