# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_nuevacategoria.ui'
#
# Created: Fri Jul 11 22:08:37 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 335)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_aceptar = QtGui.QPushButton(self.centralwidget)
        self.btn_aceptar.setGeometry(QtCore.QRect(120, 230, 98, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.btn_cancelar = QtGui.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(280, 230, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.nombre_categoria = QtGui.QLineEdit(self.centralwidget)
        self.nombre_categoria.setGeometry(QtCore.QRect(130, 40, 361, 27))
        self.nombre_categoria.setObjectName("nombre_categoria")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 91, 20))
        self.label_2.setObjectName("label_2")
        self.descripcion_categoria = QtGui.QLineEdit(self.centralwidget)
        self.descripcion_categoria.setGeometry(QtCore.QRect(130, 110, 381, 101))
        self.descripcion_categoria.setObjectName("descripcion_categoria")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Nueva categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("MainWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("MainWindow", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))

