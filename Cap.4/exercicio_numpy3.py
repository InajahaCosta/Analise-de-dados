import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

#1
success_count = np.char.find(arr[:,7], 'Success') # pegando somente a coluna 8(7) Status Mission
cond_success = arr[success_count >= 0]
success_percentage = (cond_success.shape[0] / (arr.shape[0] - 1)) * 100  # Excluindo a primeira linha

print("Porcentagem de Sucesso: {:.1f}%".format(success_percentage))


#2
cost = arr[1:, 6].astype(float)
cost_positive = cost[cost > 0]
print("Media de Gastos: {:.1f}".format(np.mean(cost_positive)))

#3
country = np.char.find(arr[: , 2], 'USA') 
arrCountry = arr[country >= 0]
print("Missoes Realizadas pelos EUA:", arrCountry.shape[0])

#4
spacex_missions = arr[np.char.find(arr[:, 1], 'SpaceX') >= 0]
costs_max = spacex_missions[:, 6].astype(float).max()
print("Maior custo de missão realizada pela SpaceX:", costs_max)

#5
nome = np.unique(arr[1:, 1], return_counts=True)
for i in range(nome[0].size):
        print("Company:", nome[0][i], "Number of Missions:", nome[1][i])