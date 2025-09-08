import requests 

# response = requests.get('http://jsonplaceholder.typicode.com/posts')

# print(response.status_code)
# print(response.text)

# response = requests.get('http://jsonplaceholder.typicode.com/posts', params={'userid': 1 })

# print(response.json())

dados = {
    'titulo' : 'meu post',
    'conteudo': 'Este é o conteudo do meu post',
    'usuarioid' : 1

}

response = requests.post('http://jsonplaceholder.typicode.com/posts',json=dados)

print(response.status_code)
# print(response.json())