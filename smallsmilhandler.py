#!/usr/bin/python3
# -*- coding: utf-8 -*-


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__ (self):

        #rootlayout
        self.width
        self.height
        self.backgroundcolor =
        #region
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        #img
        self.imgsrc = ""
        self.imgregion = ""
        self.imgbegin = ""
        self.imgdur = ""
        #audio
        self.audsrc = ""
        self.audbegin = ""
        self.auddur = ""
        #textstream
        self.txtsrc = ""
        self.txtregion = ""


    def startElement(self, name, attrs):

        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgroundcolor = attrs.get('backgroundcolor', "")
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
        elif name == 'img':
            self.imgsrc = attrs.get('imgsrc', "")
            self.imgregion = attrs.get('imgregion', "")
            self.imgbegin = attrs.get('imgbegin', "")
            self.imgdur = attrs.get('imgdur', "")
        elif name == 'audio':
            self.audsrc = attrs.get('audsrc', "")
            self.audbegin = attrs.get('audbegin', "")
            self.auddur = attrs.get('auddur', "")
        elif name == 'textstream':
            self.txtsrc = attrs.get('audsrc', "")
            self.txtregion = attrs.get('txtregion', "")



    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            print(self.pregunta)
            self.pregunta = ""
            self.inPregunta = False
        if name == 'respuesta':
            print(self.respuesta)
            self.respuesta = ""
            self.inRespuesta = False

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = self.pregunta + char
        if self.inRespuesta:
            self.respuesta += char

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
