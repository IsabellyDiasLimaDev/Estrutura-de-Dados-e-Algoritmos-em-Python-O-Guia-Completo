# Ler 5 notas e informar a média

soma = 0
numero = 1

while numero < 6:
    nota = float(input(f"Digite a {numero} nota: "))
    soma += nota
    numero += 1

media = soma / 5
print(f"A média é {media}")


soma = 0

for numero in range(1,6):
    nota = float(input(f"Digite a {numero} nota: "))
    soma += nota
    numero += 1

media = soma / 5
print(f"A média é {media}")

