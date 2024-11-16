# fiap-postech-Sub4
# Serviço de Venda de Veículos

Este microserviço gerencia a listagem de veículos disponíveis para venda e o registro de vendas. Ele é desenvolvido utilizando FastAPI e SQLAlchemy com PostgreSQL.

## **Requisitos**

- Python 3.9 ou superior
- PostgreSQL
- Docker e Docker Compose (opcional, para rodar com containers)
- Pipenv ou pip para gerenciar dependências

---

# Vehicle Sales Service

Este é o serviço de **venda de veículos** que faz parte de uma solução maior para a revenda de automóveis. Este serviço é responsável por:
- Listar veículos disponíveis para venda.
- Registrar vendas de veículos.
- Listar veículos vendidos.

Este serviço funciona como um microserviço independente, com um banco de dados segregado.

---

## 🚀 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pytest](https://pytest.org/)
- [Docker](https://www.docker.com/)

---

## 📦 Estrutura do Projeto

```plaintext
vehicle-sales-service/
│
├── src/
│   ├── main.py                # Arquivo principal do serviço
│   ├── models.py              # Modelos do banco de dados
│   ├── schemas.py             # Esquemas Pydantic para validação
│   ├── database.py            # Configuração do banco de dados
│   ├── services/              # Lógica do negócio
│   └── tests/                 # Testes automatizados
│
├── requirements.txt           # Dependências do projeto
├── Dockerfile                 # Configuração Docker
├── docker-compose.yml         # Configuração para ambiente local
├── buildspec.yml              # Arquivo necessário para CI/CD
└── README.md                  # Documentação do projeto
```

---


## 🛠️ Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/kcrismartins/fiap-postech-Sub4-vehicle-sales-service.git
   cd vehicle-sales-service
2. Clone o repositório:
   ```bash
   pip install -r requirements.txt
3. Clone o repositório:
   ```bash
   DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/sales_service_db
4. Clone o repositório:
   ```bash
   python -m src.database

---

## ⚙️ Executar o Serviço

### Localmente:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Com Docker Compose:

1. Construa e inicie o container:
   ```bash
   docker-compose up --build
2. O serviço estará disponível em: http://localhost:8000

---

## 📂 Endpoints Disponíveis

### Cadastro de Veículos

- Rota: GET /vehicles
- Descrição: Registra uma venda de veículo.
- Body:
   ```json
   {
  "vehicle_id": 1,
  "buyer_cpf": "12345678901",
  "sale_date": "2024-11-15"
   }
   ```

---

## 🧪 Testando o Serviço

1. Execute os testes:
   ```bash
   pytest --disable-warnings

2. Para gerar o relatório de cobertura:
    ```bash
    coverage run -m pytest
   coverage report -m
   coverage html  # Para um relatório em HTML

