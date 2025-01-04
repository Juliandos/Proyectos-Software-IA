import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import sqlite3

# clase para representar las caracteristicas de los episodios
class Episodio:
    def __init__(self, id, nombre, fecha, duracion, descripcion):
        """
        Representa un episodio de un podcast.

        :param id: ID del episodio.
        :param nombre: Nombre del episodio.
        :param fecha: Fecha de lanzamiento del episodio.
        :param duracion: Duración del episodio en minutos.
        :param descripcion: Descripción del episodio.
        """
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.duracion = duracion
        self.descripcion = descripcion

    def __str__(self):
        """
        Retorna una representación legible del episodio.
        """
        return (
            f"Id: {self.id}\n"
            f"Episodio: {self.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Duración: {self.duracion} minutos\n"
            f"Descripción: {self.descripcion}\n"
            "-------------------------------------------------------------------------"
        )

def obtener_claves_secretas():
    # Carga las claves de seguridad desde un archivo.env
    load_dotenv()

    # Configura tus credenciales
    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

    return client_id, client_secret

def iniciar_sesion_spotify(client_id, client_secret):
    # Autenticación
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp

# Ejemplo: Buscar una canción

# result = sp.search(q='canserbero', type='track', limit=5)
# for idx, track in enumerate(result['tracks']['items']):
#     print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")


# Dame el listado de episodios del potcast con ID 0hurw4EWdMieYjHA6aBmwg:
def extraer_episodios(potcast_id, sp):
    episodes = sp.show_episodes(potcast_id, limit=10)

    episodios = []
    for episode in episodes['items']:
        episodio = Episodio(
            id=episode['id'],
            nombre=episode['name'],
            fecha=episode['release_date'],
            duracion=episode['duration_ms'] // 60000,
            descripcion=episode['description']
        )
        episodios.append(episodio)

    return episodios

def conectar_db(archivo_db):
    """
    Conecta a la base de datos SQLite.
    
    :param archivo_db: Nombre del archivo de la base de datos SQLite.
    
    :return: Objeto de la base de datos SQLite.
    """
    try:
        conn = sqlite3.connect(archivo_db)
        return conn
    except sqlite3.Error as error:
        return None

def main():
    client_id, client_secret = obtener_claves_secretas()
    sp = iniciar_sesion_spotify(client_id, client_secret)
    
    episodios = extraer_episodios('0hurw4EWdMieYjHA6aBmwg', sp)

    for episodio in episodios:
        print(episodio)

main()