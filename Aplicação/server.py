import socket
from threading import Thread
from dataBase.dataBase import setPost, returnPosts, resetBase

#Definição dos Dados Fixos da Aplicação
NameServer = 'Servidor Mural'
ADDR = 'localhost'
PORT = 8000

#Função que inicia o Servidor
def startServer():
    print('Servidor ', NameServer,' está Online!')
    #Criação do socket Servidor e atribuição de um endereço IP e Número de Porta e configuração para aceitar conexões
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.bind((ADDR, PORT))
    socketServer.listen(10)

    #Processo que aplica Thread e processamento de solicitações dos clientes
    while True:
            socketClient, clienteAddr = socketServer.accept()
            Thread(target=process(socketClient, clienteAddr), args=(socketClient, clienteAddr)).start()
   
#Função que realiza o processamento do Servidor
def process(socketClient, clienteAddr):
    #Processamento da Mensagem e tratamento dos Métodos POST, GET, DELETE solicitados pelo cliente
    dataReceived = socketClient.recv(1024)
    dataReceived = dataReceived.decode()
    message = dataReceived.split('\r\n')[-1]
    if dataReceived.startswith("POST"):
        print('\nProcessamento Método POST')
        data = message.split('\r\n')[-1]
        setPost(data)
        print('Processamento Método POST Concluido com Sucesso!\n')
        socketClient.sendall(f'Post adicionado com Sucesso!'.encode('utf-8'))
    if dataReceived.startswith("GET"):
        print('\nProcessamento Método GET')
        respondeHead = f'HTTP/1.1 200 OK\r\n\r\n'
        file = returnPosts()
        response = respondeHead + file.read()
        print('Processamento Método GET Concluido com Sucesso!\n')
        socketClient.sendall(response.encode('utf-8'))
    if dataReceived.startswith("DELETE"):
        print('\nProcessamento Método DELETE')
        resetBase()
        print('Processamento Método DELETE Concluido com Sucesso!\n')
        socketClient.sendall(f'Mural deletado com Sucesso!'.encode('utf-8'))
    socketClient.close()


#Inicialização do Servidor
startServer()
