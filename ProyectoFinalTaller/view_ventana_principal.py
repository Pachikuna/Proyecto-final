# -*- coding: utf-8 -*-
import sys
import os
from PySide import QtGui, QtCore
import controller
import view_ventana_nuevareceta
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
        self.ventana.lineEdit.textChanged[str].connect(self.filtro)
        self.ventana.tabla_recetas.clicked.connect(self.infoRecetas)
        self.ventana.nueva_categoria.clicked.connect(self.nueva_cate)
        self.ventana.editar_categoria.clicked.connect(self.editar_cate)
        self.ventana.eliminar_categoria.clicked.connect(self.eliminar_cate)
        self.ventana.nueva_receta.clicked.connect(self.nueva_rece)
        self.ventana.editar_receta.clicked.connect(self.editar_rece)
        self.ventana.eliminar_receta.clicked.connect(self.eliminar_rece)
        #demas métodos
        self.show()

    def render_table(self):
        self.ventana.tabla_categorias.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.ventana.tabla_categorias.adjustSize()
        self.ventana.tabla_categorias.setFixedWidth(600)
        self.ventana.tabla_categorias.setFixedHeight(200)

    def filtro(self, txt):
        texto = txt.encode('utf8')
        products = controller.filtrarProductos(txt)
        self.cargar_recetas_filtro(products)

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
        self.model = QtGui.QStandardItemModel(len(recetas), 7)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"id categoria"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Descripción"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Ingredientes"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Preparación"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"País"))

        r = 0
        for row in recetas:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id_receta'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_categoria'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['ingredientes'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['preparacion'])
            index = self.model.index(r, 6, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_pais'])
            r = r + 1
        self.ventana.tabla_recetas.setModel(self.model)
        self.ventana.tabla_recetas.setColumnWidth(0, 80)
        self.ventana.tabla_recetas.setColumnWidth(1, 150)
        self.ventana.tabla_recetas.setColumnWidth(2, 80)
        self.ventana.tabla_recetas.setColumnWidth(3, 100)
        self.ventana.tabla_recetas.setColumnWidth(4, 800)
        self.ventana.tabla_recetas.setColumnWidth(5, 800)
        self.ventana.tabla_recetas.setColumnWidth(6, 100)




    def nueva_rece(self):
        formulario = view_ventana_nuevareceta.Form_3(self)
        formulario.exec_()

    def eliminar_rece(self):
        model = self.ventana.tabla_recetas.model()
        index = self.ventana.tabla_recetas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            print cod
            if (controller.delete_receta(cod)):
                self.cargar_recetas()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.showMessage("Error al eliminar el registro")
                return False

    def editar_rece(self):
        model = self.ventana.tabla_recetas.model()
        index = self.ventana.tabla_recetas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            cod = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            receta = controller.buscarEditar2(cod)
            print receta
            self.formulario = view_ventana_nuevareceta.Form_3(self)
            self.formulario.carga(receta, cod)


    def cargar_categorias(self):
        categorias = controller.obtener_categorias()
        self.model = QtGui.QStandardItemModel(len(categorias), 4)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Número de recetas"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Descripción"))



        r = 0
        for row in categorias:
            cantidad = controller.contador(row[0])
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id_categoria'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, cantidad)
            r = r + 1
        self.ventana.tabla_categorias.setModel(self.model)
        self.ventana.tabla_categorias.setColumnWidth(0, 100)
        self.ventana.tabla_categorias.setColumnWidth(1, 120)
        self.ventana.tabla_categorias.setColumnWidth(2, 150)
        self.ventana.tabla_categorias.setColumnWidth(3, 800)





    def cargar_recetas_filtro(self, productos):
        self.model = QtGui.QStandardItemModel(len(productos), 7)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"id categoria"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Descripción"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Ingredientes"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Preparación"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"País"))
        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id_receta'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_categoria'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['ingredientes'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['preparacion'])
            index = self.model.index(r, 6, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_pais'])
            r = r + 1
        self.ventana.tabla_recetas.setModel(self.model)
        self.ventana.tabla_recetas.setColumnWidth(0, 80)
        self.ventana.tabla_recetas.setColumnWidth(1, 150)
        self.ventana.tabla_recetas.setColumnWidth(2, 80)
        self.ventana.tabla_recetas.setColumnWidth(3, 100)
        self.ventana.tabla_recetas.setColumnWidth(4, 800)
        self.ventana.tabla_recetas.setColumnWidth(5, 800)
        self.ventana.tabla_recetas.setColumnWidth(6, 100)

    def infoRecetas(self):
        model = self.ventana.tabla_recetas.model()
        index = self.ventana.tabla_recetas.currentIndex()
        codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        valores = controller.infoFila2(codigo)

        ficheros = os.listdir('Img/')
        fichero = valores[6] in ficheros
        if fichero is True:
            direccion = 'Img/{0}'.format(valores[6])
            self.ventana.imagen.setPixmap(direccion)
            self.ventana.imagen.adjustSize()
        else:
            fichero = valores[6] + ".png" in ficheros
            if fichero is True:
                direccion = 'Img/{0}'.format(valores[6])
                self.ventana.imagen.setPixmap(direccion)
                self.ventana.imagen.adjustSize()


def run():
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
