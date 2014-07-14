# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller
# import view_ventana_nuevareceta
# import view_ventana_nuevacategoria
from ventana_principal import *


class Form(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__()
        self.ventana = Ui_Dialog()
        self.ventana.setupUi(self)
        self.render_table()
        self.render_table2()
        self.cargar_categorias()
        self.cargar_recetas()
        #demas métodos
        self.show()

    def render_table(self):
        self.ventana.tabla_categorias.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.ventana.tabla_categorias.adjustSize()
        self.ventana.tabla_categorias.setFixedWidth(600)
        self.ventana.tabla_categorias.setFixedHeight(200)

    def render_table2(self):
        self.ventana.tabla_recetas.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.ventana.tabla_recetas.adjustSize()
        self.ventana.tabla_recetas.setFixedWidth(500)
        self.ventana.tabla_recetas.setFixedHeight(200)

    def cargar_recetas(self):
        recetas = controller.obtener_recetas()
        self.model = QtGui.QStandardItemModel(len(recetas), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"id categoria"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripción"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Ingredientes"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Preparación"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"País"))

        r = 0
        for row in recetas:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_categoria'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['ingredientes'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['preparacion'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_pais'])
            r = r + 1
        self.ventana.tabla_recetas.setModel(self.model)
        self.ventana.tabla_recetas.setColumnWidth(0, 150)
        self.ventana.tabla_recetas.setColumnWidth(1, 100)
        self.ventana.tabla_recetas.setColumnWidth(2, 100)
        self.ventana.tabla_recetas.setColumnWidth(3, 800)
        self.ventana.tabla_recetas.setColumnWidth(4, 800)
        self.ventana.tabla_recetas.setColumnWidth(5, 100)



    def cargar_categorias(self):
        categorias = controller.obtener_categorias()
        self.model = QtGui.QStandardItemModel(len(categorias), 2)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Descripción"))

        r = 0
        for row in categorias:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            r = r + 1
        self.ventana.tabla_categorias.setModel(self.model)
        self.ventana.tabla_categorias.setColumnWidth(0, 150)
        self.ventana.tabla_categorias.setColumnWidth(1, 800)




def run():
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
