N=int(input())

avamel=[]
tavan=[]
for factor in range(2, N + 1):
    TedadAvamel=0
    while N % factor == 0:
        TedadAvamel+=1
        N = N // factor
        if N == 1:
            break
    if TedadAvamel!=0:
        avamel.append(factor)
        tavan.append(TedadAvamel)

str1=''
for i in range(len(tavan)):
    if tavan[i]==1:
        str1=str1+str(avamel[i])
    else:
        str1=str1+str(avamel[i])+"^"+str(tavan[i])
    if i!=len(tavan)-1:
        str1=str1+"*"

print(str1)



