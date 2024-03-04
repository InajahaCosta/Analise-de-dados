# Exercicio 1 
times = [ "Argentina","França","Croácia","Marrocos","Holanda",]

# a) 3 primeiros colocados
tres_primeiros = times[:3]
print(tres_primeiros)

# b) ultimos 2 colocados
dois_ultimos = times[-2:]
print(dois_ultimos)

# c) lista em ordem alfabetica
times.sort()
print(times)

# d) em que posição esta Holanda
posicao_holanda = times.index("Holanda")
print("Holanda está na posição:", posicao_holanda)


# Exercicio 2 
loja1 = {"IPhone 15", "Galaxy S21", "Xiaomi Redmi",}
loja2 = {"IPhone 15", "Galaxy S21", "Xiaomi Redmi 9 Pro",}

total_modelos = loja1.union(loja2)
print (total_modelos)

modelos_disponiveis_em_ambas_as_lojas = loja1.intersection(loja2)
print (modelos_disponiveis_em_ambas_as_lojas)


#  Exercicio 3 
# Dicionário para armazenar nome, média e situação final do aluno
aluno = {}

# Leitura do nome e média do aluno
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

# Armazenamento no dicionário
aluno["Nome"] = nome
aluno["Média"] = media

# Função para determinar a situação do aluno com base na média
def determinar_situacao(media):
    if media >= 60:
        return "AP" 
    else:
        return "RP" 
    
# Determinar a situação final do aluno
aluno["Situação"] = determinar_situacao(media)

# Exibição do conteúdo do dicionário
print()
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")