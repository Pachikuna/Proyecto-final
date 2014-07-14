#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller
from ventana_nuevacategoria import *

class Form_2(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Form_2, self).__init__()
        self.ventana = Ui_ventana_nuevacategoria()
        self.ventana.setupUi(self)
        self.ventana.btn_aceptar.clicked.connect(self.aceptar)
        self.ventana.btn_cancelar.clicked.connect(self.cancelar)
        self.codigo = ""
        self.var = 0

        self.show()

    def carga(self, categoria, codigo):
        self.codigo = codigo
        self.ventana.id_categoria.setText(str(categoria[0][0]))
        self.ventana.nombre_categoria.setText(categoria[0][1])
        self.ventana.descripcion_categoria.setText(categoria[0][2])
        var = 1


    def aceptar(self):
        id_cate = self.ventana.id_categoria.text()
        nombre = self.ventana.nombre_categoria.text()
        descrip = self.ventana.descripcion_categoria.text()

        datos = (id_cate, nombre, descrip)
        cod2 = self.codigo
        if(self.var == 1):

            controller.reescribeProducto(datos, cod2)
        else:
            controller.insertarproductos(datos)
        self.close()


    def cancelar(self):
        self.close()

