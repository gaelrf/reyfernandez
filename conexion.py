import locale
from datetime import datetime

import xlwt as xlwt
from PyQt5 import QtSql, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

import facturacion
import var
import xlrd as xlrd


class Conexion():
    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None,
                                               'No se puede abrir la base de datos.\n' 'Hz click para continuar',
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexion establecida')
                return True
        except Exception as error:
            print('Problemas en conexion', error)

    def altaCli(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni, alta, apellido, nombre, direccion, provincia, municipio, sexo, pago, envio)'
                'VALUES (:dni, :alta, :apellido, :nombre, :direccion, :provincia, :municipio, :sexo, :pago, :envio)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':alta', str(newcli[1]))
            query.bindValue(':apellido', str(newcli[2]))
            query.bindValue(':nombre', str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            query.bindValue(':envio', str(newcli[9]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente insertado Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('DNI repetido Válido')
                msg.exec()
        except Exception as error:
            print('Error en Alta cliente', error)

    def bajaCli(dni):
        try:
            print(dni)
            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente borrado Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('DNI no Válido')
                msg.exec()
        except Exception as error:
            print('Error en Baja cliente', error)

    def cargarTablaCli(self):

        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellido, nombre ,alta, pago from clientes order by apellido, nombre')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    alta = query.value(3)
                    pago = query.value(4)
                    var.ui.tableCliente.setRowCount(index + 1)
                    var.ui.tableCliente.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tableCliente.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tableCliente.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tableCliente.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tableCliente.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index += 1

        except Exception as error:

            print('Error en mostrar tabla clientes', error)

    def cargaCli(dni):

        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select direccion, provincia, municipio, sexo, envio from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    for i in range(5):
                        record.append(query.value(i))
                return record

        except Exception as error:
            print('Error en cargar datos de cliente', error)

    def cargarProv(self):
        try:
            record = {}
            query = QtSql.QSqlQuery()
            query.prepare('select * from provincias')
            if query.exec_():
                while query.next():
                    record[query.value(1)] = query.value(0)
                return record
        except Exception as error:
            print('Error en cargar provincias', error)

    def cargarMun(provincia):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select municipio from municipios where provincia_id = :provincia')
            query.bindValue(':provincia', int(provincia))
            if query.exec_():
                while query.next():
                    record.append(query.value(0))
                return record
        except Exception as error:
            print('Error en cargar provincias', error)

    def modifCli(modifcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set alta = :alta, apellido = :apellido, nombre = :nombre, '
                          'direccion = :direccion, provincia = :provincia, municipio = :municipio, sexo = :sexo, '
                          'pago = :pago, envio = :envio where dni = :dni')
            query.bindValue(':dni', str(modifcli[0]))
            query.bindValue(':alta', str(modifcli[1]))
            query.bindValue(':apellido', str(modifcli[2]))
            query.bindValue(':nombre', str(modifcli[3]))
            query.bindValue(':direccion', str(modifcli[4]))
            query.bindValue(':provincia', str(modifcli[5]))
            query.bindValue(':municipio', str(modifcli[6]))
            query.bindValue(':sexo', str(modifcli[7]))
            query.bindValue(':pago', str(modifcli[8]))
            query.bindValue(':envio', str(modifcli[9]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente modificado Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('DNI ni Válido')
                msg.exec()

        except Exception as error:
            print('Error en modificar client', error)

    def importarDatos(clientes):
        try:
            ejecucion = True
            print('a')
            dnis = []
            query = QtSql.QSqlQuery()
            query.prepare('select dni from clientes')
            if query.exec_():
                while query.next():
                    dnis.append(query.value(0))

            for i in range(clientes.nrows - 1):
                c1 = clientes.cell_value(i + 1, 0)
                c2 = clientes.cell_value(i + 1, 1)
                c3 = clientes.cell_value(i + 1, 2)
                c4 = clientes.cell_value(i + 1, 3)
                c5 = clientes.cell_value(i + 1, 4)
                c6 = clientes.cell_value(i + 1, 5)
                if c1 in dnis:
                    query.prepare('update clientes set apellido = :apellido, nombre = :nombre, '
                                  'direccion = :direccion, provincia = :provincia, sexo = :sexo '
                                  'where dni = :dni')
                    query.bindValue(':dni', c1)
                    query.bindValue(':apellido', c2)
                    query.bindValue(':nombre', c3)
                    query.bindValue(':direccion', c4)
                    query.bindValue(':provincia', c5)
                    query.bindValue(':sexo', c6)
                    if query.exec_():
                        ejecucion = True

                else:
                    query.prepare(
                        'insert into clientes (dni, apellido, nombre, direccion, provincia, sexo)'
                        'VALUES (:dni, :apellido, :nombre, :direccion,:provincia, :sexo)')
                    query.bindValue(':dni', c1)
                    query.bindValue(':apellido', c2)
                    query.bindValue(':nombre', c3)
                    query.bindValue(':direccion', c4)
                    query.bindValue(':provincia', c5)
                    query.bindValue(':sexo', c6)
                    if query.exec_():
                        ejecucion = True
            return ejecucion
        except Exception as error:
            print('Error al cargar datos del excel ', error)

    def exportExcel(self):
        try:
            print('a')
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls',
                                                                options=option)
            wb = xlwt.Workbook()
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'APELIDOS')
            sheet1.write(0, 2, 'NOME')
            sheet1.write(0, 3, 'DIRECCION')
            sheet1.write(0, 4, 'PROVINCIA')
            sheet1.write(0, 5, 'SEXO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_() and directorio != '':
                while query.next():
                    sheet1.write(f, 0, query.value(0))
                    sheet1.write(f, 1, query.value(2))
                    sheet1.write(f, 2, query.value(3))
                    sheet1.write(f, 3, query.value(4))
                    sheet1.write(f, 4, query.value(5))
                    sheet1.write(f, 5, query.value(7))
                    f += 1
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Datos exportados con éxito.")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje generado exportar datos ', error)

                wb.save(directorio)

        except Exception as error:
            print('Error en conexion para exportar excel ', error)
    def altaArt(newart):
        try:
            query = QtSql.QSqlQuery()
            print(newart)
            query.prepare(
                'insert into articulos (nombre, precio_unidad)'
                'VALUES (:nombre, :precio_unidad)')
            query.bindValue(':nombre', str(newart[0]))
            query.bindValue(':precio_unidad', str(newart[1]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente insertado Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Fallo al Insertar Articulo')
                msg.exec()
        except Exception as error:
            print('Error en Alta cliente', error)

    def bajaArt(nombre):
        try:
            print(nombre)
            query = QtSql.QSqlQuery()
            query.prepare('delete from articulos where codigo = :codigo')
            query.bindValue(':codigo', str(nombre))
            msg = QtWidgets.QMessageBox()
            if query.exec_():
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo borrado Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Fallo al Borrar Articulo')
                msg.exec()
        except Exception as error:
            print('Error en Baja Articulo', error)

    def cargarTablaArt(self):

        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre ,precio_unidad from articulos order by nombre')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    nombre = query.value(1)
                    precio_unidad = query.value(2)
                    precio_unidad = locale.currency(precio_unidad)
                    var.ui.tableArt.setRowCount(index + 1)
                    var.ui.tableArt.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tableArt.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tableArt.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio_unidad)))
                    index += 1

        except Exception as error:

            print('Error en mostrar tabla articulos', error)

    def buscarTablaArt(nombre):

        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigo ,precio_unidad from articulos where nombre = :nombre')
            query.bindValue(':nombre', str(nombre))
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    precio_unidad = query.value(1)
                    var.ui.tableArt.setRowCount(index + 1)
                    var.ui.tableArt.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tableArt.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tableArt.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio_unidad)))
                    index += 1

        except Exception as error:

            print('Error en mostrar tabla articulos', error)

    def modifArt(modifart):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update articulos set nombre = :nombre, precio_unidad = :precio_unidad where codigo = :codigo')
            query.bindValue(':codigo', str(modifart[0]))
            query.bindValue(':nombre', str(modifart[1]))
            modifart[2] = modifart[2].replace('€', '')
            modifart[2] = modifart[2].replace(',', '.')
            query.bindValue(':precio_unidad', str(modifart[2]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo modificado Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Fallo al Modificar Articulo')
                msg.exec()

        except Exception as error:
            print('Error en modificar articulo', error)


    def buscaNombreFact(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellido, nombre from clientes where dni = :dni')
            query.bindValue( ':dni', str(dni))
            if query.exec_():
                while query.next():
                    registro.append(query.value(1))
                    registro.append(query.value(2))
                return registro
        except Exception as error:
            print('Error en buscar cliente facturacion', error)

    def altaFact(registro):
        try:
            print(registro)
            query= QtSql.QSqlQuery()
            query.prepare('insert into facturas (dni, fechafact) values (:dni, :fechafact)')
            query.bindValue(':dni', str(registro[0]))
            query.bindValue(':fechafact', str(registro[1]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de alta Correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Fallo al Insertar Factura')
                msg.exec()

        except Exception as error:
            print('Error en alta factura', error)

    def cargarTableFact(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codfact, fechafact from facturas')
            if query.exec_():
                while query.next():

                    codigo = str(query.value(0))
                    fecha = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    icopapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setFixedSize(24,24)
                    var.btnfacdel.setIcon(QtGui.QIcon(icopapelera))
                    var.ui.tableFact.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tableFact.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tableFact.setItem(index, 1, QtWidgets.QTableWidgetItem(fecha))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFact)
                    lay_out.setAlignment(QtCore.Qt.AlignVCenter)
                    var.ui.tableFact.setCellWidget(index, 2, cell_widget)
                    var.ui.tableFact.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tableFact.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1

        except Exception as error:
            print('Error en cargar la tabla de facturas', error)

    def bajaFact():

        try:

            numfac = var.ui.lblnumfac.text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(numfac))
            if query.exec_():
                Conexion.cargarTablaFac()
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("La factura ha sido dada de baja")
                msgBox.setWindowTitle("Aviso")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("La factura no ha sido dada de baja. Recuerda seleccionarla antes de eliminarla")
                msgBox.exec()

        except Exception as error:
          print('Error en dar baja factura', error)
    def buscaDNIFact(codfact):
        try:
            print(codfact)
            query= QtSql.QSqlQuery()
            query.prepare('select dni from facturas where codfact = :codfact')
            query.bindValue(':codfact', int(codfact))
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                return dni
        except Exception as error:
            print('Error en buscar DNI', error)

    def cargarCmbProducto(self):
        try:
            var.cmbProducto.clear()
            var.cmbProducto.addItem('')
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from articulos order by nombre')
            if (query.exec_()):
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))
        except Exception as error:
            print('error cargar combo productos',error)

    def obtenerCodPrecio(articulo):
        try:
            dato = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, precio from productos where producto = :articulo')
            query.bindValue(':articulo',str(articulo))
            if query.exec_():
                while (query.next()):
                    dato.append(int(query.value(0)))
                    dato.append(str(query.value(1)))
                
        except Exception as error:
            print('Error en cargar codigo precio', error)

    def cargarVenta(venta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into ventas (factura, articulo, precio, cantidad) '
                          'values (:factura, :articulo, :precio, :cantidad)')
            query.bindValue(':factura', venta[0])
            query.bindValue(':articulo', venta[1])
            query.bindValue(':precio', venta[2])
            query.bindValue(':cantidad', venta[3])
            if query.exec_():
                var.ui.lblVenta.setText("Venta realizada")
                var.ui.lblVenta.setStyleSheet('QLabel {color: green;}')
                Conexion.cargarLineasVenta(venta[0])
            else:
                var.ui.lblVenta.setText("Error en venta")
                var.ui.lblVenta.setStyleSheet('QLabel {color: red;}')

        except Exception as error:
            print('Error al cargar venta ', error)

    def cargarLineasVenta(factura):
        try:

            suma = 0.0
            var.ui.tableVentas.clearContents()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codventa, precio, cantidad, articulo from ventas where factura = :factura')
            query.bindValue(':factura', int(factura))
            if query.exec_():
                while query.next():
                    codventa = query.value(0)
                    precio = str(query.value(1))
                    cantidad = str(query.value(2))
                    prod = query.value(3)

                    producto = Conexion.buscaArt(prod)

                    suma = suma + (float(precio) * float(cantidad))
                    var.ui.tableVentas.setRowCount(index + 1)
                    var.ui.tableVentas.setItem(index,0, QtWidgets.QTableWidgetItem(str(codventa)))
                    var.ui.tableVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tableVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(producto)))
                    var.ui.tableVentas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tableVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio + '€')))
                    var.ui.tableVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignRight)
                    var.ui.tableVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(cantidad)))
                    var.ui.tableVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tableVentas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(float(precio) * float(cantidad))+ '€'))
                    var.ui.tableVentas.item(index, 4).setTextAlignment(QtCore.Qt.AlignRight)
                    index = index + 1
            facturacion.Facturacion.cargaLineaVenta(index)
            iva = suma * 0.21
            total = suma + iva
            var.ui.lblSubTotal.setText(str(round(suma,2)) + '€')
            var.ui.lblIva.setText(str(round(iva, 2)) + '€')
            var.ui.lblTotal.setText(str(round(total, 2)) + '€')

        except Exception as error:
            print('error cargar las lines de factura', error)

    def buscaArt(prod):
        try:
            query2 = QtSql.QSqlQuery()
            query2.prepare('select nombre from productos where codigo = :codigo')
            query2.bindValue(':codigo', int(prod))
            if query2.exec_():
                while query2.next():
                    producto = query2.value(0)

            return producto

        except Exception as error:
            print('error cargar las líneas de venta', error)

    def borrarVenta(self):
        try:
            row = var.ui.tabVentas.selectedItems()
            codVenta = row[0].text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codventa = :codventa')
            query.bindValue(':codventa', int(codVenta))
            if query.exec_():
                facturacion.Facturacion.cargaFac(self)
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Venta eliminada')
                msg.exec()

        except Exception as error:
            print('Error al borrar una venta ', error)