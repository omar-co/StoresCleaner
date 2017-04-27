import pandas as pd
import time
print('Leyendo store.xlsx')
df2 = pd.read_excel('store.xlsx', 0)
print('store.xlsx cargado en memoria')

print('Filtrando Columnas')
df2 = df2[['Stores ID', '# Sucursal Cliente',
           'Cadena', 'Formato', 'Nombre Tienda', 'Region', 'Zona', 'Area Nielsen', 'Estatus de Tienda', 'Canal']]

print('Filtrando Regiones')
df3 = df2[(df2.Region.str.contains(r'^(region)\s\d{1,2}$') | df2.Region.str.contains('^DPP1$'))]

print('Eliminando Duplicados')
df3['Stores ID'].drop_duplicates()

print('Generando stores_limpio_xlsx')
print('Guardando stores_limpio.xlsx')
df3.to_excel('stores_limpio.xlsx', 'stores', index=None)

print(str(df3['Stores ID'].count()) + ' Tiendas Filtradas Correctamente')
time.sleep(2)
