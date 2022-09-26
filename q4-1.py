number=input()

for i in range(len(number)):
    print('%s: '%(number[i]),end='')
    for j in range(int(number[i])):
        print('%s'%(number[i]),end='')
    print("\n")


