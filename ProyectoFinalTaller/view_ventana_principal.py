# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller
# import view_ventana_nuevareceta
import view_ventana_nuevacategoria
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
        self.ventana.nueva_categoria.clicked.connect(self.nueva_cate)
        self.ventana.editar_categoria.clicked.connect(self.editar_cate)
        self.ventana.eliminar_categoria.clicked.connect(self.eliminar_cate)
        #demas métodos
        self.show()

    def render_table(self):
        self.ventana.tabla_categorias.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.ventana.tabla_categorias.adjustSize()
        self.ventana.tabla_categorias.setFixedWidth(600)
        self.ventana.tabla_categorias.setFixedHeight(200)


    def editar_cate(self):
        model = self.ventana.tabla_categorias.model()
        index = self.ventana.tabla_categorias.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            categoria = controller.buscarEditar(cod)
            self.formulario = view_ventana_nuevacategoria.Form_2(self)
            self.formulario.carga(categoria, cod)


    def nueva_cate(self):
        formulario = view_ventana_nuevacategoria.Form_2(self)
        formulario.exec_()

    def eliminar_cate(self):
        model = self.ventana.tabla_categorias.model()
        index = self.ventana.tabla_categorias.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(cod)):
                self.cargar_categorias()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                return False

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
        self.model = QtGui.QStandardItemModel(len(categorias), 3)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
#        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Cantidad de recetas"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Descripción")


        r = 0
        for row in categorias:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id_categoria'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])

            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            r = r + 1
        self.ventana.tabla_categorias.setModel(self.model)
        self.ventana.tabla_categorias.setColumnWidth(0, 100)
        self.ventana.tabla_categorias.setColumnWidth(1, 100)
#        self.ventana.tabla_categorias.setColumnWidth(2, 100)
        self.ventana.tabla_categorias.setColumnWidth(2, 800)




def run():
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
