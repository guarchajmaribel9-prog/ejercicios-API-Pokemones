import requests

def obtener_pokemones():
    """
    Se conecta a la API pública de Pokémon, obtiene los primeros 20 Pokémon
    y muestra sus nombres en pantalla.
    """
    api_url = "https://pokeapi.co/api/v2/pokemon"
    
    try:
        # 1. Conectarse a la API y obtener los primeros 20 Pokémon
        # La API por defecto devuelve 20 resultados si no se especifica 'limit'
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP (4xx o 5xx)
        
        data = response.json()
        pokemones = data.get('results', []) # Obtiene la lista de Pokémon o una lista vacía si no existe

        # 3. Mostrar en pantalla únicamente el nombre de cada Pokémon
        print("Lista de Pokémon:")
        if pokemones:
            for i, pokemon in enumerate(pokemones):
                # El índice 'i' se usa para numerar la lista (empezando desde 0, sumamos 1)
                print(f"{i + 1}. {pokemon['name'].capitalize()}") # 'capitalize()' pone la primera letra en mayúscula
        else:
            print("No se encontraron Pokémon.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Pokémon: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para ejecutar el programa
obtener_pokemones()