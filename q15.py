N=int(input())

listNum=[]
for i in range(N):
    listNum.append(int(input()))

for Number in listNum:
    sumaval=0
    sumnumber=0
    for N in range(2,Number):
        i=N
        stri=str(i)
        for j in range(len(str(i))):
            #print(len(str(i)))
            sumnumber+=int(stri[j])
        for factor in range(2, i + 1):
            if i % factor == 0:
                sumaval+=factor
                while i % factor == 0:
                    i = i // factor
                    if i == 1:
                        break
        if Number==N+sumaval+sumnumber:
            print("Yes")
            break
        if N==Number-1:
            print("No")