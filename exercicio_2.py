"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""

peso_paciente = float(input("Digite o peso do paciente (em kg): "))
print(type(peso_paciente))

dose_recomendada = peso_paciente * 2
print(f"Dose recomendada para o paciente: {dose_recomendada} mg")
