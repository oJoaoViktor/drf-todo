# Todo List API

## Descrição

Este projeto é uma API de lista de tarefas (Todo List) desenvolvida com Django e Django REST Framework. A API permite criar, ler, atualizar e excluir listas de tarefas e itens associados. Inclui formatação personalizada de datas e horas para visualização.

## Funcionalidades

- **Listar Tarefas**: Obtém uma lista de todas as listas de tarefas.
- **Criar Tarefa**: Cria uma nova lista de tarefas.
- **Detalhes da Tarefa**: Obtém detalhes de uma lista de tarefas específica.
- **Atualizar Tarefa**: Atualiza uma lista de tarefas existente.
- **Excluir Tarefa**: Exclui uma lista de tarefas.
- **Listar Itens**: Obtém uma lista de todos os itens em uma lista de tarefas.
- **Criar Item**: Adiciona um novo item a uma lista de tarefas.
- **Detalhes do Item**: Obtém detalhes de um item específico.
- **Atualizar Item**: Atualiza um item existente.
- **Excluir Item**: Exclui um item.

## Requisitos

- Python 3.x
- Django
- Django REST Framework

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
    Acesse o link abaixo para ter acesso aos bancos suportados pelo Django

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

### Listas de Tarefas

- **Listar Tarefas**
  - `GET /api/tasklists/`

- **Criar Tarefa**
  - `POST /api/tasklists/`

- **Detalhes da Tarefa**
  - `GET /api/tasklists/{id}/`

- **Atualizar Tarefa**
  - `PUT /api/tasklists/{id}/`

- **Excluir Tarefa**
  - `DELETE /api/tasklists/{id}/`

## Itens

- **Listar Itens**
  - `GET /api/items/`

- **Criar Item**
  - `POST /api/items/`

- **Detalhes do Item**
  - `GET /api/items/{id}/`

- **Atualizar Item**
  - `PUT /api/items/{id}/`

- **Excluir Item**
  - `DELETE /api/items/{id}/`

## Formatação de Data e Hora
Os campos de data e hora são formatados no formato `DD/MM/YY HH:MM:SS` em toda a API.

## Atualizações Futuras
- Autenticação de usuários
- Notificações para lembrar o usuário de concluir a tarefa
- Verificação de nomes iguais em listas

## Licença
Este projeto é licensiado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

Este README inclui todos os tópicos, desde a configuração do ambiente até a descrição dos endpoints da API, atualizações futuras e licença.

