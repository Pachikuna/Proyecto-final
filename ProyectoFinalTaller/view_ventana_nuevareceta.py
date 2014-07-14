#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller
from ventana_nuevareceta import *

class Form_3 (QtGui.QWidget):

    def __init__(self, parent=None):
        super(Form_3, self).__init__()
        self.ventana = Ui_ventana_nuevareceta()
        self.ventana.setupUi(self)
        self.ventana.btn_aceptar.clicked.connect(self.aceptar)
        self.ventana.btn_cancelar.clicked.connect(self.cancelar)
        self.codigo = ""
        self.var = 0

        self.show()

    def carga(self, receta, codigo):
        self.codigo = codigo
        self.ventana.nombre.setText(receta[0][1])
        self.ventana.descripcion.setText(receta[0][3])
        self.ventana.ingredientes.setText(receta[0][5])
        self.ventana.preparacion.setText(receta[0][4])
        self.ventana.pais.setText(receta[0][7])
        self.ventana.direccion_imagen.setText(receta[0][6])
        var = 1
        print var

    def aceptar(self):
        nombre = self.ventana.nombre.text()
        descrip = self.ventana.descripcion.text()
        ingre = self.ventana.ingredientes.text()
        prepa = self.ventana.preparacion.text()
        pais = self.ventana.pais.text()
        img = self.ventana.direccion_imagen.text()
        var = 1
        print var

        datos = (nombre, descrip, ingre, prepa, pais, img)
        cod2 = self.codigo

        if(var == 1):
            controller.reescribeProducto2(datos, cod2)

        self.close()

    def cancelar(self):
        self.close()

