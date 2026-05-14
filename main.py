import tkinter as tk
from tkinter import messagebox

from db import conectar, criar_banco_e_tabela
from app import AppCadastro
from auth import (
    criar_tabela_usuarios,
    autenticar_usuario,
    buscar_usuario_por_login,
    atualizar_senha_temporaria,
    trocar_senha_definitiva
)
from email_service import gerar_senha_temporaria, enviar_email_recuperacao


def abrir_tela_troca_senha(login_root, conn, usuario, ent_login, ent_senha):
    janela = tk.Toplevel(login_root)
    janela.title("Trocar senha")
    janela.geometry("350x220")
    janela.resizable(False, False)
    janela.transient(login_root)
    janela.grab_set()

    frm = tk.Frame(janela, padx=15, pady=15)
    frm.pack(fill="both", expand=True)

    tk.Label(frm, text="Nova senha").grid(row=0, column=0, sticky="w")
    ent_nova = tk.Entry(frm, show="*", width=30)
    ent_nova.grid(row=1, column=0, pady=(0, 10), sticky="ew")

    tk.Label(frm, text="Confirmar nova senha").grid(row=2, column=0, sticky="w")
    ent_confirma = tk.Entry(frm, show="*", width=30)
    ent_confirma.grid(row=3, column=0, pady=(0, 12), sticky="ew")

    def salvar():
        nova = ent_nova.get().strip()
        confirma = ent_confirma.get().strip()

        if not nova or not confirma:
            messagebox.showwarning("Aviso", "Preencha os dois campos.", parent=janela)
            return

        if nova != confirma:
            messagebox.showerror("Erro", "As senhas não coincidem.", parent=janela)
            return

        try:
            trocar_senha_definitiva(conn, usuario["login"], nova)
            usuario["deve_trocar_senha"] = 0

            messagebox.showinfo(
                "Sucesso",
                "Senha alterada com sucesso. Faça login novamente com a nova senha.",
                parent=janela
            )

            janela.destroy()

            ent_login.delete(0, tk.END)
            ent_senha.delete(0, tk.END)

            ent_login.focus_set()

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao alterar senha: {e}", parent=janela)

    tk.Button(frm, text="Salvar nova senha", command=salvar).grid(row=4, column=0, sticky="ew")
    frm.grid_columnconfigure(0, weight=1)
    ent_nova.focus()


def tela_login(conn):
    login_root = tk.Tk()
    login_root.title("Login - Sistema Cadastro de Pessoas")
    login_root.geometry("400x260")
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

    def concluir_login(usuario):
        usuario_autenticado["dados"] = usuario
        login_root.destroy()

    def fazer_login():
        login = ent_login.get().strip()
        senha = ent_senha.get().strip()

        if not login or not senha:
            messagebox.showwarning("Aviso", "Informe usuário e senha.")
            return

        usuario = autenticar_usuario(conn, login, senha)

        if not usuario:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
            return

        if usuario.get("deve_trocar_senha", 0) == 1:
            abrir_tela_troca_senha(login_root, conn, usuario, ent_login, ent_senha)
            return

        concluir_login(usuario)

    def esqueci_senha():
        janela = tk.Toplevel(login_root)
        janela.title("Recuperação de senha")
        janela.geometry("350x160")
        janela.resizable(False, False)
        janela.transient(login_root)
        janela.grab_set()

        frm_rec = tk.Frame(janela, padx=15, pady=15)
        frm_rec.pack(fill="both", expand=True)

        tk.Label(frm_rec, text="Usuário").grid(row=0, column=0, sticky="w", pady=(0, 4))
        ent_usuario_rec = tk.Entry(frm_rec, width=30)
        ent_usuario_rec.grid(row=1, column=0, sticky="ew", pady=(0, 12))

        def enviar_recuperacao():
            login = ent_usuario_rec.get().strip()

            if not login:
                messagebox.showwarning("Aviso", "Informe o usuário.", parent=janela)
                return

            usuario = buscar_usuario_por_login(conn, login)

            if not usuario:
                messagebox.showerror("Erro", "Usuário não encontrado.", parent=janela)
                return

            email_destino = usuario.get("email")

            if not email_destino:
                messagebox.showerror("Erro", "Usuário sem e-mail cadastrado.", parent=janela)
                return

            try:
                nova_senha = gerar_senha_temporaria()
                atualizar_senha_temporaria(conn, login, nova_senha)
                enviar_email_recuperacao(email_destino, nova_senha)

                messagebox.showinfo(
                    "Sucesso",
                    f"Uma nova senha foi enviada para: {email_destino}",
                    parent=janela
                )
                janela.destroy()

            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao enviar e-mail: {e}", parent=janela)

        tk.Button(
            frm_rec,
            text="Enviar recuperação por e-mail",
            command=enviar_recuperacao
        ).grid(row=2, column=0, sticky="ew")

        frm_rec.grid_columnconfigure(0, weight=1)
        ent_usuario_rec.focus()

    tk.Button(frm, text="Entrar", command=fazer_login).grid(row=4, column=0, sticky="ew", pady=(0, 8))
    tk.Button(frm, text="Esqueci minha senha", command=esqueci_senha).grid(row=5, column=0, sticky="ew")

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