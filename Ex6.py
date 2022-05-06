from datetime import*
def saisir():
    n=int(input("Donner n:"))
    return n

def remplir(T,n):
    for i in range(n):
        TE = dict()
        TE['Heures']=int(input("HEURS="))
        while not(0<TE['Heures']<23):
            TE['Heures'] = int(input("HEURS="))
        TE['Minutes']=int(input("MINUTES="))
        while not (0<TE['Minutes']<59):
            TE['Minutes'] = int(input("MINUTES="))
        TE['Secondes']=int(input("SECONDES="))
        while not (0<TE['Secondes']<59):
            TE['Secondes'] = int(input("SECONDES="))
        T.append(TE)
n=saisir()
T=[]
remplir(T,n)