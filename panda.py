#linea para arrancar el código: python3 panda.py
# %%
import pandas as pd 
# %%
#carga el archivo 
df  = pd.read_csv ("housing.csv")

#muestra primeras ileras
print (df.head(3))

#MT = df [['longitude,latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity']].iloc[:2] #lo mismo al de despues pero mas caro
#print (df.head(12)[['longitude,latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity']]) #lo mismo pero mas barato

# Verificar la cantidad de datos y las variables
print("Cantidad de datos:", df.shape[0])
print("Variables:", df.shape[1])

# Identificar el tipo de variables
print(df.dtypes)

# Obtener estadísticas descriptivas
print(df.describe())

