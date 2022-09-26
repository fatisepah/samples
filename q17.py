N=int(input())

List1=[]

for i in range(1,N+1):
    List1.append(i)
#print(List1)
i=1
while len(List1)!=1:
    ListIndexDel=[]
    while i<len(List1):
        ListIndexDel.append(List1[i])
        i+=2

    if i==len(List1)+1:
        i=1
    else:
        i=0
    #print("ListIndexDel",ListIndexDel)
    for j in range(len(ListIndexDel)):
        List1.remove(ListIndexDel[j])
    
    #print("List1",List1)



print(List1[0])
