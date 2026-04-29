import tkinter as tk

from tkinter import ttk, messagebox, filedialog

from openpyxl import Workbook

from openpyxl.utils import get_column_letter

from db import conectar

from repo import PessoaRepo

from style import aplicar_estilo, aplicar_zebra_treeview, preencher_treeview

def validar(nome: str, email: str, telefone: str):

    if not nome or len(nome.strip()) < 3:
        return False, "Informe um nome com pelo menos 3 caracteres"

    if not email or '@' not in email:

        return False, "Informe um e-mail válido ( ex.: nome@dominio.com)."

    if not telefone or len(telefone.strip()) < 8:

        return False, "Informe um telefone válido."

    return True, ""


class AppCadastro(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Cadastro de Pessoas")

        self.geometry("980x580")

        self.minsize(900, 520)

        aplicar_estilo(self)

        self.conn = conectar(usar_banco=True)

        self.repo = PessoaRepo(self.conn)

        self.var_id = tk.StringVar()

        self.var_nome = tk.StringVar()

        self.var_email = tk.StringVar()

        self.var_telefone = tk.StringVar()

        self.var_pesquisa = tk.StringVar()

        self.var_status = tk.StringVar(value="Pronto.")

        self._montar_formulario ()

        self._montar_botoes()

        self._montar_tabela()

        self._montar_statusbar()

        self._centralizar_janela()

        self.bind("<Control-n>", lambda e: self._limpar_campos())

        self.bind("<F5>", lambda e: self.listar_todos())

        self.listar_todos()

        self.protocol("WM_DELETE_WINDOW", self._fechar)


    def centralizar_janela(self):

        self.update_idletasks()

        largura = self.winfo_width()

        altura = self.winfo_height()

        tela_l = self.winfo_screenwidth()

        tela_a = self.winfo_screenheight()

        x = (tela_l- largura) // 2

        y = (tela_a- altura) // 3

        self.geometry(f"f{largura}x{altura}+{x}+{y}")

    def montar_formulario(self):

        frm = ttk.Frame(self, text = "Dados da Pessoa")

        frm.pack(side=tk.TOP, fill=tk.X, padx = 10, pady = 10)

        ttk.Label(frm, text = "ID:").grid(row = 0, column = 0, padx = 10, pady = 10, stick="e")

        ttk.Entry(frm, textvariable = self.var_id, width=8, state="readonly").grid(
            row = 0, column = 1, padx = 5, pady = 5, stick="w")

        ttk.Label(frm, text="Nome:").grid(row=0, column=2, padx=5, pady=5, stick="e")

        ttk.Entry(frm, textvariable=self.var_nome, width=40).grid(row=0, column=3, padx=5, pady=5, stick="w")

        ttk.Label(frm, text="E-mail:").grid(row=1, column=0, padx=5, pady=5, stick="e")

        ttk.Entry(frm, textvariable=self.var_email, width=40).grid(row=1, column=3, padx=5, pady=5, stick="w")

        ttk.Label(frm, text="Telefone:").grid(row=1, column=2, padx=5, pady=5, stick="e")

        ttk.Entry(frm, textvariable=self.var_telefone, width=22).grid(row=1, column=3, padx=5, pady=5, stick="w")

        ttk.Label(frm, text="Pesquisar (nome, e-mail ou telefone):").grid(row=2, column=0, padx=5, pady=5, stick="e")

        ttk.Entry(frm, textvariable=self.var_pesquisa, width=40).grid(row=2, column=1, columnspan=3, padx=5, pady=5, stick="w")

        frm.grid_columnconfigure(3, weight=1)

    def _montar_botoes(self):

        frm = ttk.Frame(self)

        frm.pack(side=tk.TOP, fill=tk.X, padx = 10, pady = 5)

        ttk.Button(frm, text="Cadastrar", command=self.cadastrar).pack(side=tk.LEFT, padx=5)

        ttk.Button(frm, text="Atualizar", command==self.atualizar).pack(side=tk.LEFT, padx=5)

        ttk.Button(frm, text="Excluir", command=self.excluir).pack(side=tk.LEFT, padx=5)

        ttk.Button(frm, text="Limpar Campos (Ctrl+N)", command=self._limpar_campos).pack(side=tk.LEFT, padx=5)

        ttk.Button(frm, text="Pesquisar", command=self.pesquisar).pack(side=tk.LEFT, padx=5)

        ttk.Button(frm, text="Exportar para Excel", command=self.exportar_excel).pack(side=tk.LEFT, padx=5)


    def _montar_tabela(self):

        frm = ttk.LabelFrame(self, text="Registros")

        frm.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx = 10, pady = 5)

        cols = ("id", "nome", "email", "telefone", "criado_em")

        self.tree = ttk.Treeview(frm, columns=cols, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID", command=lambda: self._ordernar_por(0))

        self.tree.heading("nome", text="Nome", command=lambda: self._ordernar_por(1))

        self.tree.heading("email", text="E-mail", command=lambda: self._ordernar_por(2))

        self.tree.heading("telefone", text="Telefone", command=lambda: self._ordernar_por(3))

        self.tree.heading("criado_em", text="Criado em", command=lambda: self._ordernar_por(4))

        self.tree.column("id", width=60, anchor="center")

        self.tree.column("nome", width=260, anchor="w")

        self.tree.column("email", width=260, anchor="w")

        self.tree.column("telefone", width=140, anchor="center")

        self.tree.column("criado_em", width=160, anchor="center")

        vsb = ttk.Scrollbar(frm, orient="vertical", command=self.tree.yview)

        hsb = ttk.Scrollbar(frm, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscroll=vsb.set, xscroll = hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        hsb.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        aplicar_zebra_treeview(self.tree)

        self.tree.bind("<Double-1>", self._on_duplo_clique)


    def _montar_statusbar(self):

        ttk.Label(self, textvariable=self.var_status, anchor="w").grid(
            side=tk.BOTTOM, fill=tk.X)

    def _cadastrar(self):

        nome = self.var_nome.get().strip()

        email = self.var_email.get().strip()

        telefone = self.var_telefone.get().strip()

        ok, msg = validar(nome, email, telefone)

        if not ok:

            messagebox.showwarning(title="Validação", msg)

            return
        try:

            self.repo.inserir(nome, email, telefone)

            self.var_status.set("Cadastrado realizado com sucesso.")

            self.listar_todos()

            self._limpar_campos()

        except Exception as e:

            messagebox.showerror("Erro ao Cadastrar", message=f"Falha ao inserir:\n\n{e}")

    def atualizar(self):

        if not self.var_id.get():

            messagebox.showinfo(title="Atualizar", message="Selecione um registro (duplo clique da tabela).")

            return

        nome = self.var_nome.get().strip()

        email = self.var_email.get().strip()

        telefone = self.var_telefone.get().strip()

        ok,msg = validar(nome, email, telefone)

        if not ok:

            messagebox.showwarning(title="Validação", msg)

            return

        try:

            self.repo.atualizar(int(self.var_id.get()), email, telefone)

            self.var_status.set("Registro atualizado com sucesso.")

            self.listar_todos()

            self._limpar_campos()

        except Exception as e:

            messagebox.showerror(title="Erro ao atualizar", message=f"Falha ao atualizar:\n\n{e}")


    def excluir(self):

        if not self.var_id.get():

            messagebox.showinfo(title="Excluir", message="Selecione um registro (duplo clique da tabela).")

            return

        if not messagebox.askyesno(title="Confirmação", message="Deseja realmente excluir este registro?"):

            return

        
















































































































