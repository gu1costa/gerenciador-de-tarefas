#exceções são eventos que ocorrem durante a execução do código que podem interromper o funcionamento do código

# print("Exemplo de captura de exceções : ")
# numero = input("Digite um número inteiro: ")
# resultado = 10 / numero   #não se pode dividir um número por um "texto".

#forma funcional:
# numero = int(input("Digite um número inteiro: "))
# resultado = 10 / numero   #não se pode dividir um número por um "texto".

try:
    print("Exemplo de captura de exceções: ")
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero   
except ValueError as e:
    print(f"Exceção ValueError.")
    raise ValueError("Tipo de variáveis incompatíveis.") #lança a exceção com a mensagemm escolhida.
except Exception as e:      #e = exceção (a exceção nesse caso é gérica)
    print(f"Erro: {e}")
else:                                  #executa o bloco de código
    print(f"Resultado: {resultado}")   #após ele funcionar.
finally: 
    print("Operação finalizada.")     #o finally executa o bloco
                                      #de código indepentente se
                                      #o código rodar ou não.
                                      
# com o try/excepct, o programa não é interrompido. o código continua até que o problema se resolva, executando o código diversas vezes se for preciso.

