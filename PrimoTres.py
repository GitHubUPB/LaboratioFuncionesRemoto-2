
def is_prime(a):
    
    count = 0
    for i in range(1,a+1):
        if a% i==0:
            count = count + 1
    if counter==2:
        a=a**0
        return a
    else:
        a=a*0
        return a
    
pr=0
while True:
    pr=pr+1
    try:
        n=int(input("Valor  evaluado: "))
        if n < 0:
            print("numero menor que cero")
            break
        prim=is_prime(n)
        if prim==0:
            print(prim)
        else:
            print(prim)
    except Exception:
        print("-1")

con=0
for i in range(1,pr+1):
    
    if pr% i==0:
        con = con + 1
if con==2:
    
    print("la cantidad de veces calculadas es prima y es: ",pr)
       
else:
    print("la cantidad de veces calculadas no es prima y es: ",pr)
        
        
