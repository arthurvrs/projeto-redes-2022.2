# Mural Online - Projeto de Redes de Computadores

Nosso mural online visa facilitar o compartilhamento de avisos e mensagens de maneira prática e ágil. Nele, é possível postar avisos, exibir todos os aviso já postados e excluir todo o mural (apenas quem possuir a senha de administrador).

## Como utilizar?

> ### Para executar o programa:

- Certifique-se de ter feito o download dos arquivos corretamente.
- Dentro do diretório Aplicação, estarão presentes: `/dataBase`, `client.py`, `server.py`
- Para um correto funcionamento do programa, o diretório `/dataBase` e o arquivo `server.py` devem estar sempre dentro de um mesmo diretório.
- Já o `client.py` pode estar tanto no mesmo diretório que os outros arquivos quanto fora dele.
- Após checar se os passos anteriores estão todos feitos, pode **executar** o `server.py` (para acompanhar o andamento do servidor durante a utilização da aplicação) e o `client.py` (pode ser aberto mais de uma vez, pois a aplicação suporta múltiplos clientes simultâneos).

> ### Funcionalidades

![Tela inicial](https://i.ibb.co/x2v7y3n/mural-online.png)

- **Postar no Mural**

	Para criar um post, digite a opção `1` no prompt. 
	Ao fazer isso, a sequência de entradas será `Título do Post`, `Descrição do Post` e `Autor do Post`.
	> **Dica:** para evitar bugs no texto, é melhor evitar a utilização de acentos.

![Postando](https://i.ibb.co/HtMLJ5Z/criando-post.png)

- **Visualizar Mural**

	Para mostrar todos os posts já feitos, digite a opção `2` no prompt. 
	Ao fazer isso, todos os posts junto com suas informações serão disponibilizados na tela.

![Exibindo](https://i.ibb.co/4p5xSgS/mostrar-posts.png)

- **Deletar Mural**

	Para deletar todos os posts presentes no mural, digite a opção `3` no prompt. 
	Ao fazer isso, a senha de administrador será solicitada (atualmente **1234** para fins acadêmicos) e, após ser inserida, todo o mural será deletado.

![Deletando](https://i.ibb.co/5szLC3s/deletando-mural.png)
	
E então, o Mural exibirá a seguinte mensagem:

![Sem Posts](https://i.ibb.co/310jk0C/sem-posts.png)

- **Saindo do Mural**

	Para sair do aplicativo, digite a opção `4` no prompt. 
	Ao fazer isso, o programa será finalizado. Porém, o servidor continuará rodando caso algum outro cliente queira utilizar o Mural.

> ### Servidor

- Enquanto o servidor estiver ligado, ele exibirá todas as requisições feitas pelos clientes.
- Os métodos `GET`, `POST` e `DELETE` serão sempre mostrados enquanto os clientes estiverem ativos.

![Servidor executando](https://i.ibb.co/m6YnJw3/Captura-de-Tela-10.png)
- Para desligar o servidor, basta fechar a aba do mesmo.
