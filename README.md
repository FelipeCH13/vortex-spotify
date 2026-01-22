# 🎵 Spotify Insights: Análisis de la "Fórmula del Éxito"

## 📖 Descripción
Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre el conjunto de datos *Spotify Tracks Genre*. El objetivo es desglosar los atributos técnicos de audio (danceability, energy, valence, etc.) para identificar patrones que definen la **popularidad** de una canción y entender cómo varían estas métricas entre diferentes géneros musicales.

## 🛠️ Tecnologías Utilizadas
* **Python 3.x**
* **Pandas:** Procesamiento y limpieza de grandes volúmenes de datos.
* **Matplotlib & Seaborn:** Visualización de correlaciones y perfiles sonoros.
* **Numpy:** Cálculos estadísticos y manejo de matrices de datos.

## 🎼 Diccionario de Datos (Audio Features)
El dataset incluye métricas clave calculadas por los algoritmos de Spotify:
* **Popularity (0-100):** Basado en el número total de reproducciones y su actualidad.
* **Danceability (0-1):** Qué tan adecuada es una pista para bailar basándose en su ritmo y beat.
* **Energy (0-1):** Medida perceptiva de intensidad, actividad y volumen.
* **Valence (0-1):** Describe la positividad musical (Valores altos = Alegre, Valores bajos = Triste/Enojado).
* **Acousticness (0-1):** Confianza de que la pista es acústica (no eléctrica).
* **Tempo:** La velocidad general de la pista en pulsaciones por minuto (BPM).
* **Explicit (Boolean):** Indica si la pista contiene contenido explícito.

## 🧼 Limpieza y Preparación
*(Sección en desarrollo: Aquí detallaremos el tratamiento de nulos y duplicados una vez ejecutado el código inicial).*

## 📊 Preguntas de Negocio

### 1. ¿Cuáles son los atributos de audio que más influyen en la Popularidad?
Identificaremos mediante una **Matriz de Correlación** si la "energía" o la "capacidad de baile" tienen una relación directa con el éxito comercial.

### 2. ¿Existe un "Tempo" (BPM) ideal para ser popular?
Analizaremos la distribución de la velocidad de las canciones frente a su recepción por el público.

### 3. ¿Cómo afectan el contenido explícito y la duración a la recepción del público?
Evaluaremos si las canciones con contenido explícito tienen una ventaja estadística en el algoritmo de recomendación.

### 4. ¿Qué géneros son los más "felices" (High Valence) vs los más "enérgicos"?
Segmentaremos el perfil sonoro por `track_genre` para encontrar las diferencias entre categorías musicales.

---

## 🚀 Cómo ejecutar el proyecto
1. Clona este repositorio.
2. Asegúrate de tener el archivo `train.csv` en la carpeta raíz.
3. Instala las librerías necesarias:
   ```bash
   pip install pandas matplotlib seaborn numpy