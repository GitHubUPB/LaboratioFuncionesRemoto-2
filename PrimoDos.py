
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

while True:
    try:
        n=int(input("Valor evaluado:"))
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
