def PGCD(x,y):
    while not(x==y):
        if x>y:
            x=x-y
        else:
            y=y-x
    return x

def PGCD_R(x,y):
    if x==y:
        return x
    elif x>y:
        return PGCD(x-y,y)
    else:
        return PGCD(x,y-x)

x=int(input("donner x:"))
y=int(input("donner y:"))

print(PGCD(x,y))
print(PGCD_R(x,y))