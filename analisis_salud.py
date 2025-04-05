# Ejercicio: Identificación de población, muestra y variables

import pandas as pd

# Cargar los datos
df = pd.read_csv("datos_salud.csv")

# Mostrar las primeras filas
df.head()

# Crear tabla resumen de variables
tabla_variables = pd.DataFrame({
    "Variable": ["id", "edad", "sexo", "grupo_sanguineo", "nivel_socioeconomico",
                 "peso_kg", "vacunado_covid", "frecuencia_visita_medico", "departamento"],
    "Tipo de variable": ["Cuantitativa discreta", "Cuantitativa continua", "Cualitativa nominal",
                         "Cualitativa nominal", "Cualitativa ordinal", "Cuantitativa continua",
                         "Cualitativa dicotómica", "Cuantitativa discreta", "Cualitativa nominal"],
    "Escala de medición": ["Razón", "Razón", "Nominal", "Nominal", "Ordinal", "Razón",
                           "Nominal", "Razón", "Nominal"]
})

tabla_variables
