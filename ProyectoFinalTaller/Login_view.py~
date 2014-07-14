#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui
import controller_usuarios
from Login import Ui_Login
from view_ventana_principal import Form


class Login(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiL = Ui_Login()
        self.uiL.setupUi(self)

        self.uiL.Cancelar.clicked.connect(self.Cancelar)
        self.uiL.Aceptar.clicked.connect(self.Ejecutar)
        self.show()

    def Cancelar(self):
        self.close()

    def Ejecutar(self):
#consulta si existe  el usuario con su contraseña respectiva de ser asi
#se inicia  el programa ,si no, se despliega un mensaje de error
        self.lis = controller_usuarios.busca_usuario(self.uiL.nombreu.text().strip(),
                    self.uiL.contrase.text())
        if(len(self.lis) == 1):
            self.Nueva = Form()
            self.close()
        else:
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            error = u"usuario o contraseña invalidos"
            self.errorMessageDialog.showMessage(error)
            self.uiL.nombreu.clear()
            self.uiL.contrase.clear()


def run():
    app = QtGui.QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
