# Autor:Mauricio Melo Araujo
#Projeto:listas em python

#           0         1           2      3       4       5
nomes = ['Fernando','Mauricio','Fabio','Juan']#neymar  #pedro

print(*nomes)


#adicionando nome na lista
# para retirar as aspas e os colchetes, use *
nomes.append('pedro')
print(*nomes)


# removendo um nome por texto
#buscar um nome e apagar o primeiro que aparecer
nomes.remove('Fernando')
print(*nomes)

