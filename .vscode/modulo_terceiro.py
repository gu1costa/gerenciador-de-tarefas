#módulos de terceiros são módulos diferentes dos módulos padrões do python, criados por outras pessoas.

#módulo utilizado: requests //// comando: pip install requests==2.31.0

print("\nImportação e uso de um módulo de terceiros:")
import requests

url = "https://www.example.com"  #recebe o conteúdo do site desta url

#requisição get do módulo request:
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")   #se retornar 200, então funcionou.

#o site w3school contém exemplos de uso de bibliotecas.
#o site pypi.org possui pacotes de terceiros.