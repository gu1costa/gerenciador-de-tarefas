#declaração
nome_completo = "Guilherme Ferreira da Costa Neto" #string

nome_completo_aspas = """Guilherme
Ferreira""" #as 3 aspas duplas permite pular linha.

nome_completo_quebra = "Guilherme \
Ferreira"

nome = "Guilherme"
sobrenome = "Ferreira"

#Formatação
print("Nome completo(1º forma):", nome_completo) #contém espaço na concatenação.
print("Nome completo(2º forma):" + nome_completo) #espaço não existe.
print("Nome completo(3º forma):" + "Guilherme Ferreira" + "da Costa Neto") #tudo junto sem espaço
print("Nome completo (4º forma):", "Guilherme", "Costa") #espaçamento presente
print("Nome completo(5º forma):", nome_completo_aspas)
print("Nome completo(6º forma):", nome_completo_quebra)
print("Nome completo(7º forma): %s" % nome_completo) #resultado igual a primeira forma
print("Nome completo(8º forma): %s %s" % (nome, sobrenome)) #neste tipo, a formatação converte os tipos das variáveis para serem usadas.
print(f"Nome completo(9º forma):{nome} {sobrenome}") #print format
print("Nome completo(10º forma): {} {}".format(nome, sobrenome)) #print format
print("Nome completo(11º forma): {} {}".format(sobrenome, nome)) #print format