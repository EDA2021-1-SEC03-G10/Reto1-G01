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
               'title': None,
               'cannel_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None}

    catalog['videos'] = lt.newList()
    catalog['title'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=comparetitle)
    catalog['cannel_title'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecannel_title)
    catalog['trending_date'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparetrending_date)
    catalog['cannel_title'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecannel_title)
    catalog['country'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecountry)
    catalog['views'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=compareviews)
    catalog['likes'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparelikes)
    catalog['dislikes'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparedislikes)

    return catalog


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento