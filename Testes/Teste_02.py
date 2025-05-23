!pip install requests

import requests

def testar_agify_para_nomes(nomes):
    resultados = {}
    for nome in nomes:
        url = f"https://api.agify.io?name={nome}"
        resp = requests.get(url)
        if resp.status_code != 200:
            resultados[nome] = f"Erro: status {resp.status_code}"
            continue
        
        dados = resp.json()
        # Validar se o nome retornado bate com o enviado (case insensitive)
        if dados.get('name', '').lower() == nome.lower():
            resultados[nome] = "Sucesso"
        else:
            resultados[nome] = "Nome incorreto no retorno"
    return resultados

# Testando vários nomes
nomes_teste = ["ana", "bruno", "carla", "diego"]
resultados = testar_agify_para_nomes(nomes_teste)

for nome, resultado in resultados.items():
    print(f"Teste para {nome}: {resultado}")

# Validando resultados (assert simples)
assert all(r == "Sucesso" for r in resultados.values()), "Algum teste falhou!"
print("✅ Todos os testes passaram!")

