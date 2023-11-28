cpf = (input('Digite seu cpf, informe apenas os números: '))

# tratar o cpf
# retirar os espaços vazios
cpf = cpf.strip()
# retirar os pontos
cpf = cpf.replace('.', '')
# retirar os traços
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(f'O cpf informado é {cpf}')
else:
    print('Informe o CPF corretamente')
