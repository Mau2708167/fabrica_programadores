nome=input("digite seu nome")
peso=float(input(f"{nome},agora me diga seu peso em Kgs"))
altura=float(input("nos diga sua altura em metros"))
imc=peso/(altura**2)
if imc<=18.5:
    print(F"{nome}você se encontra em estado de: magreza")
elif imc<=24.9:
    print(F"{nome}você se encontra em estado de: normalidade")
elif imc<29.9:
    print(F"{nome}você se encontra em estadop de: sobrepeso")
elif imc<=39.9:
    print(F"{nome}você se encontra em estado de: obesidade")
else:
    print(F"{nome}você se encontra em estado de: obesidade grave")
