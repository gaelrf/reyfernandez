import os.path
import sys
import zipfile
import shutil
from datetime import datetime

import xlrd as xlrd
from PyQt5 import QtPrintSupport
from PyQt5.QtWidgets import QMessageBox

import conexion
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
            print('Error al abrir el calendario ', error)

    def resizeTableArt(self):
        try:
            header = var.ui.tableArt.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        except Exception as error:
            print('Error en el modulo redimensionar tabla ', error)

    def resizeTableFact(self):
        try:
            header = var.ui.tableFact.horizontalHeader()
            for i in range(2):
                header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)
        except Exception as error:
            print('Error en el modulo redimensionar tabla ', error)

    def resizeTableCli(self):
        try:
            header = var.ui.tableCliente.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en el modulo redimensionar tabla ',error)

    def resizeTableVentas(self):
        try:
            header = var.ui.tableVentas.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)
                if i == 1 or i == 3:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error en el modulo redimensionar tabla ',error)

    def abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error en el modulo abrir archivo ',error)

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha)+'_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia,
                                                                '.zip', options=option)
            if var.dlgabrir.Accepted and filename !='':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Base de datos guardada correctamente')
                msg.exec()
        except Exception as error:
            print('Error en el modulo crear backup ',error)
    def restaurarBackup (self):
        try:
            dirpro = os.getcwd()
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad', '','*.zip;;All',options=option)
            if var.dlgabrir.Accepted and filename!=0:
                file= filename[0]
                with zipfile.ZipFile(str(file), 'r') as dbdb:
                    dbdb.extractall()
                dbdb.close()
                # shutil.move('dbdb.sqlite',str(dirpro))
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTablaCli(self)
        except Exception as error:
            print('Error en el modulo restaurar backup ',error)

    def imprimir(self):
        try:
            printdialog = QtPrintSupport.QPrintDialog()
            if printdialog.exec_():
                printdialog.show()
        except Exception as error:
            print('Error en el modulo imprimir ',error)



    def importarDatos(self):
        try:
            dirpro = os.getcwd()
            print(dirpro)
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Cargar datos desde Excel', "", '*.xls;;All ',options=option)
            print(filename)
            documento = xlrd.open_workbook(filename[0])
            clientes = documento.sheet_by_index(0)
            filas_clientes = clientes.nrows
            columnas_clientes = clientes.ncols
            print("Filas: " + str(filas_clientes) + ". Columnas: " + str(columnas_clientes))

            if var.dlgabrir.Accepted and filename != "":
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Confirmar')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('¿Estás seguro de seleccionar este archivo?')
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec()
                if msg.clickedButton() == msg.button(msg.StandardButton.Ok):
                   ejecucion = conexion.Conexion.importarDatos(clientes)
                   if ejecucion:
                       conexion.Conexion.cargarTablaCli(self)
                else:
                    print("Importación cancelada")
        except Exception as error:
            print('Error al cargar dato del excel ', error)


    def exportarDatos(self):
        try:
            conexion.Conexion.exportExcel(self)
        except Exception as error:
            print('Error en evento exportar datos ', error)