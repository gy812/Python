def fact(n):
    F=1
    for i in range(1,n+1):
        F=F*i
    return F

def fact_R(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact_R(n-1)

n=int(input("donner n:"))
f=fact(n)
print(f)
fr=fact_R(n)
print(fr)
