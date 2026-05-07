from typing import List, Tuple

#Importação da tabela Mysql
from config import NOME_TABELA

#Classe responsável por acessar o banco de dados e executar os comandos SQL.
#Cadastrando, listando, atualizando e excluindo registros (CRUD).
#Data Acess Object.
class PessoaRepo:
    def __init__(self, conn):

        #Estabelecer conexão com o db para realizar os processos.
        self.conn = conn

        #Criar conexão e permitir realizar os comandos CRUD.
        self.cur = conn.cursor()

    def inserir(self, nome: str, email: str, telefone: str, usuario_id: int) ->None:

        self.cur.execute(
            f"INSERT INTO {NOME_TABELA} (nome, email, telefone, usuario_id) VALUES (%s, %s, %s, %s)",

            (nome, email, telefone, usuario_id),
        )

    def listar_todos(self) -> List[Tuple]:

        self.cur.execute(
            f"SELECT id, nome, email, telefone, criado_em "
            
            f"FROM {NOME_TABELA} ORDER BY id DESC;"
        )

        return self.cur.fetchall()

    def pesquisar(self, termo: str) -> List[Tuple]:

        like = f"%{termo}%"

        self.cur.execute(
            f"""
                SELECT id, nome, email, telefone, criado_em
            FROM {NOME_TABELA}
            WHERE nome LIKE %s OR email LIKE %s OR telefone LIKE %s
            ORDER BY id DESC
            """,
            (like, like, like),
        )

        return self.cur.fetchall()

    def atualizar(self, id_: int, nome: str, email: str, telefone: str) -> None:

        self.cur.execute(
            f"UPDATE {NOME_TABELA} SET nome = %s, email = %s, telefone = %s WHERE id = %s;",

            (nome, email, telefone, id_),
        )

    def excluir(self, id_: int) -> None:

        self.cur.execute(
            f"DELETE FROM {NOME_TABELA} WHERE id = %s;",

            (id_,)
        )