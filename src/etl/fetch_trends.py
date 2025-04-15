import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

playlist_id = "5gJ6V0oZhIR52XOf6ruGw7"

# Caminho absoluto para a raiz do projeto
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SAVE_DIR = os.path.join(ROOT_DIR, "data", "processed")

def get_playlist_tracks(playlist_id):
    try:
        results = sp.playlist_items(playlist_id, market='BR')
        tracks = []

        for item in results['items']:
            track = item['track']
            if track:
                track_data = {
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'album': track['album']['name'],
                    'popularity': track['popularity'],
                    'duration_ms': track['duration_ms'],
                    'id': track['id']
                }
                tracks.append(track_data)

        return pd.DataFrame(tracks)

    except Exception as e:
        print(f"Erro ao buscar músicas da playlist: {e}")
        return pd.DataFrame()

df = get_playlist_tracks(playlist_id)

if not df.empty:
    print(f"{len(df)} músicas encontradas.")
    print(df.head())

    os.makedirs(SAVE_DIR, exist_ok=True)
    file_path = os.path.join(SAVE_DIR, "playlist.csv")

    df.to_csv(file_path, index=False)
    print(f"Arquivo salvo em: {file_path}")
else:
    print("Nenhuma música encontrada.")
