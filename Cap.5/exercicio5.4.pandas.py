import numpy as np
import pandas as pd

df_paises= pd.read_csv('paises.csv', delimiter=';')

#1-a
paisesOceania = df_paises[df_paises['Region'].str.strip() == 'OCEANIA']
paisesOceania = paisesOceania[['Country']]
print("Paises da Oceania:")
print(paisesOceania)

#b
numero_paisesOceania = len(paisesOceania)
print("Numero de paises da Oceania: ", numero_paisesOceania)

#2
media_literacy = df_paises['Literacy (%)'].mean()
print(f"Taxa de alfabetização: {media_literacy:.2f}%")

#3
max_population = df_paises['Population'].max()
pais_max_population = df_paises[df_paises['Population'] == max_population][['Country', 'Region']]
print("País com a maior população:")
print(pais_max_population)

#4
paises_sem_costa = df_paises[df_paises['Coastline (coast/area ratio)'] == 0][['Country']]
paises_sem_costa.to_csv('Coast.csv', sep=';', index=False)
print("Países que não possuem costa marítima:")
print(paises_sem_costa)