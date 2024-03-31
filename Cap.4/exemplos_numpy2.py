import numpy as np

#numeros aleatorios
#Randon

arr = np.random.randint(1,11,15) # vai gerar 15 numeros aleatorios entre 1 e 10
print(arr)

#seed perdi configurar para termos os mesmo numeros aleatorios em maquinas diferentes
np.random.seed(10)
arr = np.random.randint(1,11,15) # vai gerar 15 numeros aleatorios entre 1 e 10
print(arr)

# extraindo elemntos unicos
print(np.unique(arr))
print(np.unique(arr,return_counts=True)) #função tras a quantidade de vezes q os num se repetem