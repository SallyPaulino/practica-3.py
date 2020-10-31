# Pedir dos números por teclado y decir cual es mayor

P = int(input("Digite un numero: "))
R = int(input("Digite un numero: "))

if P > R:
    print("su primer numero es mayor") 
elif P < R:
    print ("su segundo numero es mayor")
else:
    print("son diferentes")