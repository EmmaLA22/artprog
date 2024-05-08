import csv
from statistics import mode
def calcular_promedio_de_edad(archivo_csv):
    edades = []
    with open(archivo_csv, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:
                age = int(row[0])
                edades.append(age)
            except ValueError:
                # Ignorar líneas que no contengan un número en la primera columna
                pass
    
    if not edades:
        print("No se encontraron edades válidas en el archivo CSV.")
        return
    
    promedio = int( sum(edades) / len(edades))
    moda = mode (edades)
    print("El promedio de age es:", promedio)
    print("La moda de age es:", moda)



archivo_csv = "insurance.csv"  
calcular_promedio_de_edad(archivo_csv)
