import pandas as pd

file_path = "1.2 Vortex - Spotify/data/train.csv/train.csv"

df_spotify = pd.read_csv(file_path)

print(df_spotify.head())

