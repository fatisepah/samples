N=int(input())


space=N//2
for i in range(1,N+1,2):
    star=space*' '+i*'*'+(2*space)*' '+i*'*'
    space-=1
    print(star)
space1=1
for i in range(N-2,0,-2):
    star=space1*' '+i*'*'+(2*space1)*' '+i*'*'
    space1+=1
    print(star)