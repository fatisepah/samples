in1=input()


for i in range(len(in1)//2):
    if in1[i]!=in1[(len(in1)-1)-i]:
        print("NO")
        break
    elif i==((len(in1)//2)-1):
        print("YES")

