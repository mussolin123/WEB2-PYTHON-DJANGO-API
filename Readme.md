# 📸 Reconhecimento Facial para Chamada de Alunos
Este projeto foi desenvolvido para modernizar o sistema de chamada de alunos nas salas de aula utilizando **reconhecimento facial.** Com uma interface web, os professores podem cadastrar e gerenciar imagens, e os alunos têm suas entradas avaliadas por meio de reconhecimento facial via webcam.

## 📋 Funcionalidades

<li> Cadastro de Alunos: Sistema de cadastro de fotos e informações de alunos. </li>
<li> Reconhecimento Facial em Tempo Real: Avaliação de entrada para identificar alunos em tempo real. </li>
<li> Gestão via Interface Web: Streamlit oferece uma interface intuitiva para professores e administradores. </li>
<li> API REST: Implementação com Django Rest Framework para operações de CRUD de alunos. </li>

## 🔧 1. Configuração do Ambiente
> [!WARNING]
> Para configurar o ambiente de desenvolvimento, siga as etapas abaixo.

<li> Python 3.11.9 (ou versão compatível) </li>
<li> Django para backend </li>
<li> Streamlit para interface web </li>
<li> OpenCV e face_recognition para reconhecimento facial </li>
<li> Pillow para manipulação de imagens </li>

# 📦 2. Instalação das Bibliotecas Necessárias
Use o comando abaixo para instalar todas as bibliotecas requeridas de uma vez:

```
pip install django streamlit opencv-python face-recognition pillow djangorestframework requests
```

## 🖥️ 2.1 Configuração do Ambiente Virtual
> [!IMPORTANT]
> Recomenda-se criar um ambiente virtual para isolar as dependências do projeto (principalmente se estiver executando no Windows).

```
python -m venv ambiente
```
Em seguida, ative o ambiente:
```
ambiente\Scripts\activate
```
## 🚀 2.2 Configuração do Projeto Django
> [!IMPORTANT]
> Se estiver usando o PowerShell no VS Code, execute o comando abaixo para permitir a execução de scripts:
```
django-admin startproject projeto_facial
cd projeto_facial
python manage.py startapp entrada
```

## 🛠️ 2.3 Preparação do Sistema para dlib
Algumas dependências adicionais são necessárias para o funcionamento do dlib:

### 2.3.1 Visual C++ Build Tools: Instale as ferramentas de compilação C++.

> https://visualstudio.microsoft.com/pt-br/downloads/?q=build+tools  <br>  <br>
![Mapa dos Terremotos](visual.png)

### 2.3.2 CMake: 
Instale o CMake com o comando:
```
pip install cmake
```

### 2.3.3 Dlib
Após instalar os pré-requisitos, instale o dlib:
```
pip install dlib
```

Se enfrentar problemas, você pode baixar e instalar o .whl compatível:
```
pip install "C:\Users\(usuario)\(caminho_whl)\dlib-19.22.99-cp39-cp39-win_amd64.whl"
```
Exemplo de como deve ficar: pip install "C:\Users\leticia.lima\Documents\Projeto Facial\dlib-19.22.99-cp39-cp39-win_amd64.whl"

> Substitua o "(usuario)" pelo seu usuário. Exemplo: leticia.lima <br>
> Substitua o "(caminho_whl)" pelo caminho em que salvou o arquivo "dlib-19.22.99-cp39-cp39-win_amd64.whl"

## 🐍 2.4. Executando o Servidor Django
Inicie o servidor de desenvolvimento do Django:
```
python manage.py runserver
```
Acesse o endereço http://127.0.0.1:8000/ para verificar se o sistema está funcionando.

## 🖼️3 Enviando Fotos para o Reconhecimento
Para enviar fotos ao servidor:

> [!WARNING]  
> Certifique-se de que o servidor está ativo.

Use a biblioteca requests para enviar imagens ao endpoint /reconhecer/.
```
pip install requests
```
Execute o script de envio de fotos:
```
python enviar_foto.py
```
## 2.5. 🔑 Criar suário base de dados Django
```
python manage.py createsuperuser
```


# 🔗 Links Úteis
<li> Django Admin: http://127.0.0.1:8000/admin/ </li>
<li> API de Alunos: http://127.0.0.1:8000/api/alunos/ </li>
