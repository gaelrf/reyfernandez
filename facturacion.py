from PyQt5 import QtWidgets, QtCore

import conexion
import var


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
            fila = var.ui.tableFact.selectedItems()
            datos = [var.ui.lblCodFact,var.ui.txtFechaFact]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            dni = conexion.Conexion.buscaDNIFact(row[0])
            var.ui.txtFactDNI.setText(dni)
            Facturacion.buscaCli(self)

        except Exception as error:
            print('Error en cargar datos de articulo', error)
    def cargarLineaVenta(self):
        try:
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            var.txtCantidad = QtWidgets.QLineEdit()
            #conexion.Conexion.cargarCmbProducto()
            var.cmbProducto.setFixedSize(150, 25)
            var.txtCantidad.setFixedSize(60, 25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tableVentas.setRowCount(index + 1)
            var.ui.tableVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tableVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea venta ', error)
    def procesoVenta(self):
        try:
            row = var.ui.tableVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            precio =conexion.Conexion.obtenerCodProd(articulo)
            var.ui.tableVentas.setItem(row,2,QtWidgets.QTableWidgetItem(str(precio,1)))

        except Exception as error:
            print('Error en proceso venta')