
def is_prime(a):
    
    count = 0
    for i in range(1,a+1):
        if a% i==0:
            count = count + 1
    if counter==2:
        print ("Number Prime")
    else:
        print ("Number not prime")

n=int(input("ingrese numero de estudio: "))
is_prime(n)
