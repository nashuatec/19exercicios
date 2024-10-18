valorcompra= float(input("Qual o valor da compra?:"))
if valorcompra >100:
    desconto = valorcompra * 0.1
    print(f"O Valor da compra eh {valorcompra - desconto}")
else:
    print(f"o valor da comprae eh {valorcompra}")   