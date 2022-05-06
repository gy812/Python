def genere():
    mot=''
    nb=1
    while nb!=0:
        R=nb%3
        if R==0:
            Y='Ma'
        elif R==1:
            Y='Des'
        elif R==2:
            Y='Son'
        mot=Y+mot
        nb=nb//3
    return mot

def trier():
    n=int(input('donner n: '))
    transférer(T,n)
    tri_insertion(T,n)
    mot=genere()
    F2=Enregistrer(T,n)

def transférer(T,n):
    F1=open('IMG_HEXA.txt','r')
    I=dict()
    for i in range(n):
        I['Hex']=str(input('donner un nombre Hexadecimal: '))
        I['Num']=int(input('donner le numéro de ligne Hexadecimal: '))
        I['Dec']=int(input('donner un nombre decimal: '))
        T.append(I)
        T[i]=F1.read()
    F1.close()

def tri_insertion(T,n):
    for i in range(n):
        V=T[i] 
        j=i
        while((j>=0) and (V<T[j])):
            T[j + 1]=T[j] 
            j=j-1
        T[j]=V

def Enregistrer(T,n):
    F2=open('Resultat.txt','w')
    for i in range(n):
        F2.write(T[i])
    F2.close()
    return F2
#Programme_Principale#
T=[]
trier()
#Programme_Principale#