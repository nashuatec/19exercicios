idade = int(input("digite sua idade:"))
maior = 18
if idade >= 18:
    print("Você ja pode dirigir mano")
elif idade <18:
    print(f"Você ainda nao pode dirigir, faltam {maior - idade} ano(s)")
