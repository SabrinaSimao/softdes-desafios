## Estrutura do código em alto nível

O código do servidor é feito em `Python 3.6` com o auxílio da biblioteca `Flask` para subí-lo. O gerenciamento dos dados de usuário, como login, senha e registros de submissão de arquivos são armazenados em `SQL` e as senhas são criptografadas com o uso da biblioteca `hashlib`. 

O arquivo principal para a execução do servidor é o `softdes.py`, com o qual é possível subir o servidor em Flask utilizando alguns arquivos em `HTML` para a interface do usuário.

## Configurando ambiente

Primeiro, é preciso configurar o ambiente instalando as dependências do servidor. Para isto, rode o seguinte comando no terminal:

```
$ pip3 install flask flask_httpauth db-sqlite3 hashlib
```

## Instalação do software

Antes de inicializar o servidor de desafios, primeiro é preciso configurar a data limite de submissão de arquivos pelos alunos. Para isto, abra o arquivo `quiz.sql` com o editor de texto de sua preferência e altere a data `2018-12-31 23:59:59` para alguma que o convenha. 

Em seguida, crie um arquivo nomeado `users.csv` e insira quantos usuários preferir, seguindo o modelo `USER,PASSWORD`.

Agora é necessário popular um banco de dados com as informações de login presentes no arquivo `users.csv`. Para isto, é necessário executar o comando:

```
$ sqlite3 quiz.db
```
então, na interface do sqlite3, execute o comando:

```
$ .read quiz.sql
```

e para efetivamente adicionar os usuários no banco de dados, execute o comando: 

```
$ python3 adduser.py
```

Por fim, é necessário subir o servidor, executando o comando:

```
$ FLASK_APP=softdes.py flask run --port="PORTA"
```
onde o campo `"PORTA"` deve ser substituido com a porta de sua escolha. Com o servidor online, agora só é necessário entrar com um usuário e sua senha correspondente no site.

