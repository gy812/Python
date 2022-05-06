def arrengement(n,p):
    return fact(n,p)/fact(n-p,p)
def fact(n,p):
    F=1
    for i in range(1,n+1):
        F=F*i
    return F

n=int(input("donner n:"))
p=int(input("donner p:"))
while not ((1<=p)and(p<=n)):
    p=int(input("donner p:"))
print(arrengement(n,p))