#bibliotecas requests
#serve para pegar informações
# usa-se para API
#Get
#criar informações=Post
#editar informações=Patch
#deletar informçoes=Ptach
#API publica
#atualizada mensalmente
import requests 
status=400
code=''
message=''
c=0


ceps={
  "cep": "05424020",
  "address_type": "Rua",
  "address_name": "Professor Carlos Reis",
  "address": "Rua Professor Carlos Reis",
  "district": "Pinheiros",
  "state": "SP",
  "city": "São Paulo",
  "state": "SP",
  "lat": "-23.5703026",
  "lng": "-46.6967364",
  "ddd": "11",
  "city_ibge": "3550308"
}

print(ceps)
for c in ceps:
  ceps=requests.get('https://cep.awesomeapi.com.br/json/05424020')



  

print(ceps)
print('acabou')