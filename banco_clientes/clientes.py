import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd


# conexao = sqlite3.connect('banco_cliente.db')
# c = conexao.cursor()
# c.execute(''' CREATE TABLE cliente (
# nome text,
# sobrenome text,
# cpf integer,
# email text,
# telefone integer
# )
# ''')

# conexao.commit()
# conexao.close()


def cadastrar_cliente():
    conexao = sqlite3.connect('banco_cliente.db')
    c = conexao.cursor()
    c.execute("  INSERT INTO cliente VALUES (:nome, :sobrenome, :cpf, :email, :telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'cpf': entry_cpf.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              }
              )

    conexao.commit()
    conexao.close()
    # entry_nome.delete() vai apos o registro apagar na interface
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_cpf.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")


# def exporta_clientes():
    # conexao = sqlite3.connect('banco_cliente.db')
    # c = conexao.cursor()
    # OID CHAVE PRÍMARIA
    # c.execute("SELECT *, oid FROM cliente")
    # cliente_cadastrado = c.fetchall()
    # cliente_cadastrado = pd.DataFrame(cliente_cadastrado, columns=[
    # 'nome', 'sobrenome', 'cpf', 'email', 'telefone', 'id'])
    # cliente_cadastrado.to_excel('banco_cliente.xlsx')
    # cliente_cadastrado = ExcelWriter('cliente_cadastrado.xlsx')

    # conexao.commit()
    # conexao.close()


janela = tk.Tk()
janela.title('Cadastro de clientes')

# Labals

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_cpf = tk.Label(janela, text='CPF')
label_cpf.grid(row=2, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=3, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=4, column=0, padx=10, pady=10)

# entry

entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_cpf = tk.Entry(janela, text='CPF', width=30)
entry_cpf.grid(row=2, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='Email', width=30)
entry_email.grid(row=3, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=4, column=1, padx=10, pady=10)

# botão

botao_cadastrar = tk.Button(
    janela, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


# columnspan = 2 para centralizar
# botao_exportar = tk.Button(
# janela, text='Exportar Base de Clientes', command=exporta_clientes)
# botao_exportar.grid(row=6, column=0, padx=10, pady=10,
# columnspan=2, ipadx=80)

janela.mainloop()
