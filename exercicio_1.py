"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""
primeira_nota = float(input("Digite a primeira nota: "))
print(type(primeira_nota))

segunda_nota = float(input("Digite a segunda nota: "))
print(type(segunda_nota))

terceira_nota = float(input("Digite a terceira nota: "))
print(type(terceira_nota))

media_notas = (primeira_nota + segunda_nota + terceira_nota)/3
print(f"Média: {media_notas}")
