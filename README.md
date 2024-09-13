Claro! Vamos criar um arquivo `README.md` que descreva o programa e inclua uma breve documentação para ele. Em seguida, farei um resumo dos desafios que foram realizados.

### Conteúdo do `README.md`

```markdown
# Lead Management API

Este projeto é uma API para gerenciar leads utilizando Flask e SQLAlchemy. A API permite criar, ler, atualizar e deletar leads, e inclui funcionalidades de pesquisa e autenticação via JWT.

## Funcionalidades

- **CRUD de Leads**: Criar, ler, atualizar e deletar leads.
- **Pesquisa de Leads**: Pesquisa de leads pelo nome.
- **Autenticação**: Protege rotas para criar, atualizar e deletar leads usando tokens JWT.
- **Paginação**: Paginação de resultados para listagem de leads.

## Endpoints

### Leads

- `GET /leads`
  - **Descrição**: Lista todos os leads com opção de pesquisa e paginação.
  - **Parâmetros**:
    - `page`: Número da página (padrão: 1)
    - `per_page`: Número de leads por página (padrão: 10)
    - `name`: Nome para pesquisa (opcional)
  - **Resposta**:
    ```json
    {
      "leads": [
        {
          "id": 1,
          "name": "Test Lead",
          "latitude": "10.000",
          "longitude": "20.000",
          "temperature": "30",
          "interest": "High",
          "email": "test@example.com",
          "telefone": "123456789"
        }
      ],
      "total": 1,
      "pages": 1,
      "current_page": 1,
      "per_page": 10
    }
    ```

- `GET /leads/<int:id>`
  - **Descrição**: Recupera um lead específico pelo ID.
  - **Resposta**:
    ```json
    {
      "id": 1,
      "name": "Test Lead",
      "latitude": "10.000",
      "longitude": "20.000",
      "temperature": "30",
      "interest": "High",
      "email": "test@example.com",
      "telefone": "123456789"
    }
    ```

- `POST /leads`
  - **Descrição**: Cria um novo lead.
  - **Corpo da Requisição**:
    ```json
    {
      "name": "Test Lead",
      "latitude": "10.000",
      "longitude": "20.000",
      "temperature": "30",
      "interest": "High",
      "email": "test@example.com",
      "telefone": "123456789"
    }
    ```
  - **Resposta**:
    ```json
    {
      "message": "Lead criado com sucesso!"
    }
    ```

- `PUT /leads/<int:id>`
  - **Descrição**: Atualiza um lead existente.
  - **Corpo da Requisição**:
    ```json
    {
      "name": "Updated Lead Name",
      "latitude": "10.000",
      "longitude": "20.000",
      "temperature": "35",
      "interest": "Medium",
      "email": "updated@example.com",
      "telefone": "987654321"
    }
    ```
  - **Resposta**:
    ```json
    {
      "message": "Lead atualizado com sucesso!"
    }
    ```

- `DELETE /leads/<int:id>`
  - **Descrição**: Deleta um lead específico pelo ID.
  - **Resposta**:
    ```json
    {
      "message": "Lead deletado com sucesso!"
    }
    ```

### Autenticação

Para acessar os endpoints de criação, atualização e deleção, você precisa estar autenticado. Use o endpoint `/login` para obter um token JWT:

- `POST /login`
  - **Corpo da Requisição**:
    ```json
    {
      "username": "admin",
      "password": "123456"
    }
    ```
  - **Resposta**:
    ```json
    {
      "access_token": "YOUR_ACCESS_TOKEN"
    }
    ```

Inclua o token JWT no header da requisição como `Authorization: Bearer YOUR_ACCESS_TOKEN`.

## Testes

Os testes automatizados para a API estão localizados no arquivo `test_app.py`. Para executar os testes, use o comando:

```bash
pytest test_app.py
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/yourusername/lead-management-api.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd lead-management-api
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados e execute a aplicação:
   ```bash
   python app.py
   ```

## Dependências

- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- pytest

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
```

### Resumo dos Desafios Realizados

1. **Desafio 1**: Implementação do CRUD completo para leads, incluindo criação, leitura, atualização e deleção.
2. **Desafio 2**: Validação de dados com expressões regulares para e-mails e telefones, além de verificação de duplicidade de e-mails.
3. **Desafio 3**: Implementação de paginação para a listagem de leads e adição de parâmetros para pesquisa por nome.
4. **Desafio 4**: Adição de funcionalidade de pesquisa por nome, permitindo que usuários busquem leads pelo nome na rota GET `/leads`.
5. **Desafio 5**: Implementação de autenticação via token JWT para proteger as rotas de criação, atualização e deleção de leads.
6. **Desafio 6**: Criação de testes automatizados usando `pytest` para validar todas as rotas da API, incluindo operações de criação, leitura, atualização e deleção de leads.

Esses desafios adicionaram funcionalidades e garantiram a robustez da API, abordando autenticação, validação de dados, pesquisa e testes automatizados.