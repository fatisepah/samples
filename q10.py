in1=int(input())

def fact(n):
    mul=1
    for i in range(1,n+1):
        mul=mul*i
    return mul

def comb(n,m):
    combb=fact(n)//(fact(m)*fact(n-m))
    return combb


def calc(n):
    sum=0
    for i in range(1,n+1):
        muls=1
        for j in range(1,i+1):
            muls=muls*comb(i,j)
        sum=sum+muls
    print(sum)

calc(in1)

