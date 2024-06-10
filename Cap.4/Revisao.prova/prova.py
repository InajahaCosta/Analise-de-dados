import numpy as np

arr = np.loadtxt('brands.csv', delimiter= ';', dtype=str, encoding='utf-8')

#2 Mostre quantas marcas neste dataset possuem a palavra “Group” em seu nome;
group = (np.char.find(arr[:,0],'Group'))
print (arr[group, :0].size)

# 3 Mostre o nome e qual seria o valor de mercado das 5 primeiras empresas deste dataset em 2023 caso tivessem um aumento de 10%;
nomes = arr[1:6,0]
print("5 primeiras:", nomes)

# 4 Faça um Slicing no dataset e extraia apenas as colunas "nome da marca, por quem foi fundada e o ano que ela foi fundada". Em seguida, mostre apenas o nome das empresas fundadas depois dos anos 2000;
slice = arr[1:, :3]
maior2000 = ((arr[1:, 2].astype(int)) > 2000)
print(arr[1:,0][maior2000])


#5 Busque os diferentes anos em que as empresas foram fundadas. Em seguida, mostre em qual ano mais empresas abriram as portas.
anos = arr[1:, 2].astype(int)
print(anos)
