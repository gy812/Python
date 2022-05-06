def conv_10_2(x):
    ch=''
    while not(x==0):
        b=x%2
        s=str(b)
        ch=s+ch
        x=x//2
    return ch
x=input('donner x:')
while not (x.isdigit()):
    x=input('donner x:')
x=int(x)
ch=conv_10_2(x)
print("l'entier ",x,"est converti en: ",ch)