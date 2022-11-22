from collections import namedtuple
import csv

Juego = namedtuple('Juego', 'rank, name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales')
''''
EL ELEMNTO MAS REPETIDO 
MOST COMMON CON COUNTER
lista=[1,1,2,2,2,2,3,3,4]
contador=Counter(lista)
mas_repetido= contador.most_common(1)

DEVUELVE: una lista de tupla, donde el primer elemento es el elemento que más se repite y el segundo elemento es el número de veces que se repite
'''
def lee_juegos(nom_fichero):
    lista=[]
    with open(nom_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for rank, name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales in lector:
            lista.append(Juego(int(rank), name, platform, int(year), genre, publisher, float(NA_sales), float(EU_sales), float(JP_sales), float(other_sales), float(global_sales)))
    return lista

def num_juegos_mas_ventasJP(lista_juegos):
    cont=0
    for l in lista_juegos:
        if l.JP_sales>l.NA_sales:
            cont+=1
    return cont

def juegos_distribuidora_anyo(lista_juegos, publisher, anyo):
    return [l.name for l in lista_juegos if l.publisher==publisher and l.year==anyo]

def num_distribuidoras(lista_juegos):
    return len({l.publisher for l in lista_juegos})

def juego_mas_antiguo(lista_juegos):
    dicc=dict()
    for l in lista_juegos:
        clave=l.year
        años=[l.year]
        if clave not in dicc:
            dicc[clave]=[l.name]
        else:
            dicc[clave].append(l.name)
        año_menor=sorted(años)[0]
    return dicc[año_menor]

def genero_mas_presente(lista_juegos):
    dicc=dict()
    for l in lista_juegos:
        clave=l.genre
        if clave not in dicc:
            dicc[clave]=1
        else:
            dicc[clave]+=1

    return  max(dicc, key=lambda x: dicc[x])

def genero_mas_ventas(lista_juegos):
    return max([l for l in lista_juegos], key=lambda x:x.global_sales).genre

def num_juegos_palabra(lista_juegos, palabra):
    return len([l for l in lista_juegos if palabra in l.name ])

def mayor_dif_NA_EU(lista_juegos):
    dicc=dict()
    for l in lista_juegos:
        clave= l.name
        if clave not in dicc:
            dicc[clave]=[abs(l.EU_sales-l.NA_sales)]
        else:
            dicc[clave].append(abs(l.EU_sales-l.NA_sales))

    return max(dicc, key=lambda x: dicc[x])

    '''
    devuelve una lista de tuplas formadas por un año y el global de ventas de ese año para los videojuegos que salieron ese año. Ordenada de mayor a menor volumen de venta.
    '''
