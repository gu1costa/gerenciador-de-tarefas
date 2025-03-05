#dicionário em python é uma coleção não ordenada de pares: chave e valor.
#não possui ordem como uma lista e tupla.
#a estrutura armazenada em um dicionário pressupõe chave-valor

#criando um dicionário de exemplo
pessoa = {"nome": "Guilherme", 
          "idade": 19, 
          "cidade": "Fortaleza"}

#Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

#Adicionando elemento ao dicionário
pessoa["sobrenome"] = "Ferreira"
print("Sobrenome:", pessoa["sobrenome"])

#para atualizar um dado
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

#remover um par de chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo: ", pessoa)

#métodos
#keys() retorno de todas as chaves em formato de lista
chaves = list(pessoa.keys()) #list é um método que transforma em lista
print("Chaves do dicionário: ", chaves)
print("Primeira chave:", chaves[0]) #primeira chave da lista

#values() retorno de todos os valores do dicionário em lista
valores = list(pessoa.values())
print("Valoers do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

#items() retorna uma lista de tuplas de pares chave-valor
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0],itens[0][1])) #[0] ->nome [1]-> Guilherme
