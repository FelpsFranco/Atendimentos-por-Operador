from tkinter import *
from tkinter import ttk


def cria_tela(arq):
    tela_chamados = Tk()
    tela_chamados.geometry('600x600')
    tela_chamados.configure(bg='gray80')
    tela_chamados.title('CHAMADOS')

    tree = ttk.Treeview(tela_chamados, columns=("Column1", "Column2", "Column3", "Column4", "Column5"), show='headings')
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview())
    tree.place(x=0, y=100, width=1200, height=600)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.heading("#1", text="OPERADOR", anchor='w')
    tree.heading("#2", text="ACEITOS", anchor='w')
    tree.heading("#3", text="POSITIVOS", anchor='w')
    tree.heading("#4", text="NEGATIVOS", anchor='w')
    tree.heading("#5", text="TEMPO RESPOSTA", anchor='w')

    dados = arq()
    for operador, aceitos, positivos, negativos, tempo in dados:
