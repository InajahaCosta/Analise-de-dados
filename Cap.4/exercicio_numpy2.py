import numpy as np

#1
np.random.seed(5) 
array = np.random.randn(10) #gerando o array com 10 numeros positivos e negativos
mult100 = 100*array # multiplicando o array por 100
arrInt= mult100.astype(int) # trazendo apenas a parte inteira dos numeros do array
print(arrInt)

#2
np.random.seed(10) 
mtz = np.random.randint(1, 50, 16).reshape(4, 4) #gerando a matriz 4x4 de 1 a 50
print(mtz)

# #Ex3
mediaLinha = mtz.mean(axis=1) #faz a media de cada linha (axis=1)
print(mediaLinha)
mediaColuna = mtz.mean(axis=0) #faz a media de cada coluna (axis=0)
print(mediaColuna) 
print("Maior valor referente a media da linha:",mediaLinha.max())
print("Maior valor referente a media da coluna:",mediaColuna.max())

#Ex4
aparicaoN = np.unique(mtz, return_counts=True) # tras a quantidade de vezes q os num se repetem
print(aparicaoN[1])
aparicao2 = aparicaoN[1] == 2 # tras a quantidade de vezes q os num se repetem 2 vezes
print(aparicaoN[0][aparicao2])