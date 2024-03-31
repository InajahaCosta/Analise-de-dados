import numpy as np

#Condicionais

#seed perdi configurar para termos os mesmo numeros aleatorios em maquinas diferentes
np.random.seed(10)
#numeros aleatorios
arr = np.random.randint(1,11,15) # vai gerar 15 numeros aleatorios entre 1 e 10
#criando uma matriz de apartir do arr
mtz=arr.reshape(3,5)
print(mtz)

#extrair da matriz apenas numeros pares
cond = mtz%2==0
print(cond) #fala se e true ou false
print(mtz[cond]) # mostra somente oque são true

#mostrar os numeros que são maiores que a media da matriz
cond2 = mtz.mean() #pegando a media
print(cond2)
condMaior = mtz>mtz.mean() #pega somente os maior que a media
print(mtz[condMaior])