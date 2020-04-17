# Servidor para Disciplina Desafios de Software
Este projeto faz parte da materia [Desenvolvimento Aberto](https://insper.github.io/dev-aberto/).
O objetivo era pegar um projeto feito por terceiros e nao documentado e melhora-lo nos seguintes aspectos:

- melhorar o padronizacao do codigo
- criar uma documentacao oficial com github pages
- fazer testes unitarios

#### Github Pages:

Disponivel em https://sabrinasimao.github.io/softdes-desafios/

## Execução de testes

### Testes de interface

Os testes de interface são realizados pela biblioteca `Selenium`, que deve ser instalada utilizando o seguinte comando:

```
$ pip install selenium
```

Após a instalação, é preciso verificar se os drivers dos navegadores a serem testados são validos para seu sistema operacional e navegador. Os drivers encontrados no diretório `/test/drivers` são válidos para Linux e compreendem a versão 81 do *Google Chrome* ou superior e versão 70 do *Firefox* ou superior. 

Para executar os testes no *Chrome*, basta executar o comando:

```
$ python3 test_interface.py chrome
```

Para executar os testes no *Firefox*, basta executar o comando:

```
$ python3 teste_interface.py firefox
```

Os testes são rodados com base nos arquivos de nome `desafio1.py` e `desafio2.py` encontrados no diretório `/testes`.

### Testes de unidade

Para realizar testes relacionados a função `lambda_handler` do arquivo central do servidor (`softdes.py`), será utilizada a biblioteca `pytest`. Para isto, é necessário instala-la com o comando:

```
$ pip install pytest
```

A execução dos testes é feita através do comando:

```
$ pytest teste_lambda.py
```

