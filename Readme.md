# 1. Configuração do Ambiente
Para começar, você precisará de algumas bibliotecas compatíveis com reconhecimento facial e o sistema web. As principais são:

Django para o backend.
Streamlit para a interface web.
OpenCV e face_recognition para o reconhecimento facial.
Pillow para lidar com imagens.

Verificando Compatibilidade
Na versão 3.11.9 do Python:

Django (versão 4.1 e superiores) é compatível.
Streamlit (versão 1.19 ou superior) funciona bem.
OpenCV e face_recognition também são compatíveis, mas vale lembrar que o face_recognition usa o dlib, que pode precisar de alguns ajustes no ambiente para funcionar corretamente.

#Intalações
Execute este comando para instalar as bibliotecas necessárias

´´´bash
pip install django streamlit opencv-python face-recognition pillow
´´´
Instalar o Django Rest Framework para API
´´´bash
pip install djangorestframework
´´´
´´´ bash
pip install face_recognition
´´´

# Passo 2: Criar um Ambiente Virtual
No Windows, é uma boa prática usar um ambiente virtual para isolar as dependências do projeto. No Prompt de Comando, navegue até o diretório onde você deseja criar o projeto e execute:

´´´´bash
python -m venv nome_do_ambiente
´´´

Substitua nome_do_ambiente por algo que faça sentido, como env ou venv. Em seguida, ative o ambiente virtual com:

´´´bash
nome_do_ambiente\Scripts\activate
´´´
#3 Se ocorrer erro com o terminal do VsCode ou do Windows:

Se o terminal do VS Code está configurado para o PowerShell, você pode alterar a política de execução diretamente nele.

No terminal do PowerShell, execute o comando abaixo para permitir a execução de scripts locais:

powershell
´´´bash
Set-ExecutionPolicy RemoteSigned -Scope Process
´´´
Em seguida, ative o ambiente virtual com:

´´´bash
nome_do_ambiente\Scripts\activate
´´´

#Django
Crie o projeto e o aplicativo Django:
´´´bash
django-admin startproject projeto_facial
cd projeto_facial
python manage.py startapp entrada
´´´

Passo 3: Registrar o Aplicativo no Projeto
Para que o Django reconheça o novo aplicativo entrada, adicione-o ao arquivo de configurações (settings.py).

Abra o arquivo settings.py que está na pasta projeto_facial/projeto_facial/.


Agora que a estrutura básica está configurada, você pode rodar o servidor de desenvolvimento para verificar se tudo está funcionando corretamente:

´´´bash
python manage.py runserver
´´´
Abra o navegador e acesse http://127.0.0.1:8000/. Se tudo estiver certo, você verá a mensagem "Bem-vindo ao sistema de reconhecimento facial!".

Solução 1: Instalar os Pré-requisitos do dlib
Antes de tentar instalar o dlib, verifique se você tem os seguintes pré-requisitos instalados no seu sistema:

Instalar o Visual C++ Build Tools: O dlib requer as ferramentas de compilação do Visual C++ para compilar o código C++ que ele utiliza. Para instalar o Visual C++ Build Tools, siga os passos abaixo:

Baixe e instale o Microsoft Visual C++ Build Tools.
Durante a instalação, certifique-se de marcar a opção "Desktop development with C++", que inclui os compiladores necessários.

Instalar o cmake: O dlib também depende do cmake para ser compilado. Instale o cmake com o seguinte comando:

bash
Copiar código
pip install cmake

einstalar o dlib: Após a instalação do cmake e do Visual C++ Build Tools, tente instalar novamente o dlib:
pip install dlib

baixar dlin: pip install "C:\Users\leticia.lima\Documents\Projeto ´´´bash
Facial\dlib-19.22.99-cp39-cp39-win_amd64.whl"
 ´´´
Passos para enviar a foto para o servidor:
Certifique-se de que o servidor Django está em execução, e a URL de reconhecimento facial (definida como /reconhecer/) esteja funcionando corretamente.

Instale a biblioteca requests no seu ambiente, caso não tenha feito isso ainda:

´´´bash
pip install requests
´´´


Instalação da biblioteca requests:
pip install requests

Executando o script:
python enviar_foto.py


abrir o django web
- http://127.0.0.1:8000/admin/

Acessando a API de Alunos
http://127.0.0.1:8000/api/alunos/
