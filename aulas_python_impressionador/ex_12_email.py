nome = input('Informe seu nome: ')
email = input('Informe seu email: ')

if nome and email:
    posiçao_a = email.find('@')
    servidor = email[posiçao_a:]
    if posiçao_a != -1 and '.' in servidor:
        print('Cadastro concluido com sucesso!')
    else:
        print('Email inválido, digite email corretamente.')
else:
    print('Digite seu nome e email corretamente!')
