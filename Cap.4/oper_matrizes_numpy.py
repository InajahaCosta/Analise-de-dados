import numpy as np

#numeros aleatorios

#seed perdi configurar para termos os mesmo numeros aleatorios em maquinas diferentes
np.random.seed(10)
#numeros aleatorios
arr = np.random.randint(1,11,15) # vai gerar 15 numeros aleatorios entre 1 e 10
#criando uma matriz de apartir do arr
mtz=arr.reshape(3,5)
print(mtz)
print(mtz.sum(axis=1)) # faz a soma de cada linha axis = 1 soma na horizontal
print(mtz.sum(axis=1)[0]) # faz a soma de uma linha espeficica
print(mtz.sum(axis=0)) # faz a soma de cada coluna axis = 0 soma na vertical
print(mtz.sum(axis=0)[0]) # faz a soma de uma linha espeficica

#broadcastinf
print(mtz*0.5) #dividindo todos da matriz por 2