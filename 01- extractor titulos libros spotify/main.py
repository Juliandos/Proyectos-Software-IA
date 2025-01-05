import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import sqlite3

# clase para representar las caracteristicas de los episodios
class Episodio:
    def __init__(self, book_id, name, release_date, duration_ms, description):
        """
        Representa un episodio de un podcast.

        :param id: ID del episodio.
        :param nombre: Nombre del episodio.
        :param fecha: Fecha de lanzamiento del episodio.
        :param duracion: Duración del episodio en minutos.
        :param descripcion: Descripción del episodio.
        """
        self.book_id = book_id
        self.name = name
        self.release_date = release_date
        self.duration_ms = duration_ms
        self.description = description

    def __str__(self):
        """
        Retorna una representación legible del episodio.
        """
        return (
            f"Id: {self.book_id}\n"
            f"Episodio: {self.name}\n"
            f"Fecha: {self.release_date}\n"
            f"Duración: {self.duration_ms} minutos\n"
            f"Descripción: {self.description}\n"
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

# Dame el listado de episodios del potcast con ID 0hurw4EWdMieYjHA6aBmwg:
def extraer_episodios(potcast_id, sp):
    episodes = sp.show_episodes(potcast_id, limit=10)

    episodios = []
    for episode in episodes['items']:
        episodio = Episodio(
            book_id=episode['id'],
            name=episode['name'],
            release_date=episode['release_date'],
            duration_ms=episode['duration_ms'] // 60000,
            description=episode['description']
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

def almacenar_episodio(conn, episodio: Episodio):
    """
    Almacena un episodio en la base de datos SQLite.
    
    :param conn: Objeto de la base de datos SQLite.
    :param episodio: Objeto Episodio con la información del episodio.
    """
    sql = """
        INSERT INTO episodio (book_id, name, release_date, duration_ms, description)
        VALUES (?,?,?,?,?)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql,
        (episodio.book_id, episodio.name, episodio.release_date, episodio.duration_ms, episodio.description))
        conn.commit()
    except sqlite3.Error as error:
        print("Error al almacenar el episodio:", error)

def main():
    client_id, client_secret = obtener_claves_secretas()
    sp = iniciar_sesion_spotify(client_id, client_secret)
    
    episodios = extraer_episodios('0hurw4EWdMieYjHA6aBmwg', sp)

    if len(episodios):
        conexion = conectar_db('Db_extraer_libros_spotify.db')
        for episodio in episodios:
            almacenar_episodio(conexion, episodio)
        conexion.close()
    else:
        print("No se pudieron extraer episodios del podcast")


main()

# Ejemplo: Buscar una canción

# result = sp.search(q='canserbero', type='track', limit=5)
# for idx, track in enumerate(result['tracks']['items']):
#     print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")