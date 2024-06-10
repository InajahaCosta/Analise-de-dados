import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # criando um gráfico, plot simples e multiplo
# x = np.array([1, 2, 3, 4])
# y = x*2 #fazendo broadcasting
# y2 = x**2

# #colonado os valores do label
# plt.xlabel("Valores de X")
# plt.ylabel("Valores de Y")

# # estilo do grafico olhar slide para mais informaçõe
# # passando as codernadas do grafico x, y 
# # marcador circular o , marcador cruz x 
# # linhas pontinhadas : , linhas espaçada -- 
# # cor verde -> g, cor azul b
# # largura da linha -> linewidth=x (x = largura)
# # tamanho dos marcadores markersize=x (x = tamanho)
# plt.plot(x, y, 'o--g', 
#          x, y2, 'x:b',
#          linewidth=3, markersize=10)
 
# plt.show() # tem que ter esse comando para exibir o grafico

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #SUBPLOTS - todos na mesma tela, mais cada um em um plano cadersiano
# x = np.array([1, 2, 3, 4])
# y = x*2 #fazendo broadcasting
# y2 = x**2

# #plotando 2 graficos separados
# plt.subplot(1, 2, 1)
# plt.plot(x, y, 'o-r')
# plt.title('Linear')

# plt.subplot(1, 2, 2)
# plt.plot(x, y2, 'x--g')
# plt.title('Exponencial')
# plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scatter plot (grafico de dispersão)
# agora fazendo o uso de um dataset

df_paises= pd.read_csv('paises.csv', delimiter=';')
# print(df_paises.columns) # para mostrar o nome das colunas

#extraindo os 6 maiores paises do mundo
df_paises2= df_paises.nlargest(6, 'Area (sq. mi.)')
# #plotando esses paises
# plt.scatter(x=df_paises2['Country'],y=df_paises2['Area (sq. mi.)'])
#trazendo o tamanho da bolinha conforme o tamaho do renda per capita, cria o s para ficar melhor a visualização dividi tudo por um valor fixo
plt.scatter(x=df_paises2['Country'],y=df_paises2['Area (sq. mi.)'], s=df_paises2['GDP ($ per capita)']/100)
plt.show()