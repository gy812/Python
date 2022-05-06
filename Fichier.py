def saisir():
    while True:
        n=int(input("Donner n: "))
        if  2<n<30:
            break
    return n

def remplir(F,n):
    for i in range(n):
        ch=input("SVP donner le nom de l'animal N°"+str(i)+": ")
        F.write(ch+"\n")
    F.close()
    return F
def afficher(F,n):
    F = open("Zoo.txt", "r")
    print("la liste des animaux")
    for i in range(n):
        ch=F.readline()
        print("l'animal",i,":",ch)
    F.close()
#programme_principale
n=saisir()
F = open("Zoo.txt", "w")
remplir(F,n)
afficher(F,n)