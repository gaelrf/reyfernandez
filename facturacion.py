from PyQt5 import QtWidgets, QtCore

import conexion
import var
from babel.numbers import format_currency
import locale
locale.setlocale( locale.LC_ALL,'')


class Facturacion():

    def buscaCli(self):
        try:
            dni = var.ui.txtFactDNI.text().upper()
            var.ui.txtFactDNI.setText(dni)
            registro = conexion.Conexion.buscaNombreFact(dni)
            if (registro):
                nombre = registro[0] + ', ' + registro[1]
                var.ui.lblNoneFact.setText(nombre)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente no encontrado')
                msg.exec()

        except Exception as error:
            print('Error en modulo buscar clientes factura', error)

    def altaFact(self):
        try:
            registro = []
            dni = var.ui.txtFactDNI.text().upper()
            var.ui.txtFactDNI.setText(dni)
            registro.append(dni)
            fechafact = var.ui.txtFechaFact.text()
            registro.append(fechafact)
            conexion.Conexion.altaFact(registro)
            conexion.Conexion.cargarTableFact(self)
        except Exception as error:
            print('Error en modulo buscar alta factura', error)

    def cargaFact(self):
        try:
            fila = var.ui.tableFact.selectedItems()  # seleccionamos la fila
            datos = [var.ui.lblCodFact, var.ui.txtFechaFact]
            if fila:  # cargamos en row todos los datos de la fila
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            dni = conexion.Conexion.buscaDNIFact(row[0])
            var.ui.txtFactDNI.setText(dni)
            registro = conexion.Conexion.buscaNombreFact(dni)
            if registro:
                nombre = registro[0] + ', ' + registro[1]
                var.ui.lblNoneFact.setText(nombre)
            conexion.Conexion.cargarLineasVenta(str(var.ui.lblCodFact.text()))

        except Exception as error:
            print('error alta en factura', error)
    def cargaLineaVenta(index):
        try:
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.currentIndexChanged.connect(Facturacion.procesoVenta)
            var.cmbProducto.setFixedSize(170,25)
            conexion.Conexion.cargarCmbProducto(self=None)
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.editingFinished.connect(Facturacion.totalLineaVenta)
            var.txtCantidad.setFixedSize(80,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tableVentas.setRowCount(index+1)
            var.ui.tableVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tableVentas.setCellWidget(index,3,var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea venta ', error)

    def procesoVenta(self):
        try:
            articulo = var.cmbProducto.currentText()
            row = var.ui.tableVentas.currentRow()
            if (articulo!=''):
                dato =conexion.Conexion.obtenerCodPrecio(articulo)
                var.precio = dato[1]
                precioEu = format_currency(dato[1], 'EUR', locale='de_DE')
                var.codpro = dato[0]
                var.ui.tableVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(precioEu)))
                var.ui.tableVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            else:
                var.ui.tableVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(None))
                var.ui.tableVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)


        except Exception as error:
            print('Error en proceso venta ', error)


    def totalLineaVenta(self = None):
        try:
            venta = []
            row = var.ui.tableVentas.currentRow()
            cantidad = round(float(var.txtCantidad.text().replace(",", ".")), 2)
            totalLinea = round(float(var.precio) * float(cantidad), 2)
            var.ui.tableVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(totalLinea) + '€'))
            var.ui.tableVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            codfac = var.ui.lblCodFact.text()
            print(codfac)
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append((float(var.precio)))
            venta.append(float(cantidad))
            conexion.Conexion.cargarVenta(venta)

        except Exception as error:
            print('Error al procesar el total de una venta ', error)

    def limpiarFacturas(self):
        try:
            var.ui.txtDNIFac.setText("")
            var.ui.lblNumFactura.setText("")
            var.ui.txtFechaFac.setText("")
            var.ui.lblNomFac.setText("")
            conexion.Conexion.cargaTabFacturas(self)

        except Exception as error:
            print('Error al limpiar campos de factura ', error)
