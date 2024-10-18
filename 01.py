Idade = int(input("informe o ano de nascimento:"))
ano_atual = int(2024)
resultado = (ano_atual - (Idade))
if resultado >=18:
        print(f"O individuo tem {resultado} anos e portanto é MAIOR de idade")
else:
        print(f"O individuo tem {resultado} anos e portante é MENOR de idade")