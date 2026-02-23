"""

import pandas as pd
Datos = {"nombre": ["pedro","juan","angelo"], "edad": [20,30,40]}
df = pd.DataFrame(Datos)
print(df)

df["nombre"]

import pandas as pd

df_empleados = {"nombre": ["jose","diego","juanes","guillermo"],
            "edad": [20,30,40,50]}
df = pd.DataFrame(df_empleados)
edades = df["edad"]
print(edades)
print(type(edades))
"""
import pandas as pd
df_empleados = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Carlos"],
    "edad": [30, 25, 40]
})

shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index

print(shape_df)
print(columns_df)
print(index_df)