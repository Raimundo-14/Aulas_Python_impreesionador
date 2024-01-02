vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]
soma_vendas = sum(vendas)
print(f'A soma das vendas foi de {soma_vendas:,} reais')

soma_vendedores = len(vendedores)
print(f'A quantidade é de {soma_vendedores} vendedores')

media_vendas = soma_vendas / soma_vendedores
print(f'A media de venda de todos os vendedores {media_vendas:,}')

for i, venda in enumerate(vendas):
    print(f'O vendendor {vendedores[i]}, vendeu {vendas[i]:,}')
