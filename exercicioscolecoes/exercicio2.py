'''
Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos,
fazendo a leitura dos valores por meio de uma estrutura de repetição.
Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
'''

dic = {}
for i in range(1,4):
    nome = input(f"Digite o nome do {i} aluno: ")
    nota = float(input(f"Digite a nota do {i} aluno: "))
    dic[nome] = nota

soma = 0
for nome, nota in dic.items():
    soma += nota

print(soma / 3)