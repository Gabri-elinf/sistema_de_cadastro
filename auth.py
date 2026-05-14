import bcrypt
from datetime import datetime, timedelta
from email_service import gerar_senha_temporaria, enviar_email_recuperacao

def gerar_hash_senha(senha):
    return bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verificar_senha(senha_digitada, senha_hash):
    return bcrypt.checkpw(
        senha_digitada.encode("utf-8"),
        senha_hash.encode("utf-8")
    )

def criar_tabela_usuarios(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            login VARCHAR(50) NOT NULL UNIQUE,
            senha_hash VARCHAR(255) NOT NULL,
            ativo TINYINT(1) NOT NULL DEFAULT 1,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()

def criar_usuario(conn, nome: str, login: str, senha: str):
    senha_hash = gerar_hash_senha(senha)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO usuarios (nome, login, senha_hash)
        VALUES (%s, %s, %s)
    """, (nome, login, senha_hash))
    conn.commit()
    cur.close()

def buscar_usuario_por_login(conn, login):
    cursor = conn.cursor()
    sql = """
        SELECT id, nome, login, email, senha_hash, ativo, deve_trocar_senha
        FROM usuarios
        WHERE login = %s
    """
    cursor.execute(sql, (login,))
    resultado = cursor.fetchone()
    cursor.close()

    if resultado:
        return {
            "id": resultado[0],
            "nome": resultado[1],
            "login": resultado[2],
            "email": resultado[3],
            "senha_hash": resultado[4],
            "ativo": resultado[5],
            "deve_trocar_senha": resultado[6]
        }
    return None


def autenticar_usuario(conn, login, senha):
    usuario = buscar_usuario_por_login(conn, login)

    if not usuario:
        return None

    if usuario["ativo"] != 1:
        return None

    senha_hash = usuario["senha_hash"]

    if not senha_hash:
        return None

    if verificar_senha(senha, senha_hash):
        return usuario

    return None


def atualizar_senha(conn, login, nova_senha):
    nova_senha_hash = gerar_hash_senha(nova_senha)

    cursor = conn.cursor()
    sql = """
        UPDATE usuarios
        SET senha_hash = %s
        WHERE login = %s
    """
    cursor.execute(sql, (nova_senha_hash, login))
    conn.commit()
    cursor.close()

def atualizar_senha_temporaria(conn, login, nova_senha):
    nova_senha_hash = gerar_hash_senha(nova_senha)

    cursor = conn.cursor()
    sql = """
        UPDATE usuarios
        SET senha_hash = %s,
            deve_trocar_senha = 1
        WHERE login = %s
    """
    cursor.execute(sql, (nova_senha_hash, login))
    conn.commit()
    cursor.close()

def trocar_senha_definitiva(conn, login, nova_senha):
    nova_senha_hash = gerar_hash_senha(nova_senha)

    cursor = conn.cursor()
    sql = """
        UPDATE usuarios
        SET senha_hash = %s,
            deve_trocar_senha = 0
        WHERE login = %s
    """
    cursor.execute(sql, (nova_senha_hash, login))
    conn.commit()
    cursor.close()

