# Descrição

FlicksAPI é uma API desenvolvida para gerenciar informações relacionadas a filmes. 
Ela oferece um conjunto abrangente de funcionalidades, incluindo operações **CRUD** (Create, Read, Update, Delete) para atores, gêneros de filmes, filmes e reviews desses filmes. 

A FlicksAPI conta com um **sistema de permissão de usuário** que controla o acesso às diferentes funcionalidades com base nos privilégios atribuídos a cada usuário.
Além disso, a FlicksAPI utiliza **autenticação baseada em JSON Web Tokens (JWT)** para garantir a segurança dos dados e o controle de acesso.

A FlicksAPI foi desenvolvida utilizando o **framework Django** e o **Django REST Framework**. 
Além disso, a API  também segue o **padrão REST**.

## Instalação

Siga os passos abaixo para clonar e executar o projeto no seu computador:

1. **Clone o repositório**
   
   ``` git clone https://github.com/seu-usuario/FlicksAPI.git ```

2. **Crie um ambiente virtual**
   
   ``` python -m venv venv ```

3. **Ative o ambiente virtual**
   
   - Windows: ``` venv\Scripts\activate ```
   - Linux/MacOs: ``` source venv/bin/activate ```

4. **Instale as dependências**
   
   ``` pip install -r requirements.txt ```

5. **Instale as dependências de desenvolvimento (opcional)**
   
   ``` pip install -r requirements_dev.txt ``` 

6. **Realize as migrações do banco de dados**
    
   ``` python manage.py migrate ```

7. **Crie um superusuário**
   
   ``` python manage.py createsuperuser ```

9. **Inicie o servidor de desenvolvimento**
    
   ``` python manage.py runserver ```

10. **Acesse o projeto no seu navegador**
    
   Abra o navegador e digite **http://127.0.0.1:8000** para ver o projeto em execução.

   Ou você também pode acessar a API pelo link **[mcandidon.pythonanywhere.com](https://mcandidon.pythonanywhere.com)**
   
---

## Observações

- Para acessar as funcionalidades da API e acessar a página de admin é **necessário** criar um superusuário!
- É recomendado que o usuário utilize o **Postman** para explorar e interargir com a API de maneira mais eficiente.

## Passo a passo para primeira utilização da API

1. **Criar um super usuário**
   
   Abra o terminal e execute os seguintes comandos para criar um super usuário:

   ``` python manage.py createsuperuser ```

2. **Acessar o admin do django (OPCIONAL)**
   - Acesse o /admin
   - Faça login com o super usuário que você criou.
   - Se desejar, crie um novo usuário comum e configure suas permissões de acordo com suas necessidades.

3. **Obter token de acesso**
   - Acesse a URL *'http://localhost:8000/authentication/token/'* em seu navegador ou cliente HTTP.
   - Informe o nome de usuário e senha do usuário que você criou.
   - Um token JWT será gerado como resposta.

4. **Utilizar a API**
   
   Ao acessar qualquer URL da API, incluindo operações CRUD para atores, gêneros de filmes, filmes e reviews,
   você precisará incluir o Bearer Token de acesso JWT que foi gerado anteriormente.
   
   Lembre-se de que o token JWT gerado possui validade de um dia!

5. **Importar atores do arquivo csv (OPCIONAL)**
   
   Caso deseje importar 50 atores fornecidos no arquivo *'actors.csv'* para o banco de dados, execute o seguinte comando no terminal:
   
   ``` python manage.py import_actors actors.csv ```
   
   Isso irá importar os atores do arquivo *'actors.csv'* e adicioná-los ao banco de dados, poupando o esforço de cadastrá-los manualmente.
