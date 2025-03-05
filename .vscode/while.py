#while é o tipo de loop que executa um bloco de código enquanto uma determinada condição for verdadeira.

print("Exemplo de while: ")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1 #contador = contador + 1

print("Programa finalizado.")

while contador <= 4:
    print(contador)
    contador += 1
    if contador == 5:
        break #força o programa a sair do loop.

print("Programa finalizado.")