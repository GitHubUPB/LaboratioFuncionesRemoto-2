def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("numero perfecto")
    else:
        print("numero no perfecto")

n=int(input("Porfavor, digita un numero: "))
perfect_number(n)
