# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_nuevareceta.ui'
#
# Created: Fri Jul 11 22:09:15 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 539)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_aceptar = QtGui.QPushButton(self.centralwidget)
        self.btn_aceptar.setGeometry(QtCore.QRect(180, 450, 98, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.btn_cancelar = QtGui.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(310, 450, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.nombre = QtGui.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(180, 60, 311, 27))
        self.nombre.setObjectName("nombre")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 101, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 340, 101, 17))
        self.label_5.setObjectName("label_5")
        self.descripcion = QtGui.QLineEdit(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(180, 110, 311, 27))
        self.descripcion.setObjectName("descripcion")
        self.pais = QtGui.QLineEdit(self.centralwidget)
        self.pais.setGeometry(QtCore.QRect(180, 340, 311, 27))
        self.pais.setObjectName("pais")
        self.preparacion = QtGui.QLineEdit(self.centralwidget)
        self.preparacion.setGeometry(QtCore.QRect(180, 240, 311, 81))
        self.preparacion.setObjectName("preparacion")
        self.ingredientes = QtGui.QLineEdit(self.centralwidget)
        self.ingredientes.setGeometry(QtCore.QRect(180, 160, 311, 61))
        self.ingredientes.setObjectName("ingredientes")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 400, 101, 17))
        self.label_6.setObjectName("label_6")
        self.direccion_imagen = QtGui.QLineEdit(self.centralwidget)
        self.direccion_imagen.setGeometry(QtCore.QRect(180, 400, 251, 27))
        self.direccion_imagen.setObjectName("direccion_imagen")
        self.carga_imagen = QtGui.QToolButton(self.centralwidget)
        self.carga_imagen.setGeometry(QtCore.QRect(440, 400, 23, 25))
        self.carga_imagen.setObjectName("carga_imagen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nueva receta", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("MainWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("MainWindow", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Descripción: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Ingredientes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Preparación: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "País", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Imagen:", None, QtGui.QApplication.UnicodeUTF8))
        self.carga_imagen.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

