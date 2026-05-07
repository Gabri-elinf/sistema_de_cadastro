import tkinter as tk
from tkinter import ttk, messagebox
from auth import criar_usuario


class TelaCadastroUsuario(tk.Toplevel):
    def __init__(self, master, conn):
        super().__init__(master)

        self.conn = conn

        self.title("Cadastrar Usuário")
        self.geometry("500x360")
        self.minsize(500, 360)
        self.resizable(False, False)

        self.var_nome = tk.StringVar()
        self.var_login = tk.StringVar()
        self.var_senha = tk.StringVar()
        self.var_confirmar = tk.StringVar()

        frm = ttk.Frame(self, padding=20)
        frm.pack(fill="both", expand=True)

        ttk.Label(frm, text="Nome").grid(row=0, column=0, sticky="w", pady=(0, 6))
        ttk.Entry(frm, textvariable=self.var_nome, width=42).grid(row=1, column=0, sticky="ew", pady=(0, 14))

        ttk.Label(frm, text="Login").grid(row=2, column=0, sticky="w", pady=(0, 6))
        ttk.Entry(frm, textvariable=self.var_login, width=42).grid(row=3, column=0, sticky="ew", pady=(0, 14))

        ttk.Label(frm, text="Senha").grid(row=4, column=0, sticky="w", pady=(0, 6))
        ttk.Entry(frm, textvariable=self.var_senha, width=42, show="*").grid(row=5, column=0, sticky="ew", pady=(0, 14))

        ttk.Label(frm, text="Confirmar senha").grid(row=6, column=0, sticky="w", pady=(0, 6))
        ttk.Entry(frm, textvariable=self.var_confirmar, width=42, show="*").grid(row=7, column=0, sticky="ew", pady=(0, 18))

        ttk.Button(frm, text="Salvar Usuário", command=self.salvar).grid(row=8, column=0, sticky="ew")

        frm.grid_columnconfigure(0, weight=1)

    def salvar(self):
        nome = self.var_nome.get().strip()
        login = self.var_login.get().strip()
        senha = self.var_senha.get().strip()
        confirmar = self.var_confirmar.get().strip()

        if not nome or not login or not senha or not confirmar:
            messagebox.showwarning("Validação", "Preencha todos os campos.", parent=self)
            return

        if len(login) < 3:
            messagebox.showwarning("Validação", "O login deve ter pelo menos 3 caracteres.", parent=self)
            return

        if len(senha) < 6:
            messagebox.showwarning("Validação", "A senha deve ter pelo menos 6 caracteres.", parent=self)
            return

        if senha != confirmar:
            messagebox.showwarning("Validação", "As senhas não coincidem.", parent=self)
            return

        try:
            criar_usuario(self.conn, nome, login, senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso.", parent=self)
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar usuário:\n\n{e}", parent=self)