meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

# i = 0
# Informe qual vendedor bateu a meta

for vendedor, qnte in vendas:
    if qnte >= meta:
        print(f'O vendedor(a) {vendedor}, vendeu R$ {qnte:,} reais')


# Qual produto vendeu mais em 2019 e 2020

vendas_produtos = [
    ('iphone', 558147, 951642),
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
    ('máquina de café', 718654, 867660),
    ('kindle', 531580, 78830),
    ('geladeira', 973139, 710331),
    ('adega', 892292, 646016),
    ('notebook dell', 422760, 694913),
    ('notebook hp', 154753, 539704),
    ('notebook asus', 887061, 324831),
    ('microsoft surface', 438508, 667179),
    ('webcam', 237467, 295633),
    ('caixa de som', 489705, 725316),
    ('microfone', 328311, 644622),
    ('câmera canon', 591120, 994303)
]

# for produto, data_2019, data_2020 in vendas_produtos:
# print(
# f'A quantidade de {produto}, vendeu em 2019 {data_2019:,}, é em 2020 {data_2020:,}''\n')

for produto, data_2019, data_2020 in vendas_produtos:
    if data_2019 > data_2020:

        print(
            f'A quantidade de {produto}, vendeu em 2019 foi de {data_2019:,}, foi maior que em 2020 {data_2020:,}, com crescimeto de {data_2019/data_2020-1:.1%}''\n')
    else:
        print(
            f'A quantidade de {produto}, vendeu em 2020 foi de {data_2020:,}, foi maior que em 2019 {data_2019:,}, com crescimeto de {data_2020/data_2019-1:.1%}''\n')
