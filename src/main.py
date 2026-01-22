import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


##-------------------------------------------1. Carga de datos y limpieza-----------------------------------------
file_path = "1.2 Vortex - Spotify/data/train.csv/train.csv"
df_spotify = pd.read_csv(file_path)
## print(df_spotify.head())

## Limpieza del DataFrame
print(df_spotify.isnull().sum()) ## Validacion de los nulos, por columna
print(f"Duplicados encontrados: {df_spotify.duplicated().sum()}")


##----------------------------------------2. Analisis de Correlacion entre variables----------------------------------------
## Matriz de correlacion
correlation_matrix = df_spotify.corr(numeric_only=True)

plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap ="coolwarm", linewidths=0.5)
plt.title("Matriz de Correlación de Variables - Spotify")
plt.show()
