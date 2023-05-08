import json

#Definição dos Dados Fixos da Aplicação
PATH = "dataBase\\dataPosts.json"

#Função que adiciona o Post ao Banco de Dados
def setPost(data):
    with open(PATH) as file:
        listFile = json.load(file)
    listFile.append(editJson(data))
    with open(PATH,"w") as file:
        json.dump(listFile, file)

#Função que modifica o dado para o formato JSON correto
def editJson(data):
    Lista = []
    size = len(data)
    data = data[1:size-1]
    data = data.split(',')
    for dt in data:
        dt = dt.split(':')[-1]
        s = len(dt)
        dt = dt[2:s-1]
        Lista.append(dt)
    Obj = {
        'title' : Lista[0],
        'description' : Lista[1],
        'author' : Lista[2],
        'time' : Lista[3]
    }
    return Obj

#Função que retorna o Banco de Dados
def returnPosts():
    return open('dataBase\\dataPosts.json','r', encoding='utf-8')

#Função que reseta o Banco de Dados
def resetBase():
    listFile = []
    with open(PATH,"w") as file:
        json.dump(listFile, file)
