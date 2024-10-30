meses = ['enero','febrero','marzo','abril','mayo']
meses.append('junio')
#Acceso por indice
#print(meses[1])
#Acceso por indice negativo
#print(meses[-1])
""" segundoBimestre = meses[2:4]
primerTrimestre = meses[:3]
segundoTrimestre = meses[2:]
print(primerTrimestre)
print(segundoTrimestre)
print(segundoBimestre)

for mes in meses:
    print(mes)
 """

years = ["Enero 2023", "Mayo 2025", "Abril 2024", "Septiembre 2023", "Diciembre 2023"]

#update_years = []

""" for year in years:
    if year.endswith("2023"):
        new = year.replace("2023", "2024")
        update_years.append(new)
    else:
        update_years.append(year)
print(years)
print(update_years)
 """

update_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]
print(update_years)