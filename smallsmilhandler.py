#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.dicc = {'root-layout': ['width', 'height', 'background-color'],
                     'region': ['id', 'top', 'bottom', 'left', 'right'],
                     'img': ['src', 'region', 'begin', 'dur'],
                     'audio': ['src', 'begin', 'dur'],
                     'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        diccaux = {}
        if name in self.dicc:
            diccaux['etiqueta '] = name
            for atributo in self.dicc[name]:
                diccaux[atributo] = attrs.get(atributo, '')
                """
                escribe el diccionario en una lista, cada elemento
                es la etiqueta con los atributos que tiene y su contenido
                """
            self.lista.append(diccaux)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    lista = cHandler.get_tags()
    print(lista)
