'''
Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição
para somar todos os valores digitados
'''

lista = []

for i in range(1, 6):
    valor = int(input(f"Digite o {i} valor: "))
    lista.append(valor)

soma = 0
for item in lista:
    soma += item

print(f"Total lista: {soma}")
