#CATEGORIA IDADE
idade = int(input("informa sua idade"))
if idade <12 :
    print(f"com {idade} anos você é CRIANÇA")
elif idade >12 and idade <17:
    print(f"com {idade} anos você é um adolescente")
elif idade == 12:
    print("ADOLESCENTE")
else:
    print("ADULTO")