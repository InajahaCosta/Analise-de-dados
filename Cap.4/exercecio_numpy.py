import numpy as np

# #1
# array = np.arange(0, 21, 1)
# print(array)

# #2
# array51 = np.arange(0, 51, 2)
# array100 = np.arange(100,50, -2)
# arrayConcate = np.concatenate([array51, np.sort(array100)])
# print("array 51" , array51)
# print("array 100" , array100)
# print(arrayConcate)

# #3
# print(np.flip(arrayConcate))

#4
# matriz1 = np.ones([3, 4])
# print(matriz1)
# matriz2 = matriz1.reshape(1,12)
# print(matriz2)

#5
matriz = np.zeros([2, 4])
numL = matriz.shape[0]
numC = matriz.shape[1]
arrayMult = np.zeros([numL*numC])
if arrayMult.size%2 == 0:
    print(arrayMult.size, "Vetor com numero PAR")
else:
    print(arrayMult.size, "Vetor com numero IMPAR")