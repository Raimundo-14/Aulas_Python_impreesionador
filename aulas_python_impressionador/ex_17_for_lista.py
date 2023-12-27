meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]


for venda in vendas:
    # print(venda)
    if venda[1] >= meta:
        print(
            f'O vendedor(a) {venda[0]} bateu a meta de vendas, ele(a) fez {venda[1]} em vendas')
