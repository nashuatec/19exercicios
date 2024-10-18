#aprovado recuperacao e reprovado
media = int(input("Informe a media do aluno"))
if media >=7:
    print(" o aluno esta aprovado")
elif media <5:
    print("reprovado")
elif media <=5 or media <7:
    print("aluno esta em recuperacao")
else:
    print("não compreendi o comando digite a media em numeros inteiros")
