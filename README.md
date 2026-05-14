# Sistema de Cadastro com Python, Tkinter e MySQL

Aplicação desktop desenvolvida em **Python** com interface gráfica em **Tkinter** e persistência de dados em **MySQL**. O projeto implementa operações de cadastro, listagem, pesquisa, atualização e exclusão de pessoas, além de estrutura para autenticação de usuários.[1][2]

## Funcionalidades

- Cadastro de pessoas com nome, e-mail e telefone.[1][2]
- Listagem e pesquisa de registros em interface gráfica.[3][2]
- Atualização e exclusão de dados via operações CRUD.[3][2]
- Integração com banco MySQL usando Python.[1][4]
- Estrutura organizada para evolução do projeto com novas funcionalidades.[1][2]
- Possibilidade de empacotamento em executável Windows com PyInstaller.[5][6]

## Tecnologias utilizadas

- Python 3
- Tkinter
- PyMySQL
- MySQL
- PyInstaller

## Estrutura sugerida do projeto

```bash
.
├── app.py
├── auth.py
├── config.py
├── db.py
├── main.py
├── repo.py
└── README.md
```

## Requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior
- MySQL Server
- pip

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

Instale as dependências:

```bash
pip install pymysql pyinstaller
```

## Configuração

Edite o arquivo `config.py` com os dados do seu ambiente:

```python
HOST = "localhost"
PORTA = 3306
USUARIO = "root"
SENHA = "sua_senha"
NOME_BANCO = "cadastro_db"
NOME_TABELA = "pessoas"
```

## Como executar

Inicie o projeto com:

```bash
python main.py
```

Na primeira execução, o sistema pode criar automaticamente o banco de dados e a tabela principal, dependendo da implementação atual do arquivo `db.py`.[3]

## Banco de dados

O projeto foi estruturado para trabalhar com uma tabela principal de pessoas, permitindo armazenar e consultar dados básicos de cadastro em um banco MySQL integrado à aplicação desktop.[1][4]

Campos principais utilizados no cadastro:

- `id`
- `nome`
- `email`
- `telefone`
- `criado_em`

## Empacotamento em executável Windows

Para gerar um arquivo `.exe`, pode ser utilizado o **PyInstaller**, que é uma abordagem comum para empacotar aplicações desktop Python para Windows.[5][6]

Comando básico:

```bash
pyinstaller --onefile --windowed main.py
```

Com nome personalizado:

```bash
pyinstaller --onefile --windowed --name "SistemaCadastro" main.py
```

O executável será gerado na pasta `dist/`.[5][6]

## Melhorias previstas

- Geração de executável para distribuição.
- Resetar senha.

## Objetivo do projeto

Este projeto foi criado com foco em prática de desenvolvimento desktop com Python, organização em camadas simples de acesso a dados e integração com banco relacional, servindo como base para evolução de um sistema administrativo maior.[1][2]

## Licença

Este projeto pode ser publicado com a licença que fizer mais sentido para o repositório, como MIT, caso se queira permitir uso e adaptação com poucas restrições.
