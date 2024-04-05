def pat(r):
    k=2*r-2
    for i in range(r):
        for j in range(k):
            print(end=' ')
        k=k-2
        for j in range(i+1):
            print('*',end=' ') 
        print()  
r=int(input('enter'))
pat(r)