# Descripcion: Carga los datos olimpicos, realiza la limpieza basica,
# crea las columnas IMC y medalla, y muestra un resumen general.

import pandas as pd

def cargar_y_preparar_datos():
    # Cargar los dos archivos CSV desde la carpeta data
    df_atletas = pd.read_csv('data/athlete_events.csv')
    df_regiones = pd.read_csv('data/noc_regions.csv')

    # Crear variable IMC
    df_atletas['IMC'] = df_atletas['Weight'] / ((df_atletas['Height'] / 100) ** 2)

    # Unir ambos dataframes usando NOC (left join para no perder atletas)
    df_merged = pd.merge(df_atletas, df_regiones, on='NOC', how='left')

    # Crear variable binaria medalla (1 si gano, 0 si no gano)
    df_merged['medalla'] = df_merged['Medal'].notna().astype(int)

    return df_merged

if __name__ == '__main__':
    df = cargar_y_preparar_datos()
    print("Total de registros cargados:", len(df))
    print("Total de atletas unicos:", df['ID'].nunique())
    print("\nTop 5 paises con mas medallas:")
    print(df.groupby('region')['medalla'].sum().sort_values(ascending=False).head(5))