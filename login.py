import tkinter as tk
from tkinter import ttk, messagebox
from auth import autenticar_usuario


class TelaLogin(tk.Toplevel):
    def __init__(self, master, conn, callback_sucesso):
        super().__init__(master)

        self.conn = conn
        self.callback_sucesso = callback_sucesso

        self.title("Login")
        self.geometry("500x400")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        frm = ttk.Frame(self, padding=15)
        frm.pack(fill="both", expand=True)

        ttk.Label(frm, text="Usuário").grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.ent_login = ttk.Entry(frm, width=30)
        self.ent_login.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(frm, text="Senha").grid(row=2, column=0, sticky="w", pady=(0, 4))
        self.ent_senha = ttk.Entry(frm, width=30, show="*")
        self.ent_senha.grid(row=3, column=0, sticky="ew", pady=(0, 12))

        ttk.Button(frm, text="Entrar", command=self.fazer_login).grid(
            row=4, column=0, sticky="ew", pady=(0, 8)
        )

        #este botão chama o método abrir_tela_recuperacao
        ttk.Button(frm, text="Esqueci minha senha", command=self.abrir_tela_recuperacao).grid(
            row=5, column=0, sticky="ew"
        )

        frm.grid_columnconfigure(0, weight=1)

        self.update_idletasks()
        largura = self.winfo_width()
        altura = self.winfo_height()
        x = (self.winfo_screenwidth() - largura) // 2
        y = (self.winfo_screenheight() - altura) // 2
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        self.deiconify()
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))
        self.focus_force()

        self.bind("<Return>", lambda e: self.fazer_login())
        self.ent_login.focus()

    #método do botão Entrar
    def fazer_login(self):
        login = self.ent_login.get().strip()
        senha = self.ent_senha.get().strip()

        if not login or not senha:
            messagebox.showwarning("Aviso", "Informe usuário e senha.", parent=self)
            return

        usuario = autenticar_usuario(self.conn, login, senha)

        if usuario:
            self.destroy()
            self.callback_sucesso(usuario)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.", parent=self)

    def abrir_tela_recuperacao(self):
        top = tk.Toplevel(self)
        top.title("Recuperação de senha")
        top.geometry("360x180")
        top.resizable(False, False)
        top.transient(self)
        top.grab_set()

        frm_rec = ttk.Frame(top, padding=20)
        frm_rec.pack(fill="both", expand=True)

        ttk.Label(frm_rec, text="Recuperação de senha").grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )

        ttk.Label(frm_rec, text="E-mail").grid(
            row=1, column=0, sticky="w", pady=(0, 4)
        )

        #guarda o campo para usar no outro método
        self.ent_email_recuperacao = ttk.Entry(frm_rec, width=30)
        self.ent_email_recuperacao.grid(
            row=2, column=0, sticky="ew", pady=(0, 12)
        )

        #botão que chama o método enviar_codigo_recuperacao
        ttk.Button(frm_rec, text="Enviar código", command=self.enviar_codigo_recuperacao).grid(
            row=3, column=0, sticky="ew", pady=(0, 8)
        )

        ttk.Button(frm_rec, text="Fechar", command=top.destroy).grid(
            row=4, column=0, sticky="ew"
        )

        frm_rec.grid_columnconfigure(0, weight=1)

        #salva a janela para usar como parent nas mensagens
        self.top_recuperacao = top

    #método já existente no seu código
    def enviar_codigo_recuperacao(self):
        email = self.ent_email_recuperacao.get().strip()

        if not email:
            messagebox.showwarning("Aviso", "Informe o e-mail.", parent=self.top_recuperacao)
            return

        messagebox.showinfo(
            "Recuperação",
            f"Código enviado para: {email}",
            parent=self.top_recuperacao
        )