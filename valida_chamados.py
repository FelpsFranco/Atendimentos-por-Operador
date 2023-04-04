import tkinter as tk
from tkinter import ttk
import pandas as pd


def pontua(dados, janela):
    janela.destroy()
    chm = pd.read_excel('Chamados_ambiente.xlsx')
    quantidade = chm['Operador'].value_counts()
    chamados = pd.DataFrame({'Operador': quantidade.index, 'Chamados': quantidade.values})
    chamados['Operador'] = chamados['Operador'].apply(corrige)
    jivo_ambiente = pd.merge(dados, chamados, on='Operador')
    print(jivo_ambiente)
    # jivo_ambiente.to_excel('Chamados.xlsx', index=False)
    tela_todos(jivo_ambiente)
    x = 0

    # if chamados['Conversas aceitas'] / (chamados['Chamados'] * 100) <= 50:
    #     return x == 5
    #
    # elif chamados['Conversas aceitas'] / (chamados['Chamados'] * 100) >= 50 < 80:
    #     return x == 2
    #
    # elif chamados['Conversas aceitas'] / (chamados['Chamados'] * 100) >= 80:
    #     return x == 1


def tela_todos(dados):
    tela_pontua = tk.Tk()
    tela_pontua.geometry('1200x400')
    tela_pontua.configure(bg='gray80')
    tela_pontua.title('PONTUAÇÃO')

    pontue_arv = ttk.Treeview(tela_pontua)
    pontue_arv['columns'] = ('Operador', 'Conversas aceitas', 'Avaliação positiva', 'Avaliação negativa', 'Chamados',
                             'Tempo de Resposta')
    pontue_arv.column('Operador', width=100, anchor='w')
    pontue_arv.column('Conversas aceitas', width=50, anchor='center')
    pontue_arv.column('Avaliação positiva', width=50, anchor='center')
    pontue_arv.column('Avaliação negativa', width=50, anchor='center')
    pontue_arv.column('Tempo de Resposta', width=20, anchor='center')
    pontue_arv.column('Chamados', width=50, anchor='center')
    pontue_arv['columns'] = tuple(dados.columns)
    pontue_arv['show'] = 'headings'
    scrollbar = ttk.Scrollbar(orient="vertical", command=pontue_arv.yview())
    pontue_arv.place(x=0, y=100, width=800, height=400)
    pontue_arv.configure(yscrollcommand=scrollbar.set)

    for col in dados.columns:
        pontue_arv.heading(col, text=col)

    for index, row in dados.iterrows():
        values = tuple(row.values)
        pontue_arv.insert("", tk.END, text=index, values=values)

    pontue_arv.pack(fill="both", expand=True)

    tela_pontua.mainloop()


def visualiza(dados, janela):
    janela.destroy()
    tela_chamados = tk.Tk()
    tela_chamados.geometry('1000x400')
    tela_chamados.configure(bg='gray80')
    tela_chamados.title('CHAMADOS')

    tree = ttk.Treeview(tela_chamados)
    tree['columns'] = ('Operador', 'Conversas aceitas', 'Avaliação positiva', 'Avaliação negativa', 'Tempo de Resposta')
    tree.column('Operador', width=100, anchor='w')
    tree.column('Conversas aceitas', width=60, anchor='center')
    tree.column('Avaliação positiva', width=60, anchor='center')
    tree.column('Avaliação negativa', width=60, anchor='center')
    tree.column('Tempo de Resposta', width=60, anchor='center')
    tree['columns'] = tuple(dados.columns)
    tree['show'] = 'headings'
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview())
    tree.place(x=0, y=100, width=1200, height=600)
    tree.configure(yscrollcommand=scrollbar.set)

    for col in dados.columns:
        tree.heading(col, text=col)

    for index, row in dados.iterrows():
        values = tuple(row.values)
        tree.insert("", tk.END, text=index, values=values)

    tree.pack(fill="both", expand=True)
    tela_chamados.mainloop()


def corrige(nome):
    new = nome.split('(')[0]
    return new.split()[0]


ch = pd.read_excel('marco_chamados.xlsx')
ch['Operador'] = ch['Operador'].apply(corrige)
ch_new = ch[['Operador', 'Conversas aceitas', 'Avaliação positiva', 'Avaliação negativa', 'Tempo de resposta médio ('
                                                                                          'em segundos)']]
ch_puro = ch_new.loc[ch_new['Conversas aceitas'] != 0]
ch_puro = ch_puro.rename(columns={'Tempo de resposta médio (em segundos)': 'Tempo de Resposta'})

print(ch_puro)

inicial = tk.Tk()
inicial.geometry('300x100')
inicial.configure(bg='gray80')
inicial.title('CHAMADOS')

escolha = tk.Label(inicial, text='DESEJA GERAR UMA VISUALIZAÇÃO?', font=('Inter', 8), bg='gray80')
escolha.place(x=50, y=5)

op1 = tk.Button(inicial, text='SIM', font=('Inter', 8), bg='gray80', command=lambda: visualiza(ch_puro, inicial))
op1.place(x=90, y=50, width=40)

op2 = tk.Button(inicial, text='NÃO', font=('Inter', 8), bg='gray80', command=lambda: pontua(ch_puro, inicial))
op2.place(x=180, y=50, width=40)

inicial.mainloop()
