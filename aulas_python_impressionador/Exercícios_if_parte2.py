""""
## 2. Cálculo de bônus com uma nova regra

- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas<br>
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

Use as mesmas variáveis de vendas_funcionários
"""

# crie seu código aqui
# obs: há 2 formas de fazer, com if dentro de if ou então com if e elif. Escolha a que você preferir

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 405 de bônus
"""

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700
meta_vendas1 = 2000
meta_vendas2 = 1000
bonus1 = 0.15
bonus2 = 0.10
bonus3 = 0.0


if vendas_funcionario1 >= meta_vendas1:
    print(f'Sua bonificação foi de {vendas_funcionario1 * bonus1}, parabéns!!')
elif vendas_funcionario1 >= meta_vendas2 and vendas_funcionario1 < meta_vendas1:
    print(f'Sua bonificação foi de {vendas_funcionario1 * bonus2}, parabéns!!')
else:
    print('Você não teve bonificação!!')

if vendas_funcionario2 >= meta_vendas1:
    print(f'Sua bonificação foi de {vendas_funcionario2 * bonus1}, parabéns!!')
elif vendas_funcionario2 >= meta_vendas2 and vendas_funcionario2 < meta_vendas1:
    print(f'Sua bonificação foi de {vendas_funcionario2 * bonus2}, parabéns!!')
else:
    print('Você não teve bonificação!!')

if vendas_funcionario3 >= meta_vendas1:
    print(f'Sua bonificação foi de {vendas_funcionario3 * bonus1}, parabéns!!')
elif vendas_funcionario3 >= meta_vendas2 and vendas_funcionario3 < meta_vendas1:
    print(f'Sua bonificação foi de {vendas_funcionario3 * bonus2}, parabéns!!')
else:
    print('Você não teve bonificação!!')
