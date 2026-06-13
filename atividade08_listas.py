# Autor:Mauricio Melo Araujo
#Projeto:listas em python

#           0         1           2      3       4       5
nomes = ['Fernando','Mauricio','Fabio','Juan']#neymar  #pedro

print(*nomes)

nomes.append(input("digite o nome do contato a a ser adicionado:"))
print(*nomes)

nomes.remove(input("digite o nome do contato a ser removido:"))
print(*nomes)