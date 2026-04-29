#Fornecer as ferramentas básicas para criar interfaces gráficas.
import tkinter as tk

#Contém widgets como botões, labels e tabelas (TreeView).
from tkinter import ttk

def aplicar_estilo (root:tk.Tk):
    #Alterar cores, tamanhos, fontes e tema visual do programa inteiro.
    style = ttk.Style(root)

    try:
        style.theme_use("clam") #Tema base

    except tk.TclError:
        pass

    fonte_padrao = ("Segoe UI", 10)

    #Aplicar fonte em todos os componentes.
    root.option_add("*Font", fonte_padrao)

    style.configure("TLabel", padding=(2, 2))

    style.configure("TEntry", padding=(4, 4))

    style.configure("TButton", padding = (6, 4))

    #Moldura utilizada para agrupar elementos.
    style.configure("TLabelframe", padding = (8, 8))

    style.configure("TLabelframe.Label", font = ("Segoe UI Semibold", 10))

    style.configure("Treeview.Heading", font = ("Segoe UI Semibold", 10))

def aplicar_zebra_treeview (tree: ttk.Treeview):

    tree.tag_configure("oddrow", background="F7F7F7")

    tree.tag_configure("evenrow", background="FFFFFF")

def preencher_treeview (tree: ttk.Treeview, rows):

    #O metodo retorna a lista com todos identificadores.
    for i in tree.get_children():

        #Remove a linha identificada.
        tree.delete(i)

    #idx:Índice da linha
    #r:Os valores das linhas (id, nome, etcs).
    for idx, r in enumerate(rows):

        tag = "evenrow" if idx % 2 == 0 else "oddrow"

        tree.insert("", "end", values=r, tags=(tag,))










