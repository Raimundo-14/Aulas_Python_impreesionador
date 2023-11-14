# Quantidade de Vendas de Coca = 150<br>
# Quantidade de Vendas de Pepsi = 130<br>
# Preço Unitário da Coca = 1,50 <br>
# Preço Unitário da Pepsi = 1,50<br>
# Custo da Loja: 2.500,00

qnt_venda_coca = 150
qnt_venda_pepsi = 130
preco_un_coca = 1.50
preco_un_pepsi = 1.50
custo_loja = 2500

# Qual foi o faturamento de Pepsi da Loja?"""

fatura_pepsi = qnt_venda_pepsi * preco_un_pepsi
print(f'O valor em vendas de Pepsi foi de R$ {fatura_pepsi}')

# 2. Qual foi o faturamento de Coca da Loja?
fatura_coca = qnt_venda_coca * preco_un_coca
print(f'O valor em vendas de Coca-Cola foi de R$ {fatura_coca}')

# 3. Qual foi o Lucro da loja?
fatura_loja = fatura_pepsi + fatura_coca
lucro = fatura_loja - custo_loja
print(f'O faturamento total da loja foi de R$ {fatura_loja}')
print(f'O lucro total da loja foi de R$ {lucro}')

# Coca -> Código: BEB1300543<br>
# Pepsi -> Código: BEB1300545<br>
# Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
# Vodka Smirnoff -> Código: BAC17675002<br>

BEB = str()

codigo = str(input('Informe o código da bebida: (insira em letra maiscula): '))
if 'BEB' in codigo:
    print('Essa é uma bebida alcoolica!')
else:
    print('Essa não é uma bebida alcoolica')
