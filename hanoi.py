def tower_of_hanoi(n,a,b,c):
    if (n>0):
        print("move 1st disc from",a,"to",c)
        return
    tower_of_hanoi(n-1,a,c,b)
    print("move",n,"from",a,"to",c)
    tower_of_hanoi(n-1,b,a,c)