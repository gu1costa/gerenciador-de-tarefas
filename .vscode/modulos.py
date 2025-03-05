#módulos são arquivos que contém definições e instruções que podem ser reutilizados em outros programas/arquivos.

#existem módulos que já vem com python(Módulos padrão) e existem módulos de terceiros.

#importação do módulo inteiro:
print("Exemplo de importação de módulo padrão:")
import math

raiz_quadrada = math.sqrt(25)
print(f"Raíz quadrada de 25: {raiz_quadrada}")   

#importação de definições específicas do módulo:
import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"Raíz quadrada de 25: {raiz_quadrada}")   

#criação do próprio módulo
print("\nExemplo de criação  utilização de um módulo personalizado:")
import meu_modulo

mensagem = meu_modulo.saudacao("Guilherme")
resultado_dobro = meu_modulo.dobro(5)
print(saudacao)
print(f"O dobro de 5 é: {resultado_dobro}")

#utilizando funções específicas do módulo
from meu_modulo import saudacao, dobro

mensagem = meu_modulo.saudacao("Guilherme")
resultado_dobro = meu_modulo.dobro(5)
print(saudacao)
print(f"O dobro de 5 é: {resultado_dobro}")