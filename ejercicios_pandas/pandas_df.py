import pandas as pd
import numpy as np
from funciones import centimetros_metros, estandar_pais, standar_civil
resultado_df = pd.read_csv('respuestas.csv')

#Obtener los primeros 5 registros
#print(resultado_df.head())

#Obtener los ultimos 5 registros
#print(resultado_df.tail())

#Saber cuantas filas y columnas tiene el dataframe
#print(resultado_df.shape)

#Nos devuelve informacion sobre los campos y sus tipos
#print(resultado_df.info())

#Obtener el listado de columnas
# print(resultado_df.columns)
#print(resultado_df.describe())
df_edad = pd.to_numeric(resultado_df['edad'],errors='coerce')
edad_nan = resultado_df[df_edad.isna()][['nombre','edad']]
resultado_df.drop(79,axis=0,inplace=True)
#print(resultado_df[78:81])
resultado_df['edad'] = resultado_df['edad'].replace(r'\D','',regex=True).replace('',np.nan).astype(np.int16)
#print(resultado_df.info())

columnas_numericas = ['peso','altura','horas_redes_sociales','horas_estudio']

def valores_nan(data,campos):
    df_numericos = data[campos]
    #Dejar solo los valores numericos y quitar las cadenas de texto
    df_numericos = df_numericos.replace(r'[^\d.]','',regex=True).replace('',np.nan).astype(np.float16)
    #converir la calumna a numerico y dejar como NAN los que no se puedan convertir
    df_numericos[campos] = df_numericos[campos].apply(pd.to_numeric, errors='coerce')
    data[campos] = df_numericos[campos]
    df_nan = df_numericos[df_numericos.isna().any(axis=1)]
    #Imprimir cuantos valores NAN hay por campo
    #print(resultado_df.isna().sum())


valores_nan(resultado_df,columnas_numericas)
df_resultado_sin_nan = resultado_df.dropna()
#print(df_resultado_sin_nan.isna().sum())


"""
Limpiar datos de Altura
"""
print(df_resultado_sin_nan[df_resultado_sin_nan['altura']>3][['nombre','altura']])

#Convertir alturas que estan en centimetros a metros
df_resultado_sin_nan['altura'] = df_resultado_sin_nan['altura'].apply(centimetros_metros)
df_resultado_sin_nan['altura'] = df_resultado_sin_nan['altura'].round(2)
#print(df_resultado_sin_nan['altura'].head())
#df_resultado_sin_nan.to_csv('Respuestas_procesadas.csv',index=False)


#Estandarizar nombre de paises
#Obgtener cuantos paises unicos hay
print(df_resultado_sin_nan['pais'].unique())
#print(df_resultado_sin_nan['pais'].value_counts())
df_resultado_sin_nan['pais'] = df_resultado_sin_nan['pais'].apply(estandar_pais)
print(df_resultado_sin_nan['pais'].value_counts())

#cambiar estado civil dependiendo del genero
df_resultado_sin_nan['estado_civil'] = df_resultado_sin_nan.apply(standar_civil, axis=1)

df_resultado_sin_nan.to_csv('Respuestas_procesadas.csv',index=False)