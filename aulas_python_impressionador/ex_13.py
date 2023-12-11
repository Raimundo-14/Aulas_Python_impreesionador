# Faturamento do mês

meses = ['janneiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', ]
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 10000]

# Adicionar uma lista na outra
vendas_1sem.extend(vendas_2sem)

# maior valor do ano
maior_valor = max(vendas_1sem)
print(max(vendas_1sem))

# o menor mês do ano
menor_valor = min(vendas_1sem)
print(min(vendas_1sem))
# achar o a posição na lista --> index
i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(menor_valor)
print(i_maior_valor)
print(i_menor_valor)

print(f'O melhor mês do ano foi {meses[10]}, com {maior_valor} em vendas')
print(f'O pior mês do ano foi {meses[11]}, com {menor_valor} em vendas')


faturamento = sum(vendas_1sem)
print(f'O faturamento total é de R$ {faturamento}')
