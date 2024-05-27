import numpy as np
import pandas as pd

# #SERIES
# dic = { 'a':10, 'b':20, 'c':30} # dicionario
# s = pd.Series(dic) # criando um serie
# print(s) # printando toda a serie
# print('elemento a:',s['a'], '\n') #printando somente um valor da serie
# print('elemento b e c :\n',s[['b', 'c']],'\n')
# print('printando valores maiores que 10:\n',s[s>10],'\n')

# # operação entre series
# s2 = pd.Series(data=[20,30,40],
#                index=['b', 'c', 'd'])

# # como a sires s2 NAO tem A e D ele entende como nao existe Nan
# print('somando das duas series:\n', s + s2,'\n')

# # agora tratando o vazio como 0
# print('somando das duas series, considerando o 0:\n', s.add(s2, fill_value=0),'\n')


# #DATAFRAME
# #estruturando um datafarme
# df = pd.DataFrame(
#     columns=['x', 'y', 'z'],
#     index= ['A', 'B', 'C'],
#     data=np.random.randint(1,50, [3,3])
# )

# print('retorno do datafarme\n', df,'\n')
# #fazendo slicing usando loc, pegando apenas alguma parte do datafarme
# print('printando informações as linhas B,C:\n',df.loc[['B','C'],['x','y','z']],'\n') # primeiro passa as linhas depois as colunas

# #usando iloc
# print('usando o iloc para trazer info linhas B,C:\n',df.iloc[1:, :]) # a partir da primeira linha todas as colunas 

#carregando arquivos diferentes no pandas pd.read_(formado do arquivo)
df2= pd.read_csv('paises.csv', delimiter=';')
print(df2)
print('Trazendo o resultado da coluna Country: \n', df2['Country'], '\n')
print('Apenas os 3 primeiros paises \n', df2.head(3), '\n')
print('Apenas os 3 ultimos paises \n', df2.tail(3))