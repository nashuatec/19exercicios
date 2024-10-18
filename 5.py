media1 = float(input("digite a primeira nota"))
media2 = float(input("digite a segunda nota"))
media3 = float(input("digite a terceira nota"))
media = (media1 + media2 + media3)/3
if media >=7:
    print(f"Aluno foi aprovado com media {media:.2f}")
else:
    print(f"O Aluno foi reprovado com media {media:.2f}")