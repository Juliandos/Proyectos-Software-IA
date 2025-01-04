import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

# Configura tus credenciales
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Ejemplo: Buscar una canción
result = sp.search(q='canserbero', type='track', limit=5)
for idx, track in enumerate(result['tracks']['items']):
    print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")
