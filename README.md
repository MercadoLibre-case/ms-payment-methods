# MS-Payment-Methods Service

Este é um microserviço de "Métodos de Pagamento" desenvolvido como parte do desafio do Meli. O serviço é construído usando FastAPI e segue os princípios da Clean Architecture para garantir uma separação clara de responsabilidades e manutenibilidade do código.

## 🚀 Tecnologias Utilizadas

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- Pytest (para testes)
- Pytest-cov (para cobertura de testes)
- HTTPX (para testes de integração)

## 📁 Estrutura do Projeto

```
ms-payment-methods/
├── app/
│   ├── controllers/       # Controladores da API
│   ├── dtos/              # Data Transfer Objects
│   ├── domain/            # Regras de negócio e entidades
│   ├── infrastructure/    # Implementações de infraestrutura
│   └── shared/            # Código compartilhado
├── tests/                 # Testes automatizados
├── main.py                # Ponto de entrada da aplicação
└── requirements.txt       # Dependências do projeto
```

## 📦 Arquitetura

O projeto segue os princípios da Clean Architecture, dividindo o código em camadas:

- **Controllers**: Responsáveis por receber requisições HTTP e retornar respostas
- **DTOs**: Objetos de transferência de dados para validação e serialização
- **Domain**: Contém as regras de negócio e entidades do sistema
- **Infrastructure**: Implementações concretas de interfaces (repositórios, serviços externos)
- **Shared**: Código compartilhado entre as camadas

## 🧪 Cobertura de Testes

Usando o CodeCov chegamos a seguinte tag de cobertura de testes:
[![codecov](https://codecov.io/gh/MercadoLibre-case/ms-payment-methods/branch/main/graph/badge.svg)](https://codecov.io/gh/MercadoLibre-case/ms-payment-methods)
