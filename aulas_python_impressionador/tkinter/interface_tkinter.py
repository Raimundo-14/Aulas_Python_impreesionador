# importando toda biblioteca do tkinter
import tkinter as tk
# o Tk e a caixa da janela
janela = tk.Tk()

# mudança de titulo da janela
janela.title('CADASTRO DE ALUNOS')

# menssagem (fg = cor da letra e bg cor do fundo )
mensagem_1 = tk.Label(text='Cadastro de Alunos',
                      fg='white', bg='black', width=25, height=5)
# o pack coloca a mensagem de fato na janela
mensagem_1.pack()

mensagem_2 = tk.Label(text='Informe o seu nome completo',
                      fg='black', bg='white', width=25, height=3)
mensagem_2.pack()

nome = tk.Entry(text='Informe seu nome completo: ')
nome.pack()

mensagem_3 = tk.Label(text='Informe o sua matricula',
                      fg='black', bg='white', width=25, height=3)
mensagem_3.pack()

matricula = tk.Entry(text='Informe seu nome completo: ')
matricula.pack()


# visualizar a janela
janela.mainloop()
