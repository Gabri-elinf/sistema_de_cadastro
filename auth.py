import bcrypt

def gerar_hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verificar_senha(senha_digitada: str, senha_hash: str) -> bool:
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

def autenticar_usuario(conn, login: str, senha: str):
    cur = conn.cursor()
    cur.execute("""
        SELECT id, nome, login, senha_hash, ativo
        FROM usuarios
        WHERE login = %s
    """, (login,))
    usuario = cur.fetchone()
    cur.close()

    if not usuario:
        return None

    usuario_id, nome, login_db, senha_hash, ativo = usuario

    if ativo != 1:
        return None

    if verificar_senha(senha, senha_hash):
        return {
            "id": usuario_id,
            "nome": nome,
            "login": login_db
        }

    return None