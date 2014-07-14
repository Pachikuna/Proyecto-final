# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_nuevacategoria.ui'
#
# Created: Mon Jul 14 00:36:04 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ventana_nuevacategoria(object):
    def setupUi(self, ventana_nuevacategoria):
        ventana_nuevacategoria.setObjectName("ventana_nuevacategoria")
        ventana_nuevacategoria.resize(547, 325)
        self.btn_cancelar = QtGui.QPushButton(ventana_nuevacategoria)
        self.btn_cancelar.setGeometry(QtCore.QRect(280, 240, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.descripcion_categoria = QtGui.QLineEdit(ventana_nuevacategoria)
        self.descripcion_categoria.setGeometry(QtCore.QRect(130, 120, 381, 101))
        self.descripcion_categoria.setObjectName("descripcion_categoria")
        self.btn_aceptar = QtGui.QPushButton(ventana_nuevacategoria)
        self.btn_aceptar.setGeometry(QtCore.QRect(120, 240, 98, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.label_2 = QtGui.QLabel(ventana_nuevacategoria)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(ventana_nuevacategoria)
        self.label.setGeometry(QtCore.QRect(40, 70, 66, 17))
        self.label.setObjectName("label")
        self.nombre_categoria = QtGui.QLineEdit(ventana_nuevacategoria)
        self.nombre_categoria.setGeometry(QtCore.QRect(130, 70, 361, 27))
        self.nombre_categoria.setObjectName("nombre_categoria")
        self.label_3 = QtGui.QLabel(ventana_nuevacategoria)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 66, 17))
        self.label_3.setObjectName("label_3")
        self.id_categoria = QtGui.QLineEdit(ventana_nuevacategoria)
        self.id_categoria.setGeometry(QtCore.QRect(130, 20, 361, 27))
        self.id_categoria.setObjectName("id_categoria")

        self.retranslateUi(ventana_nuevacategoria)
        QtCore.QMetaObject.connectSlotsByName(ventana_nuevacategoria)

    def retranslateUi(self, ventana_nuevacategoria):
        ventana_nuevacategoria.setWindowTitle(QtGui.QApplication.translate("ventana_nuevacategoria", "ventana_nuevacategoria", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("ventana_nuevacategoria", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("ventana_nuevacategoria", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ventana_nuevacategoria", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ventana_nuevacategoria", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ventana_nuevacategoria", "id:", None, QtGui.QApplication.UnicodeUTF8))

