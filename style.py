#Fornecer as ferramentas básicas para criar interfaces gráficas.
import tkinter as tk

#Contém widgets como botões, labels e tabelas (TreeView).
from tkinter import ttk

def aplicar_estilo(root: tk.Tk):
    # Alterar cores, tamanhos, fontes e tema visual do programa inteiro.
    style = ttk.Style(root)

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    fonte_padrao = ("Segoe UI", 10)
    fonte_titulo = ("Segoe UI Semibold", 10)
    fonte_heading = ("Segoe UI Semibold", 10)

    cor_bg_janela = "#F5F7FA"
    cor_bg_frame = "#FFFFFF"
    cor_borda = "#D9E1E8"
    cor_texto = "#111827"
    cor_texto_sec = "#374151"
    cor_entry_bg = "#FFFFFF"
    cor_heading_bg = "#EAF0F6"
    cor_heading_hover = "#DCE6F2"
    cor_select = "#DCEAFE"
    cor_focus = "#93C5FD"

    cor_btn_primary = "#2563EB"
    cor_btn_primary_hover = "#1D4ED8"

    cor_btn_success = "#059669"
    cor_btn_success_hover = "#047857"

    cor_btn_danger = "#DC2626"
    cor_btn_danger_hover = "#B91C1C"

    cor_btn_secondary = "#E5E7EB"
    cor_btn_secondary_hover = "#D1D5DB"

    root.configure(bg=cor_bg_janela)

    root.option_add("*Font", fonte_padrao)
    root.option_add("*Background", cor_bg_janela)
    root.option_add("*Foreground", cor_texto)

    style.configure(".", font=fonte_padrao)

    style.configure("TFrame", background=cor_bg_janela)

    style.configure(
        "TLabel",
        background=cor_bg_janela,
        foreground=cor_texto_sec,
        padding=(2, 2)
    )

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

    style.map(
        "TEntry",
        bordercolor=[("focus", cor_focus)],
        lightcolor=[("focus", cor_focus)],
        darkcolor=[("focus", cor_focus)]
    )

    style.configure(
        "TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground=cor_texto,
        relief="flat"
    )

    style.configure(
        "Primary.TButton",
        padding=(10, 6),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background=cor_btn_primary,
        bordercolor=cor_btn_primary,
        lightcolor=cor_btn_primary,
        darkcolor=cor_btn_primary,
        relief="flat"
    )

    style.map(
        "Primary.TButton",
        background=[("active", cor_btn_primary_hover), ("pressed", cor_btn_primary_hover)],
        bordercolor=[("active", cor_btn_primary_hover), ("pressed", cor_btn_primary_hover)]
    )

    style.configure(
        "Success.TButton",
        padding=(10, 6),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background=cor_btn_success,
        bordercolor=cor_btn_success,
        lightcolor=cor_btn_success,
        darkcolor=cor_btn_success,
        relief="flat"
    )

    style.map(
        "Success.TButton",
        background=[("active", cor_btn_success_hover), ("pressed", cor_btn_success_hover)],
        bordercolor=[("active", cor_btn_success_hover), ("pressed", cor_btn_success_hover)]
    )

    style.configure(
        "Danger.TButton",
        padding=(10, 6),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background=cor_btn_danger,
        bordercolor=cor_btn_danger,
        lightcolor=cor_btn_danger,
        darkcolor=cor_btn_danger,
        relief="flat"
    )

    style.map(
        "Danger.TButton",
        background=[("active", cor_btn_danger_hover), ("pressed", cor_btn_danger_hover)],
        bordercolor=[("active", cor_btn_danger_hover), ("pressed", cor_btn_danger_hover)]
    )

    style.configure(
        "Secondary.TButton",
        padding=(10, 6),
        font=fonte_padrao,
        foreground=cor_texto,
        background=cor_btn_secondary,
        bordercolor=cor_borda,
        lightcolor=cor_btn_secondary,
        darkcolor=cor_btn_secondary,
        relief="flat"
    )

    style.map(
        "Secondary.TButton",
        background=[("active", cor_btn_secondary_hover), ("pressed", cor_btn_secondary_hover)],
        bordercolor=[("active", cor_borda), ("pressed", cor_borda)]
    )

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

    cor_btn_primary = "#3B82F6"
    cor_btn_primary_hover = "#2563EB"

    cor_btn_success = "#10B981"
    cor_btn_success_hover = "#059669"

    cor_btn_danger = "#EF4444"
    cor_btn_danger_hover = "#DC2626"

    cor_btn_secondary = "#EEF2F7"
    cor_btn_secondary_hover = "#E2E8F0"

    cor_btn_excel = "#2F855A"
    cor_btn_excel_hover = "#276749"

    style.configure(
        "Primary.TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background=cor_btn_primary,
        bordercolor=cor_btn_primary,
        lightcolor=cor_btn_primary,
        darkcolor=cor_btn_primary,
        relief="flat"
    )

    style.map(
        "Primary.TButton",
        background=[("active", cor_btn_primary_hover), ("pressed", cor_btn_primary_hover)],
        bordercolor=[("active", cor_btn_primary_hover), ("pressed", cor_btn_primary_hover)]
    )

    style.configure(
        "Success.TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background=cor_btn_success,
        bordercolor=cor_btn_success,
        lightcolor=cor_btn_success,
        darkcolor=cor_btn_success,
        relief="flat"
    )

    style.map(
        "Success.TButton",
        background=[("active", cor_btn_success_hover), ("pressed", cor_btn_success_hover)],
        bordercolor=[("active", cor_btn_success_hover), ("pressed", cor_btn_success_hover)]
    )

    style.configure(
        "Danger.TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background=cor_btn_danger,
        bordercolor=cor_btn_danger,
        lightcolor=cor_btn_danger,
        darkcolor=cor_btn_danger,
        relief="flat"
    )

    style.map(
        "Danger.TButton",
        background=[("active", cor_btn_danger_hover), ("pressed", cor_btn_danger_hover)],
        bordercolor=[("active", cor_btn_danger_hover), ("pressed", cor_btn_danger_hover)]
    )

    style.configure(
        "Secondary.TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground=cor_texto,
        background=cor_btn_secondary,
        bordercolor=cor_borda,
        lightcolor=cor_btn_secondary,
        darkcolor=cor_btn_secondary,
        relief="flat"
    )

    style.map(
        "Secondary.TButton",
        background=[("active", cor_btn_secondary_hover), ("pressed", cor_btn_secondary_hover)],
        bordercolor=[("active", cor_borda), ("pressed", cor_borda)]
    )

    style.configure(
        "Excel.TButton",
        padding=(8, 5),
        font=fonte_padrao,
        foreground="#FFFFFF",
        background="#217346",
        bordercolor="#217346",
        lightcolor="#217346",
        darkcolor="#217346",
        relief="flat"
    )

    style.map(
        "Excel.TButton",
        background=[("active", "#1A5C38"), ("pressed", "#1A5C38")],
        bordercolor=[("active", "#1A5C38"), ("pressed", "#1A5C38")]
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