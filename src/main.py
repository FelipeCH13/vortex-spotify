import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


##-------------------------------------------1. Carga de datos y limpieza-----------------------------------------
file_path = "1.2 Vortex - Spotify/data/train.csv/train.csv"
df_spotify = pd.read_csv(file_path, index_col = 0)
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

##----------------------------------------3. Analisis de Correlacion entre variables por genero----------------------------------------
generos = df_spotify['track_genre'].unique()
print(generos)

df_pop = df_spotify[df_spotify['track_genre'] == 'pop']
corr_pop = df_pop.corr(numeric_only = True)
plt.figure(figsize=(12,10))
sns.heatmap(corr_pop, annot=True, fmt=".2f", cmap ="coolwarm", linewidths=0.5)
plt.title("Matriz de Correlación de Variables - Spotify")
plt.show()

# Creamos una lista para guardar los resultados
resultados = []

# Iteramos por cada género único
for genero in df_spotify['track_genre'].unique():
    df_gen = df_spotify[df_spotify['track_genre'] == genero]
    # Calculamos la correlación solo para este género
    corr_matrix = df_gen.corr(numeric_only=True)
    
    if 'popularity' in corr_matrix.columns:
        # Buscamos la correlación más alta con popularidad (excluyendo popularidad misma)
        corrs = corr_matrix['popularity'].drop('popularity')
        max_corr = corrs.abs().max()
        variable = corrs.abs().idxmax()
        
        resultados.append({'genero': genero, 'variable': variable, 'valor': corrs[variable]})

# Convertimos a DataFrame y ordenamos para ver los más altos
df_resultados = pd.DataFrame(resultados).sort_values(by='valor', ascending=False)
print(df_resultados.head(10))


# Filtramos los datos
df_classical = df_spotify[df_spotify['track_genre'] == 'classical']

# Creamos un gráfico de dispersión con una línea de tendencia
plt.figure(figsize=(10, 6))
sns.regplot(data=df_classical, x='energy', y='popularity', 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

plt.title('Relación: Energía vs Popularidad en Música Clásica')
plt.show()