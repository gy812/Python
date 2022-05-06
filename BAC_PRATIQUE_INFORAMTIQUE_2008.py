from pickle import dump,load

def saisir():
    n=int(input('donner n: '))
    while not(5<n<100):
        n=int(input('donner n: '))
    F1=open('nombres.dat','wb')
    for i in range(n):
        x=int(input('donner x: '))
        while not(0<x<32000):
            x=int(input('donner x: '))
        dump(x,F1)
    F1.close()
    return n,F1

def conv_10_b(x,b):
    ch=''
    while not(x==0):
        r=x%b
        x=x//b
        if b<10:
            s=str(r)
        else:
            s=chr(r+ord('A')-10)
        ch=s+ch
    return ch
def ajouter(F1,n):
    F1=open('nombres.dat','rb')
    F2=open('nombres_CONV.dat','wb')
    for i in range(n):
        x=load(F1)
        E=dict()
        E['dec']=x
        E['bin']=conv_10_b(x,2)
        E['oct']=conv_10_b(x,8)
        E['hex']=conv_10_b(x,16)
        print(E['dec'],'  ',E['bin'],'  ',E['oct'],'  ',E['hex']+'\n')
        dump(E,F2)
    F1.close()
    F2.close()

n,F1=saisir()
ajouter(F1,n)