def palin(s):
    if s==s[::-1]:
        print('palin')
    else:
        print('not a palin') 
s=input('enter')  
palin(s)
     