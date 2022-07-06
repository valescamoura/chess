# Chess

Jogo de xadrez com interface web realizado como trabalho final da disciplina de Engenharia de Software II (2022/1). 

Deploy já disponível no [Heroku](https://chess-es2-20221.herokuapp.com/).

## Requisitos

1. Instale ``Python 3.x``.

## Dev setup

_Execute os comandos a partir do diretório base._

1. Crie o ambiente virtual Python através do comando: ``python -m venv venv``.

2. Ative o ambiente virtual:<br/>
    Windows: ``./venv/Scripts/activate``.<br/>
    Linux/Mac: ``source ./venv/bin/activate``.

3. Instale as dependências: ``pip install -r requirements.txt``.

4. Inicie o servidor: ``python manage.py runserver``. O serviço é acessado por padrão através da url http://127.0.0.1:8000/.

# Chess

Jogo de xadrez com interface web realizado como trabalho final da disciplina de Engenharia de Software II (2022/1). 

Deploy já disponível no [Heroku](https://chess-es2-20221.herokuapp.com/).

## Requisitos

1. Instale ``Python 3.x``.

## Dev setup

_Execute os comandos a partir do diretório base._

1. Crie o ambiente virtual Python através do comando: ``python -m venv venv``.

2. Ative o ambiente virtual:<br/>
    Windows: ``./venv/Scripts/activate``.<br/>
    Linux/Mac: ``source ./venv/bin/activate``.

3. Instale as dependências: ``pip install -r requirements.txt``.

4. Inicie o servidor: ``python manage.py runserver``. O serviço é acessado por padrão através da url http://127.0.0.1:8000/.

## Testes
Para rodar os testes ative o ambiente virtual

1. Comando para rodar todos os testes:
    ``python -m unittest discover -s tests`` 
2. Comando para rodar um teste em específico:
    ``python -m unittest tests/nomeDoArquivoDeTeste.py`` 

## Cobertura dos Testes
1. Instale o coverage.py no seu ambiente virtual: 
    ``pip install coverage``
2. Comando para rodar o testes de cobertura:
    ``coverage run -m unittest tests/test_ia.py tests/test_services.py tests/test_board.py``
3. Use para obter um relatório da cobertura em seu terminal de comando:
    ``coverage report -m``
4. Para uma apresentação melhor desse relatório, use este comando para obter esse relatório em páginas HTML:
    ``coverage html``
    
    Consulte a pasta htmlcov que foi gerada.

## Guia do desenvolvedor

1. Estamos utilizando uma lógica [Trunk-based development](https://www.atlassian.com/br/continuous-delivery/continuous-integration/trunk-based-development).

2. Commits e pushes não podem ser enviados diretamente para branch main. Cada desenvolvedor deve trabalhar em sua branch e abrir um pull request com suas adições. Cada pull request deverá ter aprovação de 1 revisor e passar pelas etapas de build, lint e testes com sucesso para que o merge com a main possa ser realizado.

3. Cada merge feito com a main, sobe automaticamente uma nova release do deploy no [Heroku](https://chess-es2-20221.herokuapp.com/). Para garantir que o deploy não "quebre", existem as verificações antes do código ir para a branch main.

4. Ao instalar uma nova biblioteca, não se esqueça de adicioná-la aos requirements. 
    - Hint: ``pip freeze > requirements.txt``

5. Para atualizar localmente as branchs já deletadas no repositório utilize ``git pull && git remote update origin --prune``.