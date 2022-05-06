def Tri(F,):
    F=open("List.txt","r")
    ch=F.readline()
    ch=F.readline()
    i=0
    ch = F.readline()
    T=[]
    while (ch!=" "):
        ch = F.readline()
        p=ch.find("=")
        E=dict()
        E["Np"]=ch[:p]
        E["Mg"] =float(ch[p+1:])
        T.append(E)
        i=+1
        ch = F.readline()
    F.close()
    n=i-1
    for i in range(n):
        for j in range(n - i - 1):
            if T[j]['MG']< T[i]['MG']:
                T[i], T[j] = T[i], T[j]
    F = open("List.txt", "w")
    F.write("la liste des eleves: "+"\n")