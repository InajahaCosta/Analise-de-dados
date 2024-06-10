import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') # pegando o arquivo CVC

#1 Apresente a porcentagem de quantas missoes derão certo
success_count = np.char.find(arr[:,7], 'Success') # pegando somente a coluna 8(7) Status Mission
cond_success = arr[success_count >= 0]
success_percentage = (cond_success.shape[0] / (arr.shape[0] - 1)) * 100  # Excluindo a primeira linha

print("Porcentagem de Sucesso: {:.1f}%".format(success_percentage))


#2 Media de gastos de uma missao se baseando nas que possuem valor disponivel > 0
cost = arr[1:, 6].astype(float)
cost_positive = cost[cost > 0]
media = np.mean(cost_positive)
print("Media de Gastos: {:.1f}".format(media))

#3 Quantas missoes espaciais neste dataSet foram realizadas pelo estados unidos
country = np.char.find(arr[: , 2], 'USA') 
arrCountry = arr[country >= 0]
print("Missoes Realizadas pelos EUA:", arrCountry.shape[0])

#4 missao mais cara realizada pela Spacex
spacex_missions = arr[np.char.find(arr[:, 1], 'SpaceX') >= 0]
costs_max = spacex_missions[:, 6].astype(float).max()
print("Maior custo de missão realizada pela SpaceX:", costs_max)

#5 Nome das empressas que ja realizaram Missoes juntamente com suas respectivas quantidades
nome = np.unique(arr[:, 1], return_counts=True)
for i in range(nome[0].size):
        print("Company:", nome[0][i], "Number of Missions:", nome[1][i])