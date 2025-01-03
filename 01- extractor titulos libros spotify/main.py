import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura tus credenciales
client_id = "52b59a52c48b4780b87d8b4e61932f73"
client_secret = "3b7f1e46084b4338a68601ff3c654503"

# Autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Ejemplo: Buscar una canción
result = sp.search(q='Imagine Dragons', type='track', limit=5)
for idx, track in enumerate(result['tracks']['items']):
    print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")
