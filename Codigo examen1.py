x=int(input())

if(x>=0)and(x%2==0):
    print("ES LUNES")
    
    if (x==15):
        print("FESTIVO")
    else:
        print("Laborable")

else:
    print("ES MARTES")
    
if (x%2==1)or(x>2):
    print("ES JUEVES")
elif(x>8):
    print("es SABADO")