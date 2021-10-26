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
            pass
        except Exception as error:
            print('Error en Alta cliente' , error)