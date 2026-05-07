import tkinter as tk
from tkinter import messagebox

#Importa de módulo (db.py) as funções conectar e criar_banco_e_tabela.
#conectar -> Conexão com o Mysql.
#criar_banco_e_tabela -> Garantir que o banco e as tabelas necessárias existam.
from db import conectar, criar_banco_e_tabela

#Importa do módulo (app.py).
#Representa a interface gráfica de botões, campos de texto, tabelas e lógica de interação com o usuário.
from app import AppCadastro

#Importa do módulo (auth).
#Criar usuários e autenticar.
from auth import criar_tabela_usuarios, autenticar_usuario


def tela_login(conn):
    login_root = tk.Tk()
    login_root.title("Login - Sistema Cadastro de Pessoas")
    login_root.geometry("400x180")
    login_root.resizable(False, False)

    usuario_autenticado = {"dados": None}

    frm = tk.Frame(login_root, padx=15, pady=15)
    frm.pack(fill="both", expand=True)

    tk.Label(frm, text="Usuário").grid(row=0, column=0, sticky="w", pady=(0, 4))
    ent_login = tk.Entry(frm, width=30)
    ent_login.grid(row=1, column=0, sticky="ew", pady=(0, 10))

    tk.Label(frm, text="Senha").grid(row=2, column=0, sticky="w", pady=(0, 4))
    ent_senha = tk.Entry(frm, width=30, show="*")
    ent_senha.grid(row=3, column=0, sticky="ew", pady=(0, 12))

    def fazer_login():
        login = ent_login.get().strip()
        senha = ent_senha.get().strip()

        if not login or not senha:
            messagebox.showwarning("Aviso", "Informe usuário e senha.")
            return

        usuario = autenticar_usuario(conn, login, senha)

        if usuario:
            usuario_autenticado["dados"] = usuario
            login_root.destroy()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    tk.Button(frm, text="Entrar", command=fazer_login).grid(row=4, column=0, sticky="ew")

    frm.grid_columnconfigure(0, weight=1)

    ent_login.focus()
    login_root.bind("<Return>", lambda e: fazer_login())

    login_root.mainloop()

    return usuario_autenticado["dados"]


if __name__ == "__main__":
    try:
        c = conectar(usar_banco=False)
        criar_banco_e_tabela(c)
        c.close()
    except Exception as e:
        print("Erro ao criar banco/tabela:", e)

    try:
        conn = conectar(usar_banco=True)
        criar_tabela_usuarios(conn)

        usuario = tela_login(conn)

        if usuario:
            app = AppCadastro(conn, usuario)
            app.mainloop()
        else:
            conn.close()

    except Exception as e:
        print("Erro ao iniciar sistema:", e)
        raise