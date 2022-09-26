in1=int(input())

sum=0
for i in range(1, (in1 //2 + 1)):
    if(in1 % i == 0):
        sum+=i

if sum==in1:
    print("YES")
else:
    print("NO")