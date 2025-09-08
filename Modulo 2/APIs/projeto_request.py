import requests
def ping():
    response = requests.get('https://restful-booker.herokuapp.com/ping')

    return response.status_code 

def autenticaçao():
    corpo = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post('https://restful-booker.herokuapp.com/auth', json=corpo)
    return response.json()["token"]    

def criar_booking(nome,sobrenome,preco = 0, pago=False,
                  checkin = "2025-08-20", checkout="2025-08-25",
                  adicionais="Café da manhã"):
    corpo = {
            "firstname" : nome,
            "lastname" : sobrenome,
            "totalprice" : preco,
            "depositpaid" : pago,
            "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
            },
            "additionalneeds" : adicionais
            }
    resposta = requests.post("https://restful-booker.herokuapp.com/booking", json=corpo)
    return resposta.json()


def buscar_booking(id_booking):
    resposta = requests.get(f"https://restful-booker.herokuapp.com/booking/{id_booking}")
    print(resposta.json())
    
def atualiza_todo_booking(id_booking, nome,sobrenome,preco, pago,
                  checkin, checkout,adicionais):
    
    cabecalho = {"Cookie":f"token={autenticaçao()}"}
   
    corpo = {
            "firstname" : nome,
            "lastname" : sobrenome,
            "totalprice" : preco,
            "depositpaid" : pago,
            "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
            },
            "additionalneeds" : adicionais
            }
    
    resposta = requests.put(f"https://restful-booker.herokuapp.com/booking/{id_booking}", json=corpo, headers=cabecalho)
    print(resposta.status_code)
    print(resposta.json())

def atualiza_parcial_booking(id_booking, **kwargs):
    cabecalho = {"Cookie":f"token={autenticaçao()}"}
    corpo = kwargs


    resposta = requests.patch(f"https://restful-booker.herokuapp.com/booking/{id_booking}", json=corpo, headers=cabecalho)
    print(resposta.status_code)
    print(resposta.json())

def excluir(id_booking):
    cabecalho = {"Cookie":f"token={autenticaçao()}"}
    resposta = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id_booking}", headers=cabecalho) 
    print(resposta.status_code)

##### ÁREA DE TESTES ########
# print(ping())
# print(autenticacao())
#print(buscar_booking(2))
#atualiza_todo_booking(3, "diovanny", "almeida",1500,True,"2025/08/25","2025/08/30","Café da manhã")
# print(excluir(16))
print("-"*35)
print("ATIVIDADE 1 - HEALTH CHECK (PING)")
print(ping())
print("-"*35)

print("-"*35)
print("ATIVIDADE 2 - AUTENTICAÇÃO")
print(autenticaçao())
print("-"*35)

print("-"*35)
print("ATIVIDADE 3 - CRIAR UMA RESERVA")
resposta = criar_booking(nome="diovanny", sobrenome="ricardo")
print(resposta)
bookingId = resposta["bookingid"]
print("-"*35)

print("-"*35)
print("ATIVIDADE 4 -BUSCAR RESERVA POR ID")
print(buscar_booking(2))
print("-"*35)

print("-"*35)
print("ATIVADADE 5 - ATUALIZAR TOTALMENTE")
atualiza_todo_booking(bookingId, "diovanny", "almeida",1500,True,"2025/08/25","2025/08/30","Café da manhã")
print("-"*35)


print("-"*35)
print("ATIVIDADE 6 - ATUALIZAR PARCIALMENTE")
print(atualiza_parcial_booking(bookingId,firstname="Péricles",totalprice=50000))
print("-"*35)

print("-"*35)
print("ATIVIDADE 7 - DELETAR RESERVA")
print(excluir(bookingId))
