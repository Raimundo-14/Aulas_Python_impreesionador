# importando toda biblioteca do tkinter
import tkinter as tk
# o Tk e a caixa da janela
janela = tk.Tk()

# mudança de titulo da janela
janela.title('CADASTRO DE ALUNOS')

# menssagem (fg = cor da letra e bg cor do fundo )
mensagem_1 = tk.Label(text='Cadastro de Alunos',
                      fg='red', bg='black', width=30, height=5)
# o pack coloca a mensagem de fato na janela
mensagem_1.pack()

mensagem_2 = tk.Label(text='Informe o seu nome completo',
                      fg='blue', bg='white', width=30, height=3)
mensagem_2.pack()

nome = tk.Entry()
nome.pack()

mensagem_3 = tk.Label(text='Informe o sua matricula',
                      fg='purple', bg='white', width=30, height=3)
mensagem_3.pack()

matricula = tk.Entry()
matricula.pack()

mensagem_4 = tk.Label(text='Informe a sua primeira nota:',
                      fg='black', bg='white', width=30, height=3)

mensagem_4.pack()
nota_1 = tk.Entry()
nota_1.pack()

mensagem_5 = tk.Label(text='Informe a sua segunda nota:',
                      fg='black', bg='white', width=30, height=3)

mensagem_5.pack()
nota_2 = tk.Entry()
nota_2.pack()

mensagem_6 = tk.Label(text='Informe a sua terceira nota:',
                      fg='black', bg='white', width=30, height=3)

mensagem_6.pack()
nota_3 = tk.Entry()
nota_3.pack()

# visualizar a janela
janela.mainloop()
