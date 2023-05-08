import socket
from datetime import datetime as date
import json

#Definição dos Dados Fixos da Aplicação
ADDR = '127.0.0.1'
PORT = 8000

#Função que inicia o Cliente
def startClient():
    control = True
    print('███╗   ███╗██╗   ██╗██████╗  █████╗ ██╗          ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗\n████╗ ████║██║   ██║██╔══██╗██╔══██╗██║         ██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝\n██╔████╔██║██║   ██║██████╔╝███████║██║         ██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗  \n██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║         ██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝  \n██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║███████╗    ╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗\n╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝\n')
    while control:
        option = int(input('Digite a opção desejada:\n1 - Postar no Mural\n2 - Visualizar Mural\n3 - Deletar Mural\n4 - Fechar aplicação\n'))
        if option == 1:
            #Objetivo utilizar Mensagem HTTP - POST
            newPost()
        elif option == 2:
            #Objetivo utilizar Mensagem HTTP - GET
            getPost()
        elif option == 3:
            #Objetivo utilizar Mensagem HTTP - DELETE
            deleteWall()
        elif option == 4:
            control = False
        else:
            print('Tente novamente!')

#Conjunto de Funções Method POST
##Função geral que realiza a inicialização do método
def newPost():
    title = input('Digite o título do Post:\n')
    description = input('Digite a descrição do Post:\n')
    author = input('Digite o nome do Autor do Post:\n')
    time =  date.now().strftime('%d/%m/%Y %Hh %Mmin')
    obj = constructor(title, description, author, time)
    methodPOST(obj)

##Função que cria o Objeto a ser enviado pelo método
def constructor(title, description,author, time):
    Obj = {
        'title':title,
        'description':description,
        'author':author,
        'time':time
    }
    return Obj

##Função que aplica os conceitos do método POST
def methodPOST(data):
    #Criação do socket Cliente e atribuição da conexão com endereço IP e Número de Porta
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((ADDR,PORT))

    #Modificação do dado a ser enviado
    postDataEncode = json.dumps(data).encode('utf-8')

    #Construção do cabeçalho da mensagem POST
    headers = [
        f"POST / HTTP/1.1",
        f"Host: {ADDR}",
        f"Content-Type: application/json",
        f"Content-Length: {len(postDataEncode)}",
        f"Connection: close",
        "",
    ]
    headerEnconde = "\r\n".join(headers).encode('utf-8')

    #Processamento do envio da mensagem POST e resposta do Servidor
    socketClient.sendall(headerEnconde + postDataEncode)
    resposta = socketClient.recv(1024)
    print('\n',resposta.decode(),'\n')
    socketClient.close()
    return


#Conjunto  de Funções Method GET
##Função geral que realiza a inicialização do método
def getPost():
    print('\n\nMURAL DE POSTS:\n\n')
    message = methodGET()
    message = message.split('\r\n\r\n')[-1]
    message = message[1:len(message)-1]
    displayPosts(message)
    if len(message) == 0:
        print('Sem posts no momento!\nTente novamente mais tarde ou faça um você mesmo :)\n')
    print()
    return

##Função auxiliar que trata a mensagem recebida do método
def displayPosts(messages):
    #Tratamento dos dados
    messages = messages.split('}')
    listMessages = []
    for message in messages:
        types = message.split(',')
        listAux = []
        for type in types:
            type = type.split(':')[-1]
            type = type[2:len(type)-1]
            listAux.append(type)
        if len(listAux) == 4:
            listMessages.append(listAux)
        elif len(listAux) == 5:
            listAux.remove(listAux[0])
            listMessages.append(listAux)
    #plotagem do Mural
    for m in listMessages:
        print('   Título do Post: ', m[0])
        print('Descrição do Post: ', m[1])
        print('    Autor do Post: ', m[2])
        print('  Período do Post: ', m[3])
        print()
    return

##Função que aplica os conceitos do método GET
def methodGET():
    #Criação do socket Cliente e atribuição da conexão com endereço IP e Número de Porta
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((ADDR,PORT))

    #Construção do cabeçalho da mensagem GET
    headers = [
        f"GET / HTTP/1.1",
        f"Host: {ADDR}",
        f"Connection: close",
        "",
    ]
    headerEnconde = "\r\n".join(headers).encode('utf-8')

    #Processamento do envio da mensagem GET e resposta do Servidor
    socketClient.sendall(headerEnconde)
    resposta = socketClient.recv(1024)
    r = resposta.decode()
    socketClient.close()
    return r


#Conjunto  de Funções Method DELETE
##Função geral que realiza a inicialização do método
def deleteWall():
    password = input('Digite a senha ADM:\n')
    if(password == '1234'):
        methodDelete()
    else:
        print('Senha Incorreta!')
        return

##Função que aplica os conceitos do método DELETE
def methodDelete():
    #Criação do socket Cliente e atribuição da conexão com endereço IP e Número de Porta
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((ADDR,PORT))

    #Construção do cabeçalho da mensagem DELETE
    headers = [
        f"DELETE / HTTP/1.1",
        f"Host: {ADDR}",
        f"Connection: close",
        "",
    ]
    headerEnconde = "\r\n".join(headers).encode('utf-8')

    #Processamento do envio da mensagem DELETE e resposta do Servidor
    socketClient.sendall(headerEnconde)
    resposta = socketClient.recv(1024)
    print('\n',resposta.decode(),'\n')
    socketClient.close()
    return


#Inicialização do Cliente
startClient()