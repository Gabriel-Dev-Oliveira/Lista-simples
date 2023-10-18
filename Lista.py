import tkinter as tk

def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entry_tarefa.delete(0, tk.END)

def remover_tarefa():
    try:
        selecao = lista_tarefas.curselection()[0]
        lista_tarefas.delete(selecao)
    except IndexError:
        pass

janela = tk.Tk()
janela.title("Lista de Tarefas")

entry_tarefa = tk.Entry(janela)
botao_adicionar = tk.Button(janela, text="Adicionar tarefa: ", command=adicionar_tarefa)
botao_remover = tk.Button(janela, text="Remover tarefa: ", command=remover_tarefa)
lista_tarefas = tk.Listbox(janela)

entry_tarefa.pack()
botao_adicionar.pack()
botao_remover.pack()
lista_tarefas.pack()

janela.mainloop()