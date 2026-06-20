#Autor: Mauricio Melo
#Projeto: entrada pelo usuario

valor1 = float(input('digite o primeiro valor: '))
valor2 = float(input('digite o segundo valor: '))

#Funçao calcular
def calcular (valor1,valor2):
    somar = valor1 + valor2
    subtrair = valor1 - valor2
    multiplicar = valor1 * valor2
    dividir = valor1 / valor2

# imprimindo os resultados
    print(f' o resultado da soma é:{ somar}')
    print(f' o resultado da subtraçao  é:{ subtrair}')
    print(f' o resultado da multipliacaçao   é:{ multiplicar}')
    print(f' o resultado da divisão  é:{ dividir}')

#chamada da funçao
calcular(valor1,valor2)









