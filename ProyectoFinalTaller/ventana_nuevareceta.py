# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_nuevareceta.ui'
#
# Created: Sat Jul 12 00:12:18 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ventana_nuevareceta(object):
    def setupUi(self, ventana_nuevareceta):
        ventana_nuevareceta.setObjectName("ventana_nuevareceta")
        ventana_nuevareceta.resize(523, 538)
        self.btn_cancelar = QtGui.QPushButton(ventana_nuevareceta)
        self.btn_cancelar.setGeometry(QtCore.QRect(300, 440, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.direccion_imagen = QtGui.QLineEdit(ventana_nuevareceta)
        self.direccion_imagen.setGeometry(QtCore.QRect(170, 390, 251, 27))
        self.direccion_imagen.setObjectName("direccion_imagen")
        self.descripcion = QtGui.QLineEdit(ventana_nuevareceta)
        self.descripcion.setGeometry(QtCore.QRect(170, 100, 311, 27))
        self.descripcion.setObjectName("descripcion")
        self.label_6 = QtGui.QLabel(ventana_nuevareceta)
        self.label_6.setGeometry(QtCore.QRect(60, 390, 101, 17))
        self.label_6.setObjectName("label_6")
        self.ingredientes = QtGui.QLineEdit(ventana_nuevareceta)
        self.ingredientes.setGeometry(QtCore.QRect(170, 150, 311, 61))
        self.ingredientes.setObjectName("ingredientes")
        self.label_2 = QtGui.QLabel(ventana_nuevareceta)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(ventana_nuevareceta)
        self.label.setGeometry(QtCore.QRect(60, 60, 66, 17))
        self.label.setObjectName("label")
        self.label_3 = QtGui.QLabel(ventana_nuevareceta)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtGui.QLabel(ventana_nuevareceta)
        self.label_5.setGeometry(QtCore.QRect(60, 330, 101, 17))
        self.label_5.setObjectName("label_5")
        self.carga_imagen = QtGui.QToolButton(ventana_nuevareceta)
        self.carga_imagen.setGeometry(QtCore.QRect(430, 390, 23, 25))
        self.carga_imagen.setObjectName("carga_imagen")
        self.pais = QtGui.QLineEdit(ventana_nuevareceta)
        self.pais.setGeometry(QtCore.QRect(170, 330, 311, 27))
        self.pais.setObjectName("pais")
        self.btn_aceptar = QtGui.QPushButton(ventana_nuevareceta)
        self.btn_aceptar.setGeometry(QtCore.QRect(170, 440, 98, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.nombre = QtGui.QLineEdit(ventana_nuevareceta)
        self.nombre.setGeometry(QtCore.QRect(170, 50, 311, 27))
        self.nombre.setObjectName("nombre")
        self.preparacion = QtGui.QLineEdit(ventana_nuevareceta)
        self.preparacion.setGeometry(QtCore.QRect(170, 230, 311, 81))
        self.preparacion.setObjectName("preparacion")
        self.label_4 = QtGui.QLabel(ventana_nuevareceta)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 101, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ventana_nuevareceta)
        QtCore.QMetaObject.connectSlotsByName(ventana_nuevareceta)

    def retranslateUi(self, ventana_nuevareceta):
        ventana_nuevareceta.setWindowTitle(QtGui.QApplication.translate("ventana_nuevareceta", "Nueva receta", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Imagen:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Descripción: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Ingredientes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ventana_nuevareceta", "País", None, QtGui.QApplication.UnicodeUTF8))
        self.carga_imagen.setText(QtGui.QApplication.translate("ventana_nuevareceta", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ventana_nuevareceta", "Preparación: ", None, QtGui.QApplication.UnicodeUTF8))

