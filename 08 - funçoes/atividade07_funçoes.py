# Autor: Mauricio Melo
# projeto: IMC com input e f - string

#declaraçao com variaveis
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

def calcular(peso,altura):
    imc = peso / (altura * altura)
    print(f'seu imc é: {imc:.2f}')

calcular(peso,altura)


