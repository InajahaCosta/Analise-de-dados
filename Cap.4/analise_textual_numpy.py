import numpy as np

#Analise textual
#char
arr = np.array(['Pedro', 'Arthur', 'Ana', 'Maciel'])
result = np.char.find(arr, 'a')
print(result) #vai printar a posição que esta a letra a
cond= np.char.find(arr, 'a') >=0
print(arr[cond]) #agora trazendo o nome das pessoas que possuem a letra "a" no nome