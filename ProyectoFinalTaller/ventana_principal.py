# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created: Mon Jul 14 03:53:08 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1094, 615)
        Dialog.setMinimumSize(QtCore.QSize(500, 0))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 17))
        self.label.setObjectName("label")
        self.tabla_categorias = QtGui.QTableView(Dialog)
        self.tabla_categorias.setGeometry(QtCore.QRect(10, 70, 541, 201))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_categorias.sizePolicy().hasHeightForWidth())
        self.tabla_categorias.setSizePolicy(sizePolicy)
        self.tabla_categorias.setMinimumSize(QtCore.QSize(500, 200))
        self.tabla_categorias.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabla_categorias.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabla_categorias.setAutoScroll(False)
        self.tabla_categorias.setDragEnabled(True)
        self.tabla_categorias.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla_categorias.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_categorias.setSortingEnabled(True)
        self.tabla_categorias.setObjectName("tabla_categorias")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 66, 17))
        self.label_2.setObjectName("label_2")
        self.tabla_recetas = QtGui.QTableView(Dialog)
        self.tabla_recetas.setGeometry(QtCore.QRect(10, 320, 361, 251))
        self.tabla_recetas.setObjectName("tabla_recetas")
        self.nueva_categoria = QtGui.QPushButton(Dialog)
        self.nueva_categoria.setGeometry(QtCore.QRect(660, 90, 121, 27))
        self.nueva_categoria.setObjectName("nueva_categoria")
        self.eliminar_categoria = QtGui.QPushButton(Dialog)
        self.eliminar_categoria.setGeometry(QtCore.QRect(660, 190, 131, 27))
        self.eliminar_categoria.setObjectName("eliminar_categoria")
        self.editar_categoria = QtGui.QPushButton(Dialog)
        self.editar_categoria.setGeometry(QtCore.QRect(660, 140, 121, 27))
        self.editar_categoria.setObjectName("editar_categoria")
        self.eliminar_receta = QtGui.QPushButton(Dialog)
        self.eliminar_receta.setGeometry(QtCore.QRect(520, 500, 131, 27))
        self.eliminar_receta.setObjectName("eliminar_receta")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 320, 101, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(520, 380, 101, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.editar_receta = QtGui.QPushButton(Dialog)
        self.editar_receta.setGeometry(QtCore.QRect(520, 460, 121, 27))
        self.editar_receta.setObjectName("editar_receta")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(520, 340, 231, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(640, 380, 101, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.nueva_receta = QtGui.QPushButton(Dialog)
        self.nueva_receta.setGeometry(QtCore.QRect(520, 420, 121, 27))
        self.nueva_receta.setObjectName("nueva_receta")
        self.imagen = QtGui.QLabel(Dialog)
        self.imagen.setGeometry(QtCore.QRect(780, 340, 251, 181))
        self.imagen.setObjectName("imagen")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Administrador de recetas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Categorías:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Recetas:", None, QtGui.QApplication.UnicodeUTF8))
        self.nueva_categoria.setText(QtGui.QApplication.translate("Dialog", "Nueva categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_categoria.setText(QtGui.QApplication.translate("Dialog", "Eliminar categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_categoria.setText(QtGui.QApplication.translate("Dialog", "Editar categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_receta.setText(QtGui.QApplication.translate("Dialog", "Eliminar receta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "categorias", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_receta.setText(QtGui.QApplication.translate("Dialog", "Editar receta", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Dialog", "paises", None, QtGui.QApplication.UnicodeUTF8))
        self.nueva_receta.setText(QtGui.QApplication.translate("Dialog", "Nueva receta", None, QtGui.QApplication.UnicodeUTF8))
        self.imagen.setText(QtGui.QApplication.translate("Dialog", "Imagen", None, QtGui.QApplication.UnicodeUTF8))

