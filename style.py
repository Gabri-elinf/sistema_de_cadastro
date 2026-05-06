#Fornecer as ferramentas básicas para criar interfaces gráficas.
import tkinter as tk

#Contém widgets como botões, labels e tabelas (TreeView).
from tkinter import ttk

def aplicar_estilo(root: tk.Tk):
    # Alterar cores, tamanhos, fontes e tema visual do programa inteiro.
    style = ttk.Style(root)

    try:
        style.theme_use("clam")  # Tema base
    except tk.TclError:
        pass

    fonte_padrao = ("Segoe UI", 10)
    fonte_titulo = ("Segoe UI Semibold", 10)
    fonte_heading = ("Segoe UI Semibold", 10)

    # Cores
    cor_bg_janela = "#F5F7FA"
    cor_bg_frame = "#FFFFFF"
    cor_borda = "#D9E1E8"
    cor_texto = "#111827"
    cor_texto_sec = "#374151"
    cor_entry_bg = "#FFFFFF"
    cor_heading_bg = "#EAF0F6"
    cor_heading_hover = "#DCE6F2"
    cor_select = "#DCEAFE"

    root.configure(bg=cor_bg_janela)

    # Aplicar fonte padrão em widgets tk
    root.option_add("*Font", fonte_padrao)
    root.option_add("*Background", cor_bg_janela)
    root.option_add("*Foreground", cor_texto)

    # Frame padrão
    style.configure(
        "TFrame",
        background=cor_bg_janela
    )

    # Label
    style.configure(
        "TLabel",
        background=cor_bg_janela,
        foreground=cor_texto_sec,
        padding=(2, 2)
    )

    # Entry
    style.configure(
        "TEntry",
        padding=(6, 4),
        fieldbackground=cor_entry_bg,
        foreground=cor_texto,
        bordercolor=cor_borda,
        lightcolor=cor_borda,
        darkcolor=cor_borda,
        relief="solid"
    )

    # Button padrão
    style.configure(
        "TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground=cor_texto,
        relief="flat"
    )

    # LabelFrame
    style.configure(
        "TLabelframe",
        background=cor_bg_frame,
        bordercolor=cor_borda,
        relief="solid",
        padding=(10, 10)
    )

    style.configure(
        "TLabelframe.Label",
        background=cor_bg_janela,
        foreground=cor_texto,
        font=fonte_titulo
    )

    # Treeview corpo
    style.configure(
        "Treeview",
        background="#FFFFFF",
        foreground=cor_texto,
        fieldbackground="#FFFFFF",
        bordercolor=cor_borda,
        lightcolor=cor_borda,
        darkcolor=cor_borda,
        rowheight=28,
        relief="flat",
        font=fonte_padrao
    )

    style.map(
        "Treeview",
        background=[("selected", cor_select)],
        foreground=[("selected", cor_texto)]
    )

    # Treeview cabeçalho
    style.configure(
        "Treeview.Heading",
        background=cor_heading_bg,
        foreground=cor_texto,
        bordercolor=cor_borda,
        lightcolor=cor_borda,
        darkcolor=cor_borda,
        relief="flat",
        padding=(8, 6),
        font=fonte_heading
    )

    style.map(
        "Treeview.Heading",
        background=[("active", cor_heading_hover)]
    )


def aplicar_zebra_treeview(tree: ttk.Treeview):
    tree.tag_configure("oddrow", background="#F8FAFC", foreground="#111827")
    tree.tag_configure("evenrow", background="#FFFFFF", foreground="#111827")


def preencher_treeview(tree: ttk.Treeview, rows):
    for i in tree.get_children():
        tree.delete(i)

    for idx, r in enumerate(rows):
        tag = "evenrow" if idx % 2 == 0 else "oddrow"
        tree.insert("", "end", values=r, tags=(tag,))