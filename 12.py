#maior de 03 numeros
num1 = int(input("digite o primeiro numero"))
num2 = int(input("digite o segundo numero"))
num3 = int(input("digite o terceiro numero "))
if num1 > num2 and num1 > num3:
    print(f"o {num1} eh o maior")
elif num2 > num1 and num2 > num3:
    print(f"o {num2} eh o maior")
else:
    print(f"o maior deles eh o {num3}")
    

