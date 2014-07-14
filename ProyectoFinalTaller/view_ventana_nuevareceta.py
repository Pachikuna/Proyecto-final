#!/usr/bin/python
# -*- coding: utf-8 -*-
import ventana_nuevareceta
from PySide import QtGui
from ventana_nuevareceta import Ui_ventana_nuevareceta

class Ui_ventana_nuevareceta (QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.edit = 0
        self.codigo = ""
        self.ui = Ui_ventana_nuevareceta()
        self.ui.Ui_ventana_nuevareceta(self)
        self.ui.Aceptar.clicked.connect(self.aceptar)
        self.ui.Cancelar.clicked.connect(self.cancelar)
        self.show()

    def carga(self, producto, codigo):
        self.codigo = codigo
        self.label.setText(producto[0][3])
        self.label_2.setText(producto[0][1])
        self.label_3.setText(producto[0][2])
        self.label_4.setText(producto[0][3])
        self.label_5.setText(producto[0][1])
        self.label_6.setText(producto[0][2])
        self.show()

    def aceptar(self):
        nombre = self.label.setText()
        descrip = self.label_2.setText()
        ingre = self.label_3.setText()
        prepa = self.label_4.setText()
        pais = self.label_5.setText()
        img = self.label_6.setText()

        datos = (nombre, descrip, ingre, prepa, pais, img)

        self.close()

    def cancelar(self):
        self.close()

