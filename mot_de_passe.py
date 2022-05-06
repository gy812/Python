from random import randint

def genérer():
    x=randint(0,5)
    ch=str(x)
    for i in range(5):
        K=randint(65,90)
        if i==2:
            ch=ch+chr(K).lower()
        else:
            ch = ch + chr(K)
    y=randint(4,8)
    ch=ch+str(y)
    return ch

def remplir():
    F = open("Password.txt", "w+")
    for i in range(15):
        ch=genérer()
        F.write(ch)
        F.write('\n')
    F.close()
    return F

def afficher():
    F = open("Password.txt", "r")
    for i in range(15):
        ch=F.readline()
        print(ch)
    F.close()

F=remplir()
afficher()