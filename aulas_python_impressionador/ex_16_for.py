print('Olá seja bem vindo(a)')
qnt_hospedes = int(input('Quantas pessoas ficariam no quarto? '))
print(f'Ok, entendi, ficarão {qnt_hospedes} no mesmo quarto!')
nome_cpf = qnt_hospedes
for i in range(nome_cpf):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    print(f'Seja bem vindo(a) {nome}.')
