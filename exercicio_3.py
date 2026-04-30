"""
#### Exercício 3

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""

receber_numero = int(input("Digite um número inteiro: "))

calcular_resto = receber_numero % 2

if calcular_resto == 0:
    print("Este número é par")
else:
    print("Este número é ímpar")
