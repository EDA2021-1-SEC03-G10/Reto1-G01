"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos. Adicionalmente crea una lista vacia para guardar el título, el canal, 
    fecha de tendencia, pais, vistas, me gusta, no me gusta. Retorna el catalogo inicializado.
    title, cannel_title, trending_date, country, views, likes, dislikes
    """
    catalog = {'videos': None,
               'channels': None,
               'categories':None,
               'countries':None,
               'tags': None}

    catalog['videos'] = lt.newList()
    ############ Hace falta más adelante realizar las funciones de comparación e incluirlas aqui
    catalog['channels'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction = None)
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction = None)
    catalog['countries'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction = None)
    catalog['tags'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=None)


    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtienen los canales de cada video y se adicionan
    channel = video['channels']
    lt.addLast(catalog['channels'], channel)
    # Se obtienen los paises de cada video y se adicionan
    country = video['countries']
    lt.addLast(catalog['countries'], country)
    #Se obtienen los tags de cada video
    tags = video['tags'].split("|")
    # Cada tag, se crea en la lista de videos del catalogo, y se
    # crea un video en la lista de dicho tag (apuntador al video)
    for tag in tags:
        lt.addLast(catalog['tags'], tag)

def addCountry(catalog, countryname, video):
    """
    Adiciona un pais a lista de videos, la cual guarda referencias
    a los videos de dicho pais
    """
    countries = catalog['countries']
    poscountry = lt.isPresent(countries, countryname)

    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
        
    ##########newCountry: se debe realizar más adelante

    else:
        country  = newContry(countryname)
        lt.addLast(countries, country)
    lt.addLast(country['videos'], video)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento