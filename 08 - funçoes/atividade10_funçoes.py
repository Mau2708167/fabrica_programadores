# Projeto: Desvio Condicional

# Definição de variáveis
temperatura =float(input("Me fale, como está a temperatura?"))
def status(temperatura):
    if temperatura < 20:
        print(' A temperatura está muito fria')
    else:
        print(' A temperatura está muito quente')

 #chamada de funçao
status(temperatura)