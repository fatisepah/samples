in1=int(input())
in2=int(input())

numbers=""
tedad=0
for i in range(in1+1,in2):
    isprime = 1
    for j in range(2, (i //2 + 1)):
        if(i % j == 0):
            isprime = 0
            break
            
    if (isprime == 1):
        if tedad==0:
            numbers=numbers+str(i)
        else:
            numbers=numbers+","+str(i)
        tedad+=1

print(numbers)