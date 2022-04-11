# Chess

Jogo de xadrez com interface web realizado como trabalho final da disciplina de Engenharia de Software II. 

Deploy já disponível no [Heroku](https://chess-es2-20221.herokuapp.com/).

## Requisitos

1. Instale Python 3.x.

## Dev setup

_Execute os comandos a partir do diretório base._

1. Crie o ambiente virtual Python através do comando: ``python -m venv venv``.

2. Ative o ambiente virtual: 
    Windows: ``./venv/Scripts/activate``.
    Linux/Mac: ``source ./venv/bin/activate``.

3. Instale as dependências: ``pip install -r requirements.txt``.

4. Inicie o servidor: ``python manage.py runserver``. O serviço é acessado por padrão através da url http://127.0.0.1:8000/.

## Guia do desenvolvedor

1. Estamos utilizando uma lógica [Trunk-based development](https://www.atlassian.com/br/continuous-delivery/continuous-integration/trunk-based-development).

2. Commits e pushes não podem ser enviados diretamente para branch main. Cada desenvolvedor deve trabalhar em sua branch e abrir um pull request com suas adições. Cada pull request deverá ter aprovação de 1 revisor e passar pelas etapas de build, lint e testes com sucesso para que o merge com a main possa ser realizado.

3. Cada merge feito com a main, sobe automaticamente uma nova release do deploy no [Heroku](https://chess-es2-20221.herokuapp.com/). Para garantir que o deploy não "quebre", existem as verificações antes do código ir para a branch main.

4. Ao instalar uma nova biblioteca, não se esqueça de adicioná-la aos requirements. 
    - Hint: ``pip freeze > requirements.txt``