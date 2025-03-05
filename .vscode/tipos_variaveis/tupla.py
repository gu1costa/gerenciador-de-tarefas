#ordenada e IMUTÁVEL!!!!!.

#criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla: ", minha_tupla)

#acessando os elementos da tupla:
print("Minha tupla:", minha_tupla[0])
print("Minha tupla:", minha_tupla[2])
print("Minha tupla:", minha_tupla[-1]) #último elemento da tupla.

#método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o 2 aparece na tupla: ", contagem)

#index
indice = minha_tupla.index(3)
print("Índice da primeira ocorrência do elemento 3:", indice)