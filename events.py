import sys
from window import *
import var


class Eventos():
    def salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print("Error en módulo salir")
    def abrirCal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario ',error)
    def resizeTableCli(self):
        try:
            header = var.ui.tableCliente.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en el modulo redimensionar tabla ',error)

    def abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error en el modulo abrir archivo ',error)

