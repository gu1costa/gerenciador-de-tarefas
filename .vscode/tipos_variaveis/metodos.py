nome = "Guilherme"
sobrenome = "Ferreira"
nome_completo = "Guilherme Ferreira da Costa Neto"

#método upper
nome.upper() #o método transforma o conteúdo em maiúsculo.

#nome.lower
nome.lower() #o método transforma o conteúdo em minúsculo.

nome[0] #acessa um caractere do conteúdo da variável.

nome_completo.count("o") #conta quantos caracteres especificados estão presentes no conteúdo da variável

nome_completo.find("g") #identifica a primeira ocorrência de um caractere na string.

nome.encode() #transforma o conteúdo em bytes.

nome.encode().decode() #decodifica o conteúdo codificado anteriormente.

nome_completo.replace("g", "b") #utilizado para substituir um caractere por outro.

nome_completo.replace("g", "b").replace("h", "x").replace("u","v") #substituição mais de uma vez.

"-".join(nome) #separa a string de acordo com o caractere que é declarado no início.

nome_completo.split("G") #Esse método converte uma string em um array. Podemos dizer que ele como que “corta” uma string em vários “pedaços”, que são as posições do array que será retornado.

nome_errado = "xGuilhermex"
nome_errado.strip("x") #retira caracteres errados no início e/ou no final.
nome_errado.rstrip("x") #retira o caractere a direita do conteúdo.

nome.startswith("Gui") #verifica se o conteúdo da string começa com os caracteres especificados. retorna true ou falso.

"lhe" in nome #verifica se os caracteres especificados estão no conteúdo da string. retorna true ou falso.

"abc" not in nome #verifica se os caracteres especificados não estão no conteúdo da string. retorna true ou falso.

