import numpy as np
def centimetros_metros(valor):
    if valor >=3:
        altura = valor /100
        if altura >= 3 or altura < 1:
            altura = np.nan
        return altura
    return valor

def estandar_pais(pais):
    corrections = {
        "guatrmala":'guatemala',
        "perú, pero resido en argentina":"perú",
        "guate":"guatemala",
        "perú":"perú",
        "peru":"perú",
        "méxico":"méxico",
        "mexico":"méxico",
        "el salvador":"el salvador",
        "republica dominicana":"republica dominicana"
    }
    pais = pais.strip().lower()
    pais_title= corrections.get(pais,pais)
    return pais_title.title()

def standar_civil(row):
    corrections = {
        ('Solter@','Masculino'):'Soltero',
        ('Solter@','Femenino'):'Soltera',
        ('Casad@','Femenino'):'Casada',
        ('Casad@','Masculino'):'Casado'}
    return corrections.get((row['estado_civil'],row['genero']),row['estado_civil'])  