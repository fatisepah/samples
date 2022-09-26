in1=input()

for i in range(len(in1)):
    if in1[i]==' ':
        index=i

list1=[]
m=int(in1[0:index])
s=int(in1[index:])
for i in range(10**(m-1),10**m):
    add=0
    stri=str(i)
    for j in range(m):
        add+=int(stri[j])
    if add==s:
        list1.append(i)

if len(list1)==0:
    print('-1 -1')
else:
    print(list1[0],list1[-1])

