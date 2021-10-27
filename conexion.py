from PyQt5 import QtSql, QtWidgets

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
                print ('Conexion establecida')
                return True
        except Exception as error:
            print ('Problemas en conexion', error)
    def altaCli(newcli):
        try:
            print(newcli)
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, alta, apellido, nombre, direccion, provincia, municipio, sexo, pago)'
                          'VALUES (:dni, :alta, :apellido, :nombre, :direccion, :provincia, :municipio, :sexo, :pago)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':alta', str(newcli[1]))
            query.bindValue(':apellido', str(newcli[2]))
            query.bindValue(':nombre', str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            if query.exec_():
                print ('Insercion corredta')
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('DNI ni Válido')
                msg.exec()
        except Exception as error:
            print('Error en Alta cliente' , error)