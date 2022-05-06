def puiss(x,y):
    if y==0:
        return 1
    else:
        return x*puiss(x,y-1)

def CONV_16_10(ch):
    S=0
    for i in range(len(ch)):
        if ch[i] in range('0','9'):
            x=int(ch[i],e)
        else:
            x=(ord(ch[i])-55)
            S=S+x*puiss(16,len(ch)-i)
    return S

def transfert(T):
    global n
    n=int(input('donner n: '))
    F1=open('IMG_HEXA.txt','r')
    i=0
    Fin_Fichier=False
    I=dict()
    for i in range(n):
        T=F1.read()
    while Fin_Fichier==False:
        try:
            i=i+1
            ch=F1.read()
            T[i]['Hex']=ch
            T[i]['Num']=i
            T[i]['Dec']=CONV_16_10(ch)
        except:
            print('ERREUR_FICHIER')
            Fin_Fichier=True
    F1.close()
    return F1
'''
def tri_bulle(T,n):
    valid=True
    while valid==True:
        Test=False
        for i in range(n):
                if T[i]['Dec']>T[i+1]['Dec']:
                    aux=T[i]
                    T[i]=T[i+1]
                    T[i+1]=aux
                    Test=True
        if Test==False:
            Test=False
'''
'''
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
'''
def remplir_res(T,n):
    F2=open('Resultat.txt','w')
    for i in range(n):
        F2.write(ch)
    F2.close()

#Programme_Principale#
F1=open('IMG_HEXA.txt','r')
F2=open('Resultat.txt','w')
T=[]
F1=transfert(T)
#tri_bulle(T,n)
remplir_res(T,n)
#Programme_Principale#