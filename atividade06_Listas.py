# Autor:Mauricio Melo Araujo
#Projeto:listas em python

#           0         1           2      3       4       5
nomes = ['Fernando','Mauricio','Fabio','Juan']#neymar  #pedro

print(*nomes)


#adicionando nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append('pedro')
print(*nomes)

#adicionando um nome em uma posiçao especifica
nomes.insert(4,'Neymar')
print(*nomes)

#modificar uma pessoa da lista
nomes[5] = 'Mbappe'
print(*nomes)

#removendo o nome da lista
del nomes [2]
print(*nomes)

# removendo um nome por texto
#buscar um nome e apagar o primeiro que aparecer
nomes.remove('Fernando')
print(*nomes)

#usando o popn para mostrar o nome removido
#   0         1       2        3
# Mauricio   juan   Neymar    Mbappe
removido= nomes.pop(1)
print(f'após o pop foi removido o nome: {removido}', nomes)

#limpar a lista
nomes.clear()
print(f'após o clear a lista é:{nomes}')