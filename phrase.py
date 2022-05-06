def saisir():
    ph =str(input("dooner une chaine de caractere:"))
    while (ph==''):
        ph=str(input("dooner une chaine de caractere:"))
    return ph


def remplir():
    F=open("phrase.txt","w")
    ph=saisir()
    F.write(ph+'\n')
    rep=input("votre repeonse O \ N:")
    while not(rep =='O'):
        ph=saisir()
        F.write(ph+'\n')
        rep=input("votre repeonse O \ N:")
    F.close()
    return F


def net(ph):
    #partie N°1
    ph=ph[:len(ph)-1]
    while(ph.find("  ")!=-1):
        y=ph.find("  ")
        ph=ph[:y]+ph[y+1,len(ph)]
    # partie N°1

    # partie N°2
    if ph[0]=="  ":
        ph=ph[1:]
    # partie N°2

    # partie N°3
    if ph[len(ph)-1]=="  ":
        ph=ph[len(ph) - 1]
    # partie N°3

    # partie N°4
    if(ph[len(ph)-1]==".")and(ph[len(ph)-1]=="  "):
        ph=ph[:len(ph)-2]+"."
    # partie N°4

    # partie N°5
    if (ph[len(ph)-1]!="."):
        ph=ph+"."
    # partie N°5
    return ph


def correction(F):
    F=open("phrase.txt","r")
    Fc=open("phrase_corr.txt","w")

    ph=F.readline()
    while ph!=' ':
        ph=net(ph)
        Fc.write(ph+"\n")
        nb=+1
        ph = F.readline()
    F.close()
    Fc.close()
    print("LE NOMBRE DE PHRASES= ",nb)

F=remplir()
correction(F)&