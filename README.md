# PCS3643- Laboratório de Engenharia de Software I (2022)

## Grupo 11

## Integrantes

-   Sergio Magalhães Contente NUSP: 10792087
-   Luis del Llano NUSP: 6718450

## :tada: Overview

O projeto tem sua descrição técnica no seguinte diretório:

[Casos de uso](<utils/Aula%202%20-%20Especificação%20Caso%20de%20Uso.docx%20(4).pdf>)

Nele poderá entender-se o resumo dos Casos de Uso do projeto.

## :open_file_folder: Estrutura de Arquivos

-   **MyProject/**
    -   **MyProject/** - Pasta que contém os arquivos do projeto principal
    -   **template/** - Pasta que contém os arquivos para template (HTML e CSS)

## Guia de instalação

Para instalar as dependências necessárias para rodar o projeto é necessário seguir o seguinte passo-a-passo em um ambitente Windows:

1.  :snake: Instale Python 3.X no seu computador seguindo o seguinte [link](https://www.python.org/downloads/).
2.  :cd: Clone o repositório onde preferir, como exemplo, na pasta webapp. Para tal, faça o seguinte comando:

    ```
    $ git clone https://github.com/sergio-contente/PCS3643.git
    E vá para o diretório do projeto:

        		$ cd PCS3643/MyProj

    ```

3.  :earth_americas: Crie um ambiente virtual utilizando o comando, onde **env** pode ser qualquer nome de ambiente:

        	$ python -m venv env

4.  :heavy_check_mark: Ative o ambiente virtual utilizando o comando:

        $ .\env\scripts\Activate.ps1

5.  :fire: Instale o Django dentro deste ambiente virtual recém-criado:

        $ pip install django

## Como executar

Para conseguir executar o projeto de maneira satisfatória é necessário realizar as seguintes operações dentro da pasta MyProject/:

```
	python manage.py  migrate
	python manage.py runserver
```

Então, para averiguar que ocorreu conforme o esperado, o terminal irá informar: "Starting development server at http://127.0.0.1:8000/".Abra no navegador o seguinte servidor: "http://127.0.0.1:8000/FIRST/".

## Diagramas

Os diagramas referentes a documentação do projeto encontra-se na pasta PCS3643/utils

## Testando

Para realizar testes, repita os seguintes passos:

1. Na pasta "MyProj", faça:
```
python manage.py makemigrations
```

1. Crie então um banco de dados:
```
python menage.py migrate
```

1. Os testes estão definidos em `FlightApp\test.py`. Execute-os:
```
python manage.py test
```
## Login Teste

Para realizar o login, utilize as seguintes credenciais:
```
Username: admin
Password: admin
```
