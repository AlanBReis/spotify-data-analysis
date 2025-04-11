import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

def get_top_tracks(country='BR'):
    results = sp.country_top_tracks(country_code=country)  # isso pode variar
    for item in results['tracks']:
        print(item['name'], "-", item['artists'][0]['name'])

get_top_tracks()
