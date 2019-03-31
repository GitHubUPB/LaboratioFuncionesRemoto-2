def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("numero perfecto")
    else:
        print("numero no perfecto")
    if a<=(n-3) and a>=(n+3):
        print("no es un número casi perfecto")
    else:
        print("es un número casi perfecto") 

n=int(input("digita un numero: "))
perfect_number(n)
 
