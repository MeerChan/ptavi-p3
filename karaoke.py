#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import smallsmilhandler
from xml.sax import make_parser


class KaraokeLocal:
    def __init__(self, file):
        try:
            parser = make_parser()
            cHandler = smallsmilhandler.SmallSmilHandler()
            parser.setContentHandler(cHandler)
            parser.parse(open(file))
            self.lista = cHandler.get_tags()
        except FileNotFoundError:
            sys.exit("File not found")


    def __str__(self):
        todo_unido = ''
        for diccaux in self.lista:
            nombre_etiqueta = diccaux['etiqueta ']
            todo_unido += diccaux['etiqueta ']
            diccaux['etiqueta '] = 'etiqueta '
            for atributo, valor in diccaux.items():
                if atributo != diccaux['etiqueta '] and valor != "":
                    """
                    Concatena cada linea, el 0 es el atributo y el 1 es el valor
                    """
                    todo_unido += '\t'+'{0}="{1}"'.format(atributo, valor)
            todo_unido += '\n'
            diccaux['etiqueta '] = nombre_etiqueta
        return todo_unido


if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")

    karaoke = KaraokeLocal(file)
    print(karaoke)
