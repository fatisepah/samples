number=input()

intNumber=int(number)

i=0

while (2**i)<intNumber:
    i+=1

print(2**i)