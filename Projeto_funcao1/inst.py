"""Como instalar um ambiente virtual: 
1 - criar virtual env: python -m venv (.venv)  .VENV É O NOME DA PASTA
2 - ativar o virtual env: (.venv/Scripts/activate
2.1 - caso não consiga ativar: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
volta para o passo 2.
3 - instalar dependências: pip install {nome da lib}
5 - Visualizar instalações: pip list
4 - criar requirements.txt : pip freeze > requirements.txt - como se fosse o sumario do seu ambiente 
6 - desativar: deactivate
7 - instalar através do requirements.txt: pip install -r requirements.txt
"""