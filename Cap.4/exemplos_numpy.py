import numpy as np

# 1 dimensão
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

# 2 dimensões 
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

matriz5 = np.ones([5, 5])
print(matriz5)

arr = np.zeros(10)
print(arr)

# arange
arr = np.arange(20, 30 , 1)
print(arr)

# reshape (transformando o arange em matriz)
arrMatriz = arr.reshape(5, 2)
print(arrMatriz)

# reshape (transformando a matriz em arange)
arrArange = arrMatriz.reshape(1,10)
print(arrArange)


# Operações entre Numpy Arrays
jan = np.arange (20, 30 , 1)
fev = np.arange (40, 50 , 1)

print(jan)
print(fev)

# operação elemento a elemento
print(jan+fev)
print(np.concatenate([jan, fev]))
# usando o reshape
arrReshape = np.concatenate([jan, fev]).reshape(5, 4)
print(arrReshape)
# tamanho de um np array
print(jan.size)
# dimensão de um np array
print(jan.ndim)
# Shape de um np array
print(jan.shape)
print(arrReshape.shape)