# Guia dos Professores

## Adicionando novos usuários

Para adicionar novos usuários no servidor, é preciso abrir o documento `users.csv` e então é preciso inserir quantos usuários desejar, seguindo o modelo "`USER,PASSWORD`".

Agora é necessário atualizar o banco de dados com as informações de login presentes no arquivo `users.csv`. Para isto, é necessário executar o comando:

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

## Adicionando novos desafios no servidor

Para adicionar um novo desafio, primeiro é preciso abrir o arquivo de base de dados `quiz.db` com a interface do `sqlite3`. Para fazer isto, é necessário rodar a seguinte linha de código no terminal:

```
sqlite3 quiz.db
```
A partir deste ponto, dentro da interface, é necessário rodar o seguinte comando, fazendo as devidas substituições:

```
Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values ('DESID', 'INICIO', 'FIM', 'DESC','TESTES', 'RES', 'DIAG');
```

Onde:
* `'DESID'` correspooriginalmentende ao número do desafio ao qual ele será identificado (Desafio 1, 2, 3, etc.);
*  `'INICIO'` e `FIM` correspondem, respectivamente, à data de inicio do desafio e a data limite de submissão do mesmo (formatação `'AAAA-MM-DD HH:MM:SS'`);
* `'DESC'` corresponde à descrição do desafio;
* `'TESTES'` correspondem à ações deixadas pelo professor para testar as submissões dos alunos;
* `'RES'` corresponde ao resultado do desafio enviado pelo aluno (valor default `'[0,0,0]'`);
* `'DIAG'` corresponde à mensagem de feedback deixada pelo professor para o desafio. 

