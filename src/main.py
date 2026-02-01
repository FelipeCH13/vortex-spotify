import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import os

# Creamos la carpeta 'images' si no existe
if not os.path.exists('images'):
    os.makedirs('images')


##-------------------------------------------0. Carga de datos y limpieza-----------------------------------------
file_path = "1.2 Vortex - Spotify/data/train.csv/train.csv"
df_spotify = pd.read_csv(file_path, index_col = 0) ##Se omite la primera columna que funciona como indice
## print(df_spotify.head())

## Limpieza del DataFrame
print(df_spotify.isnull().sum()) ## Validacion de los nulos, por columna
print(f"Duplicados encontrados: {df_spotify.duplicated().sum()}") ##Conteo de duplicados


##----------------------------------------1. Analisis de Correlacion entre variables----------------------------------------
## Matriz de correlacion
correlation_matrix = df_spotify.corr(numeric_only=True) ##Este parametro permite tener en cuenta unicamente variables numericas

plt.figure(figsize=(12,10)) ##Se indica el ancho y el alto de la imagen a generar
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap ="coolwarm", linewidths=0.5)
## annot: Permite visualizar el numero exacto de la correlacion en cada cuadro
## fmt: Indica que solo deben ser dos deciales
## cmap: Define la paleta de colores utilizada en el mapa
## linewidths: Permite agregar una linea blanca entre los cuadros
plt.title("Matriz de Correlación de Variables - Spotify")
## Este es el titulo de la matriz
##plt.show()
## Mostramos el grafico
plt.title("Matriz de Correlación de Variables - Spotify")
plt.savefig('images/matriz_correlacion.png', dpi=300, bbox_inches='tight')

##----------------------------------------1.1 Prueba Analisis de Correlacion entre variables filtrando por genero----------------------------------------
# Verificamos los valores únicos de 'explicit' en Classical
print(df_spotify[df_spotify['track_genre'] == 'classical']['explicit'].value_counts())

generos = df_spotify['track_genre'].unique()
print(generos)

df_pop = df_spotify[df_spotify['track_genre'] == 'classical']
corr_pop = df_pop.corr(numeric_only = True)
plt.figure(figsize=(12,10))
sns.heatmap(corr_pop, annot=True, fmt=".2f", cmap ="coolwarm", linewidths=0.5)
plt.title("Matriz de Correlación de Variables - Genero Classical")
# plt.show()
plt.title("Matriz de Correlación de Variables -  Genero Classical")
plt.savefig('images/matriz_correlacion_classical.png', dpi=300, bbox_inches='tight')

##-----------------------------------------1.2 Analisis de Correlacion entre variables para todos los generos------------------------------------

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

## --------------------------------------------- 1.3 Grafico de dispersion entre la variable energia y popularidad: Genero Classical-----------------

# Filtramos los datos
df_classical = df_spotify[df_spotify['track_genre'] == 'classical']

# Creamos un gráfico de dispersión con una línea de tendencia
plt.figure(figsize=(10, 6))
sns.regplot(data=df_classical, x='energy', y='popularity', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relación: Energía vs Popularidad en Música Clásica')
# plt.show()
plt.title("Relación: Energía vs Popularidad en Música Clásica")
plt.savefig('images/relacion_energia_popularidad.png', dpi=300, bbox_inches='tight')

##-----------------------------------------------2. Histograma para verificar la distribucion de las canciones segun el tempo----------------------------

plt.figure(figsize=(10,6))
sns.histplot(data=df_spotify, x="tempo", kde=True) 
plt.title('Distribución Global del Tempo (BPM) en Spotify')
plt.xlabel('Tempo (BPM)')
plt.ylabel('Cantidad de Canciones')
# plt.show()
plt.title("Histograma distribucion Tempo")
plt.savefig('images/histograma_tempo.png', dpi=300, bbox_inches='tight')

##-----------------------------------------------2.1 Verificar el comportamiento de popularidad segun los BPMs----------------------------

df_spotify['tempo_agrupado'] = (df_spotify['tempo'] / 10).round() * 10
df_tempo_popularity = df_spotify.groupby('tempo_agrupado')['popularity'].agg(['mean','count']).reset_index()

plt.figure(figsize=(12,6))
sns.scatterplot(data=df_tempo_popularity, x='tempo_agrupado', y='mean', size='count', sizes=(20, 500), alpha=0.6)
sns.lineplot(data=df_tempo_popularity, x='tempo_agrupado', y='mean', alpha=0.4)
plt.title('Popularidad Promedio y Volumen de Canciones por Tempo')
plt.xlabel('Tempo (BPM)')
plt.ylabel('Popularidad Promedio')
plt.grid(True, alpha=0.3)
# plt.show()
plt.title("Comportamiento BPMs segun la popularidad")
plt.savefig('images/tempo_popularidad.png', dpi=300, bbox_inches='tight')


## ------------------------------------------------ 3. ADN del exito ---------------------------------------------------
variables_adn = ['danceability', 'energy', 'valence', 'acousticness', 'speechiness', 'instrumentalness']
df_top_songs = df_spotify[df_spotify['popularity'] > 80][variables_adn].mean()
df_bottom_songs = df_spotify[df_spotify['popularity'] < 20][variables_adn].mean()

# df_sorted = df_spotify.sort_values(by='popularity', ascending=False)
# top_100 = df_sorted.head(10000)
# bottom_100 = df_sorted.tail(10000)
# top_profile = top_100[variables_adn].mean()
# bottom_profile = bottom_100[variables_adn].mean()

print("--- Perfil Top ---")
print(df_top_songs)
print("\n--- Perfil Bottom ---")
print(df_bottom_songs)

spider = go.Figure()

spider.add_trace(go.Scatterpolar(
    r = df_top_songs.values, # Define la distancia desde el centro para cada variable
    theta = variables_adn, # Define los nombres de los ejes en el círculo
    fill = 'toself', # Cierra y rellena el área del polígono
    name = 'Top Songs (>80 Popularidad)' # Etiqueta para la leyenda
))

spider.add_trace(go.Scatterpolar(
    r = df_bottom_songs.values, # Valores promedio del grupo menos popular
    theta = variables_adn, # Mismos ejes para permitir la comparación
    fill = 'toself', # Crea la segunda capa de color
    name = 'Bottom Songs (<20 Popularidad)' # Etiqueta comparativa
))

spider.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True, # Muestra la escala numérica del radio
            range=[0, 1] # Fija los límites de 0 a 1 para normalizar la vista
        )),
    showlegend=True, # Muestra el cuadro de convenciones
    title="ADN del Éxito: Top vs Bottom Songs" # Título principal del gráfico
)

# El renderer 'vscode' fuerza la aparición de la gráfica dentro del editor
# spider.write_html("resultado_adn.html")
spider.write_image("images/resultado_adn.png")