#Triagulos
lado1 = int(input("digite o primeiro lado"))
lado2 = int(input("digite o segundo lado"))
lado3 = int(input("digite o terceiro lado"))
if lado1 == lado2 and lado1 == lado3:
    print("Podemos formar um triangulo equilatero")
elif lado1 == lado2 and lado1 != lado3:
    print("podemos formar um trinagulo Isosceles")
else:
    print("poodemos formar um tringulo Escaleno")

