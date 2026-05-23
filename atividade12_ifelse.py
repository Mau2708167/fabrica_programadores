nome=input(" informe seu nome:")
telefone=int(input("telefone"))
cidade=input("em qual cidade você reside:")
salario=float(input("de quanto é o seu salario:"))
if salario>1000:
    print(f"{nome},você possui uma boa renda mensal BOA")
elif salario>700:
    print(f"{nome}, você possui uma renda RAZOAVEL")
elif salario > 500:
    print(f"{nome}você possui uma renda mensal BAIXA")
else:
    print(f"{nome}você possui uma renda mensal MUITO BAIXA")
