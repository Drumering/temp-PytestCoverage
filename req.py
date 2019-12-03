import requests

response = requests.post('https://www.4devs.com.br/ferramentas_online.php', data={'acao':'gerar_pessoa','sexo':'I','pontuacao':'S','idade':'0','cep_estado':'','txt_qtde':'7','cep_cidade':''})
response_json = response.json()
for pessoa in range(len(response_json)):
    print(response_json[pessoa]['nome'], '-> Idade:',response_json[pessoa]['idade'], 'Portador do CPF:', response_json[pessoa]['cpf'])