#Biblioteca utilizada para conectar o python ao banco de dados MySQL.
import pymysql

#Tratar erros específicos do Mysql.
from pymysql import err as pymysql_err

#Variáveis necessários para conectar ao db.
from config import HOST, PORTA, USUARIO, SENHA, NOME_BANCO, NOME_TABELA

#Função para abrir conexão com o banco de dados.
def conectar(usar_banco=True):
    #Inicia bloco para tratar possíveis erros de conexão, falha na autenticação, servidor desligado ou banco inexistente.
    try:
        if usar_banco:
            return pymysql.connect(
                host=HOST,
                port=PORTA,
                user=USUARIO,
                password=SENHA,
                database=NOME_BANCO,
                # Suporta emojis e todos os caracteres especiais
                charset="utf8mb4",
                autocommit=True,
                #Usado para retornar dados como tuplas (linhas de valores).
                cursorclass=pymysql.cursors.Cursor
            )
        else:
            return pymysql.connect(
                host=HOST,
                port=PORTA,
                user=USUARIO,
                password=SENHA,
                charset="utf8mb4",
                autocommit=True,
                cursorclass=pymysql.cursors.Cursor
            )

    except pymysql_err.OperationalError as e:
        #1049 Código de erro no Mysql "Unknown database" (banco de dados desconhecido)
        if getattr(e, "args", None) and e.args and e.args[0] == 1049:
            conn = pymysql.connect(
                host=HOST,
                port=PORTA,
                user=USUARIO,
                password=SENHA,
                charset="utf8mb4",
                autocommit=True,
                cursorclass=pymysql.cursors.Cursor
            )

            criar_banco_e_tabela(conn)

            conn.close()

            return pymysql.connect(
                host=HOST,
                port=PORTA,
                user=USUARIO,
                password=SENHA,
                database=NOME_BANCO,
                charset="utf8mb4",
                autocommit=True,
                cursorclass=pymysql.cursors.Cursor
            )
        raise

#Função responsável que recebe como parâmetro uma conexão ativa.
#Cursor permite executar comandos SQL.
def criar_banco_e_tabela(conn):
    with conn.cursor() as cur:
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS {NOME_BANCO}"
            "DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
        )
        #Collate: define as regras de comparação e ordenação de textos.
        #General: tipo de regra de ordenação
        #Ci: Ignora diferença de maiúscula e minúscula

        cur.execute(f"USE {NOME_BANCO};")

        cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS {NOME_TABELA} (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(120) NOT NULL,
                        email VARCHAR(150) UNIQUE NOT NULL,
                        telefone VARCHAR(20) NOT NULL,
                        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    )   ENGINE=InnoDB DEFAULT CHARACTER=utf8mb4;;
                    """
        )
        #Engine: Tipo de mecanismo de armazenamento usado pelo o MySQL.
        #InnoDB: Suporta transações e chaves estrangeiras, para relacionar tabelas no futuro.

def criar_tabela_logs(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs_sistema (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario_id INT NOT NULL,
            acao VARCHAR(50) NOT NULL,
            tabela_afetada VARCHAR(50) NOT NULL,
            registro_id INT NULL,
            descricao TEXT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_logs_usuario
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)
    conn.commit()
    cur.close()
