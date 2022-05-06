def conv_10_16(x):
    ch=''
    while not(x==0):
        b=x%16
        if b<10:
            s=str(b)
            ch=s+ch
        else:
            ch=chr(b+55)+ch
        x=x//16
    return ch
x=input('donner x:')
while not (x.isdigit()):
    x=input('donner x:')
x=int(x)
ch=conv_10_16(x)
print("l'entier ",x,"est converti en: ",ch)