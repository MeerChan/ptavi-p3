#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import urllib.request
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
                    Concatena cada linea, el 0 es el atributo y el 1es el valor
                    """
                    todo_unido += '\t'+'{0}="{1}"'.format(atributo, valor)
            todo_unido += '\n'
            diccaux['etiqueta '] = nombre_etiqueta
        return todo_unido

    def do_json(self, file):
        file_json = ''
        if file_json == '':
            file_json = file.replace('.smil', '.json')
        with open(file_json, 'w') as f:
            """
            Dump pasa el objeto (self.lista)a un string en json y lo mete en f
            Indent es el numero de espacios que crea el json,4 es como un tab
            """
            json.dump(self.lista, f, indent=4)

    def do_local(self):
        for diccaux in self.lista:
            for atributo, valor in diccaux.items():
                if atributo == 'src':
                    if valor.startswith('http://'):
                        """
                        rfind devuelve la posicion de la ultima "/"
                        """
                        file_local = valor[valor.rfind('/'):]
                        """
                        Descarga lo que hay en la ruta "valor"
                        y crea un archivo de nombre "desde donde
                        encontro la ultima "/" hasta el final", es decir,
                        el nombre que tenia el elemento que queremos descargar
                        """
                        urllib.request.urlretrieve(valor, file_local[1:])
                        """
                        Ahora en src sustituimos la URL por el archivo local, 
                        para que "mire" el archivo descargado en lugar de usar
                        internet
                        """
                        diccaux['src'] = file_local[1:]


if __name__ == "__main__":
    """
    Programa principal
    """
    if len(sys.argv) != 2:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    karaoke = KaraokeLocal(file)
    print(karaoke)
    karaoke.do_json(file)
    karaoke.do_local()
    """
    Como esta hecho para que si no le decimos nombre, sea el mismo cambiando
    .smil por .json, podemos pasar local.smil aunque no exista y asi nos
    devolvera local.json, que es lo que queremos
    """
    karaoke.do_json('local.smil')
    print(karaoke)
