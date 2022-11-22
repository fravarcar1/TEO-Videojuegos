from videojuegos import *

REGISTRO = lee_juegos('./data/videojuegos.csv')

def test_lee_juegos(registro):
    print("        LECTURA")
    print(f"El número total de registros leídos son {len(registro)} registros")
    print(f"\nLos tres primeros registros son:\n{registro[:3]}")
    print(f"\nLos tres últimos registros son:\n {registro[-3:]}")

def test_num_juegos_mas_ventasJP(registro):
    print("             NÚMERO JUEGOS MÁS VENTAS JAPÓN")
    print(f"Hay {num_juegos_mas_ventasJP(registro)} videojuegos que han tenido más ventas en Japón que en Norte América")

def test_juegos_distribuidora_anyo(registro,publishier,anyo):
    print("               VIDEOJUEGOS DISTRIBUIDORA Y AÑO DADO")
    print(f"Los videojuegos de la distribuidora {publishier} en el año {anyo} son: \{juegos_distribuidora_anyo(registro,publishier,anyo)}")
def test_num_distribuidoras(registro):
    print("        Número de distribuidoras")
    print(f"El número de distribuidoras distintas es: \n{num_distribuidoras(registro)}")

def test_juego_mas_antiguo(registro):
    print("         JUEGOS MÁS ANTIGUOS")
    print(f"Los juegos más antiguos son:{juego_mas_antiguo(registro)}")

def test_genero_mas_presente(registro):
    print("       GÉNERO MÁS PRESENTE")
    print(f"El género más presente es: {genero_mas_presente(registro)}")

def test_genero_mas_ventas(registro):
    print("        GÉNERO MÁS VENTAS")
    print(f"El género con más ventas es: {genero_mas_ventas(registro)}")

def test_num_juegos_palabra(registro,palabra):
    print("         NÚMERO DE JUEGOS CON PALABRA")
    print(f"El número de juegos que contiene la palabra {palabra} es: \n{num_juegos_palabra(registro,palabra)}")

def test_mayor_dif_NA_EU(registro):
    print(" MAYOR DIFERENCIA EUROPA Y NORTEAMÉRICA")
    print(f"El videojuego con una mayor diferencia de ventas entre Europa y Norteamérica es: \n{mayor_dif_NA_EU(registro)}")
#####LLAMADA A LA FUNCIÓN

#test_lee_juegos(REGISTRO)
#test_num_juegos_mas_ventasJP(REGISTRO)
#test_juegos_distribuidora_anyo(REGISTRO,'Nintendo',2006)
#test_num_distribuidoras(REGISTRO)
#test_juego_mas_antiguo(REGISTRO)
#test_genero_mas_presente(REGISTRO)
#test_genero_mas_ventas(REGISTRO)
#test_num_juegos_palabra(REGISTRO,'Wii')
test_mayor_dif_NA_EU(REGISTRO)