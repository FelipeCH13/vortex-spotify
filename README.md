### 📊 Diccionario de Datos Completo y Guía de Interpretación

| Variable | Descripción | Tipo | Interpretación para el Análisis |
| :--- | :--- | :--- | :--- |
| **Identificadores** | | | |
| `artists` | Artista(s) de la pista. | Cadena | Útil para identificar qué artistas dominan el éxito. |
| `album_name` | Nombre del álbum. | Cadena | Permite ver si ciertos álbumes tienen éxito uniforme. |
| `track_name` | Nombre de la canción. | Cadena | Identificador único de la obra. |
| `track_genre` | Género de la pista. | Cadena | **Variable de Segmentación:** Para comparar estilos. |
| **Métricas de Éxito** | | | |
| `popularity` | Popularidad (0-100). | Entero | **Variable Objetivo:** El "éxito" que queremos explicar. |
| **Atributos de Audio** | | | |
| `danceability` | Aptitud para el baile (0-1). | Flotante | > 0.7 indica ritmos muy estables y bailables. |
| `energy` | Intensidad y actividad (0-1). | Flotante | Representa qué tan "fuerte" o rápida se siente la pista. |
| `loudness` | Sonoridad promedio (dB). | Flotante | Volumen físico. Valores más altos (ej. -5) son más fuertes. |
| `valence` | Positividad (0-1). | Flotante | Mide la "alegría" (Cercano a 1) vs "tristeza" (Cercano a 0). |
| `tempo` | Velocidad en BPM. | Flotante | El pulso de la canción; clave para el ritmo. |
| `acousticness` | Nivel acústico (0-1). | Flotante | 1.0 indica alta probabilidad de ser una pista acústica. |
| `instrumentalness` | Probabilidad instrumental. | Flotante | > 0.5 sugiere que la canción no tiene voces. |
| `speechiness` | Presencia de habla (0-1). | Flotante | > 0.6 indica que es casi puro contenido hablado. |
| `liveness` | Grabación en vivo (0-1). | Flotante | Detecta la presencia de público en la grabación. |
| **Detalles Técnicos** | | | |
| `duration_ms` | Duración en ms. | Entero | Longitud de la pista; útil para ver tendencias de tiempo. |
| `explicit` | Contenido explícito. | Booleano | Determina si el lenguaje fuerte afecta el alcance. |
| `key` | Tonalidad (0-11). | Entero | La nota base de la canción (C, C#, D, etc.). |
| `mode` | Modalidad (0 o 1). | Entero | 1 = Mayor (más brillante), 0 = Menor (más sombrío). |
| `time_signature` | Compás de la pista. | Entero | Número de pulsos por compás (ej. 4/4). |