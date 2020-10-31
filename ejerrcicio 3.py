# Pedir tres números por teclado e imprimir el mayor de ellos solamente.

A = int(input("Digite su primer numero: "))
T = int(input("Digite su segundo numero: "))
S = int(input("Digite su tercer numero: "))

if A > T and A > S:
    print("su primer numero es mayor") 
elif T > S and T > A:
    print ("su segundo numero es mayor")
else:
    S > A and S > T
    print("Su tercer numero es mayor")