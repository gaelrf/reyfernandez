import locale

import conexion
from window import *
import var
locale.setlocale(locale.LC_ALL, '')


class Articulo():
    def guardaArt(self):
        try:
            newart = []
            newart.append(var.ui.txtNombreArt.text())
            precio = str(var.ui.txtPrecioArt.text())
            #Aquí Habría que sustituir las comas por puntos
            newart.append(precio)
            print(newart)
            conexion.Conexion.altaArt(newart)
            conexion.Conexion.cargarTablaArt(self)
        except Exception as error:
            print('Error en modulo guardar articulo', error)

    def modifArt(self):
        try:
            newart = []
            newart.append(var.ui.lblNumArt.text())
            newart.append(var.ui.txtNombreArt.text())
            precio = str(var.ui.txtPrecioArt.text())
            #Aquí Habría que sustituir las comas por puntos
            newart.append(precio)
            print(newart)
            conexion.Conexion.modifArt(newart)
            conexion.Conexion.cargarTablaArt(self)

        except Exception as error:
            print('Error en modificar datos de articulo', error)

    def bajaArt(self):
        try:
            conexion.Conexion.bajaArt(str(var.ui.lblNumArt.text()))
            conexion.Conexion.cargarTablaArt(self)
        except Exception as error:
            print('Error en modulo borrar articulo', error)

    def cargaArt(self):
        try:
            fila = var.ui.tableArt.selectedItems()
            datos = [var.ui.lblNumArt, var.ui.txtNombreArt, var.ui.txtPrecioArt]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

        except Exception as error:
            print('Error en cargar datos de articulo', error)

    def buscaArt(self):
        try:
            conexion.Conexion.buscarTablaArt(str(var.ui.txtNombreArt.text()))
        except Exception as error:
            print('Error en modulo buscar articulo', error)
