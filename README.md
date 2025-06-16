# API-USER

Uma API RESTful para gerenciamento de usuários, desenvolvida com Django e Django REST Framework.

## ✨ Funcionalidades

*   **CRUD de Usuários**: Crie, leia, atualize e exclua informações de usuários.
*   **Endpoints RESTful**: Interface clara e padronizada para interação com a API.

## 🚀 Tecnologias Utilizadas

*   **Django**: Framework web Python.
*   **Django REST Framework**: Para construção da API REST.
*   **Python**: Linguagem de programação.
*   **SQLite**: Banco de dados (padrão para desenvolvimento).

## ⚙️ Instalação e Execução

Para rodar esta API em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x
*   pip

### Passos

1.  Clone o repositório:
    ```bash
    git clone https://github.com/rafaelcrb/API-USER.git
    cd API-USER
    ```
2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install Django djangorestframework
    ```
4.  Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  (Opcional) Crie um superusuário para o painel administrativo:
    ```bash
    python manage.py createsuperuser
    ```
6.  Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
    A API estará acessível em `http://127.0.0.1:8000/` (ou a porta indicada). Os endpoints específicos dependerão das configurações em `urls.py` e `views.py` (ex: `http://127.0.0.1:8000/users/`).

## 7. Endpoints (Exemplo)

*   **GET /users/**: Lista todos os usuários.
*   **POST /users/**: Cria um novo usuário.
*   **GET /users/{id}/**: Retorna os detalhes de um usuário específico.
*   **PUT /users/{id}/**: Atualiza completamente um usuário existente.
*   **PATCH /users/{id}/**: Atualiza parcialmente um usuário existente.
*   **DELETE /users/{id}/**: Exclui um usuário existente.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


