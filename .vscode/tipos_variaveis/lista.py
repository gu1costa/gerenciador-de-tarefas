#Declaração da lista

minha_lista = [1, 2, 3, 4, 5, "Guilherme", True, False] 

#exibindo a lista
print("Minha lista de exemplo:", minha_lista)

#exibindo elementos individuais da lista
print("minha lista[6]:", minha_lista[5]) #índice dentro dos colchetes
print("minha lista[1]:", minha_lista[0]) #índice dentro dos colchetes
print("minha lista[1 ao 6]:", minha_lista[1:7]) #apresentando vários elemntos da lista.
print(minha_lista[:6]) #do começo até um alvo específico.
print(minha_lista[2:]) #de um início específico até o final.

#substituição/adição do conteúdo da lista
minha_lista[0] = "Python"
minha_lista.append(6) #método que adiciona um elemento ao final de uma lista.
print("Após o método append:", minha_lista)

#método index
indice = minha_lista.index(2)
print("Indice do elemento 2:", indice)

#método insert: insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert: ", minha_lista)

#método pop: remove e retorna um elemento de um índice específico
elemento_removido = minha_lista.pop(3)
print("Elemento removido: ", minha_lista)

#método remove: remove o primeiro elemento com valor especificado.
minha_lista.remove(True)
print("Após o remove: ", minha_lista)

#método sort: organiza a lista em ordem crescente
print("Após o sort: ", minha_lista.sort()) #os elementos da lista tem que estar do mesmo tipo.