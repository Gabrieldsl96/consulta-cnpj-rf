import requests
import json  # Importa o módulo para formatação de JSON

url = "https://publica.cnpj.ws/cnpj/00000000000000" #Aqui é onde voce coloca o CNPJ

resp = requests.get(url)

# Converte o conteúdo da resposta em JSON
data = resp.json()

# Formata e printa o JSON "bonitinho" (com indentação)
print(json.dumps(data, indent=4, ensure_ascii=False))
