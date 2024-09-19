# Todo List API

## Descrição

Este projeto é uma API de lista de tarefas (Todo List) desenvolvida com Django e Django REST Framework. A API permite criar, ler, atualizar e excluir listas de tarefas e itens associados. Inclui formatação personalizada de datas e horas para visualização.

## Funcionalidades

- **Gestão de usuários:**
  - Autenticação;
  - CRUD para usuários.
- **Lista de tarefas:**  
  Criação de listas de tarefas, como: "Tarefas diárias", "Reunião", etc... Fique à vontade para definir o nome que quiser.
  - CRUD para listas de tarefas.
- **Tarefas:**  
  Criação de tarefas, como: "Dar comida para o cachorro", "Reunião às 17h30min", etc... Fique à vontade para definir o nome que quiser.
    - CRUD para tarefas;
    - Tarefas podem ser inseridas em lista de tarefas;

## Requisitos
- [Python](https://www.python.org/downloads/) 3.x  
As bibliotecas estarão disponíveis no arquivos de requisitos posteriormente

## Configuração no Windows

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/username/todo-list-api.git
   cd todo-list-api
   ```

2. **Crie um Ambiente Virtual**
    ```bash
    py -m venv venv
    venv/Scripts/activate
    ```

3. **Instale as Dependências**
    ```python
    pip install -r requirements.txt
    ```

4. **Configure o Banco de Dados**

    Caso você opte por utilizar outro banco de dados, será necessário configurá-lo em settings.py
    Acesse o link abaixo para ter informações sobre os bancos suportados pelo Django
    [Databases|Django documentation](https://docs.djangoproject.com/en/5.1/ref/databases/)

5. **Execute as Migrações**
    ```python
    py manage.py migrate
    ```

6. **Crie um Super Usuário (Opcional, para acessar o admin)**
    ```python
    py manage.py createsuperuser
    #Siga os passos no terminal
    ```

7. **Inicie o servidor**
    ```python
    py manage.py runserver
    ```

    A API estará disponível em `http://127.0.0.1:8000/`

## Endpoints da API
- **[Autenticação de Usuário](#autenticação-de-usuário)**
- **[Cadastro de Usuário](#cadastro-de-usuário)**
- **[Lista de Tarefas](#listas-de-tarefas)**
- **[Tarefas](#itens)**

## Autenticação de usuário
Esta API utiliza autenticação baseada em tokens JWT para garantir que apenas usuários autenticados possam acessar certas funcionalidades.

- **Obter Token de Acesso**
  - `POST /api/auth/jwt/create`
  - **Body da requisição**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Resposta da requisição:**
    ```json
    {
      "access": "<access_token>",
      "refresh": "<refresh_token>"
    }
    ```
- **Autenticar requisições**

  Necessário em todas as requisições de páginas protegidas
  - **Header:**
    ```http
    Authorization: Bearer <access_token>
    ```

- **Renovar Acess Token**
  - `POST /api/auth/jwt/refresh`
  - **Body da requisição:**
    ```json
    {
      "refresh":"<refresh_token>"
    }
    ```
  - **Resposta da requisição:**
    ```json
    {
      "access":"<access_token>"
    }
    ```
  
## Cadastro de Usuário
A API com  a biblioteca [djoser](https://djoser.readthedocs.io/en/latest/) permite que novos usuários sejam registrados enviando os dados necessários.
- **Criar novo usuário:**
  - `POST api/auth/users`
  - **Body da requisição:**
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "email": "your_email", //(Optional)
    }
    ```
  - **Resposta da requisição:**
    ```json
    {
      "id": "user_id",
      "username": "your_username",
      "email": "your_email",
    }
    ```

## Djoser
Clique no link abaixo caso deseje informações adicionais sobre a biblioteca djoser, como: recuperação de senha, troca de nome de usuário, etc...

[djoser| Base Endpoints](https://djoser.readthedocs.io/en/latest/base_endpoints.html)

## Listas de Tarefas

- **Listar lista de Tarefas**
  - `GET /api/tasklists/`

- **Criar lista de Tarefas**
  - `POST /api/tasklists/`

- **Detalhes da lista de Tarefa**
  - `GET /api/tasklists/{id}/`

- **Atualizar lista de Tarefa**
  - `PUT /api/tasklists/{id}/`

- **Excluir lista de Tarefa**
  - `DELETE /api/tasklists/{id}/`

## Tarefas

- **Listar Tarefa**
  - `GET /api/items/`

- **Criar Tarefa**
  - `POST /api/items/`

- **Detalhes da Tarefa**
  - `GET /api/items/{id}/`

- **Atualizar Tarefa**
  - `PUT /api/items/{id}/`

- **Excluir Tarefa**
  - `DELETE /api/items/{id}/`

## Formatação de Data e Hora
Os campos de data e hora são formatados no formato `DD/MM/YY HH:MM:SS` em toda a API.

## Atualizações Futuras
- Notificações para lembrar o usuário de concluir a tarefa
- Verificação de nomes iguais em listas

## Licença
Este projeto é licensiado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

Este README inclui todos os tópicos, desde a configuração do ambiente até a descrição dos endpoints da API, atualizações futuras e licença.

