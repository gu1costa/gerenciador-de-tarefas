#condicionais permitem tomar decisões com condições específicas, que executam um bloco de código que estão contidas dentro dela.

#if
idade = 19
if idade >= 18:
    print("Maior de idade.")

#else
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#elif
idade = int(input("Quantos anos você tem?")) #ou idade = int(idade)
if idade >= 18:
    print("Maior de idade.")
elif idade >= 12 and idade < 18:
    print("Adolescente")
else: 
    print("Menor de idade.")