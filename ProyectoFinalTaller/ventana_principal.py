# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created: Fri Jul 11 22:07:08 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 616)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 70, 601, 201))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtGui.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(20, 310, 461, 201))
        self.tableView_2.setObjectName("tableView_2")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 66, 17))
        self.label_2.setObjectName("label_2")
        self.nueva_categoria = QtGui.QPushButton(self.centralwidget)
        self.nueva_categoria.setGeometry(QtCore.QRect(640, 90, 121, 27))
        self.nueva_categoria.setObjectName("nueva_categoria")
        self.editar_categoria = QtGui.QPushButton(self.centralwidget)
        self.editar_categoria.setGeometry(QtCore.QRect(640, 130, 121, 27))
        self.editar_categoria.setObjectName("editar_categoria")
        self.eliminar_categoria = QtGui.QPushButton(self.centralwidget)
        self.eliminar_categoria.setGeometry(QtCore.QRect(640, 170, 131, 27))
        self.eliminar_categoria.setObjectName("eliminar_categoria")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 310, 101, 17))
        self.label_3.setObjectName("label_3")
        self.nueva_receta = QtGui.QPushButton(self.centralwidget)
        self.nueva_receta.setGeometry(QtCore.QRect(500, 410, 121, 27))
        self.nueva_receta.setObjectName("nueva_receta")
        self.editar_receta = QtGui.QPushButton(self.centralwidget)
        self.editar_receta.setGeometry(QtCore.QRect(500, 450, 121, 27))
        self.editar_receta.setObjectName("editar_receta")
        self.eliminar_receta = QtGui.QPushButton(self.centralwidget)
        self.eliminar_receta.setGeometry(QtCore.QRect(500, 490, 131, 27))
        self.eliminar_receta.setObjectName("eliminar_receta")
        self.imagen = QtGui.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(760, 310, 171, 191))
        self.imagen.setObjectName("imagen")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 330, 231, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 370, 101, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(620, 370, 101, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Administrador de recetas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Categorías:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Recetas:", None, QtGui.QApplication.UnicodeUTF8))
        self.nueva_categoria.setText(QtGui.QApplication.translate("MainWindow", "Nueva categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_categoria.setText(QtGui.QApplication.translate("MainWindow", "Editar categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_categoria.setText(QtGui.QApplication.translate("MainWindow", "Eliminar categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.nueva_receta.setText(QtGui.QApplication.translate("MainWindow", "Nueva receta", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_receta.setText(QtGui.QApplication.translate("MainWindow", "Editar receta", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_receta.setText(QtGui.QApplication.translate("MainWindow", "Eliminar receta", None, QtGui.QApplication.UnicodeUTF8))
        self.imagen.setText(QtGui.QApplication.translate("MainWindow", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "categorias", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("MainWindow", "paises", None, QtGui.QApplication.UnicodeUTF8))
