#função é um bloco de código reutilizável que executa uma tarefa específica quando é chamado.

#exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudação:")
saudacao("Guilherme")
saudacao("Nicolas")

#função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função [5]:", resultado_quadrado)

#função com múltiplos parâmetros
def soma(numero1, numero2):
    resultado_soma = numero1 + numero2
    return resultado_soma

print("\nResultado da função soma[20][50]:")
print(soma(20, 50))