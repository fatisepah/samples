in1=int(input())

listfibo=[1]
i=1
while listfibo[i-1]<in1:
    if i==1:
        listfibo.append(2)
    elif listfibo[i-2]+listfibo[i-1]<in1:
        listfibo.append(listfibo[i-2]+listfibo[i-1])
    else:
        break
    i+=1

if in1==0:
    print(0)


sum=0
num=0
for i in range(len(listfibo)):
    sum+=listfibo[(len(listfibo)-1)-i]
    if sum<=in1:
        num=in1-listfibo[(len(listfibo)-1)-i]
        print((len(listfibo))-i,end=" ")
    else:
        sum-=listfibo[(len(listfibo)-1)-i]