nome=input("DIGA O NOME DO ALUNO")
nota1=float(input(F"DIGITE A PRIMEIRA NOTA DO ALUNO{nome}"))
nota2=float(input("DIGITE A SEGUNDA NOTA DO ALUNO"))
nota3=float(input("DIGITE A TERCEIRA NOTA DO ALUNO"))
media=(nota1+nota2+nota3)/3
resultado=print(F"A média do (a)aluno em questão é:{media}")
if media>=7:
    print(F"O(a)aluno(a){nome} está: APROVADO")
elif media>4:
    print(F"por conta da média o aluno está em recuperaçao")
else:
    print(F"O(a)estudante{nome} será: REPROVADO")