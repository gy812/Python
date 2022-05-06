from random import*
def saisir():
    while True:
        n=int(input("donner la taille  du tableau: "))
        if 2<=n<=10:
            break
    return n
def remplir(M,n):
    for i in range(n):
        for j in range(n):
            M[i,j]=randint(65,90)

def afficher(M,n):
    #partie 1#
    for i in range(n):
        for j in range(n):
            print(M[i],[j])
        print()
    #partie 1#
    #partie 2#
    for i in range(n):
        for j in range(n):
            if (i==j):
                print(M[i],[j])
    for i in range(n):
        print(M(i,n-i-1))
    #partie 2#

#programme_Principale#
n=saisir()
M=[]
remplir(M,n)
afficher(M,n)
#programme_Principale#