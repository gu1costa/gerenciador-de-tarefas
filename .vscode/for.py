#loop é uma estrutura que permite repetir o bloco de código enquanto uma condição for verdadeira.

#for
lista = [1, 2, 3, 4, 5]

print("for utilizando lista:")
for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)

print("\nfor utilizando tupla:")
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Guilherme",
          "idade": 19,
          "cidade": "Fortaleza"}

print("\nFor utilizando dicionário-chaves:")
for chave in pessoa.keys():
    print(chave)

print("\nfor utilizando chave-valores:")
for valor in pessoa.values():
    print(valor)

print("\nfor utilizando dicionario-valores:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#for com range()
#range() retorna um intervalo numérico em formato de lista

print(list(range(0, 10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nUtilizando a função range:")
for numero in range(5): #do 0 ao 4
    print("Número:",numero)

print("\nUtilizando a função range() com len()")

lista = [1, 2, 3, 4, 5]

for indice in range(0, len(lista)): #do índice 0 ao 4
    print("Índice:", indice)
    print("Elemento:", lista[indice])
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]

for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")

    if indice == 1:
        print("Índice 1.")