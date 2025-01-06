#Proyecto 1 - Extracción de info de canales de spotity

## 1. Módulo - Extracción de informacion de episodios de un potcast

Este módulo Python permite extraer información de los episodios de un potcast en spotify

### 1.1 Instalción

### 1.1.1 Creation virtual environment
Use this to create a virtual environment

```bash
    python -m venv venv
```

### 1.1.2 Activate virtual environment
Use this to activate the virtual environment

Linux/Mac OS:

```bash
    source venv/bin/activate
    ```

Windows:

```bash
    venv\Scripts\activate
```

### 1.1.3 Install dependencies

To install dependencies from the virtual environment use the following command:

```bash
pip install -r requirements.txt
```

### 1.2 Execution

to execute the module we use the following command:

```bash
python main.py -i "768GVwxeh1o6kD5bD0qJeJ" -d "Db_extraer_libros_spotify.db"
```

The `-i` flag is used to specify the spotify potcast id

The `-d` flag is used to specify the database file where the extracted information will be stored.

once we have executed the comand a database will be created and stored the potcast episodes into the database.