# import requests

# print("ativando o assistente")

# def perguntar(questao):
#     url = "http://localhost:11434/api/chat"
#     data = {
#         "model":"gemma3",
#         "messages":[
#             {"role":"user","content":questao}
#         ],
#         "stream":False
#     }

#     return requests.post(url,json=data) # da primeira abordagem

# while True:
#     pergunta = input("Voce: ")
#     if pergunta.lower() == "sair":
#         break
    
#     resposta = perguntar(pergunta)

#     print(resposta.json()['model'] + ":",resposta.json()['message']['content'])

# print("Desligando")

#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
from ollama import Client

client = Client(host='http://localhost:11434')
model = "gemma3"

print("ativando o assistente")

def perguntar(questao):
    stream = client.chat(
        model=model,
        stream=True,
        messages=[
            {'role':'user','content':questao}
        ]
    )
    return stream

# while True:
#     perguntando = input("Voce: ")
#     if perguntando.lower() == "sair":
#         break
#     resposta = perguntar(perguntando)
#     print(model + ": ",end="")

stream = client.chat(
        model=model,
        stream=True,
        messages=[
            {'role':'user','content':"Como voce esta?"}
        ]
    )
for chunk in stream:
    print(chunk['message']['content'],end='',flush=True)