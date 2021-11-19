from PyQt5 import QtSql, QtWidgets

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
                msg.setText('DNI ni Válido')
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
            query.prepare('select direccion, provincia, municipio, sexo from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    for i in range(4):
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
                          'pago = :pago where dni = :dni')
            query.bindValue(':dni', str(modifcli[0]))
            query.bindValue(':alta', str(modifcli[1]))
            query.bindValue(':apellido', str(modifcli[2]))
            query.bindValue(':nombre', str(modifcli[3]))
            query.bindValue(':direccion', str(modifcli[4]))
            query.bindValue(':provincia', str(modifcli[5]))
            query.bindValue(':municipio', str(modifcli[6]))
            query.bindValue(':sexo', str(modifcli[7]))
            query.bindValue(':pago', str(modifcli[8]))
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
                if c1 in dnis and clientes.Clientes.validarDNI():
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
