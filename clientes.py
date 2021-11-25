import conexion
from window import *
import var


class Clientes():
    
    def validarDNI():
        try:
            global dnivalido
            dnivalido = False
            dni = var.ui.txtDni.text()
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color: green}')
                    var.ui.lblValidoDni.setText('V')
                    var.ui.txtDni.setStyleSheet('background-color: rgb(255, 255, 255)')
                    dnivalido = True
                else:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color: red}')
                    var.ui.lblValidoDni.setText('X')
                    var.ui.txtDni.setStyleSheet('background-color: rgb(255, 0, 0)')
                    dnivalido = False
            else:
                var.ui.lblValidoDni.setStyleSheet('QLabel {color: red}')
                var.ui.lblValidoDni.setText('X')
                var.ui.txtDni.setStyleSheet('background-color: rgb(255, 150, 150)')
                dnivalido = False
            return dnivalido
        except Exception as error:
            print("Error en modulo dni", error)

    # def selSexo(self):
    #     try:
    #         if var.ui.rbtFem.isChecked():
    #             print('Marcado Femenino')
    #         if var.ui.rbtHom.isChecked():
    #             print('Marcado Masculino')
    #     except Exception as error:
    #         print('Error en modulo seleccionar sexo',error)

    # def selPago(self):
    #     try:
    #         if var.ui.chkEfectivo.isChecked():
    #             print ('Has marcado efectivo')
    #         if var.ui.chkTarjeta.isChecked():
    #             print('Has marcado tarjeta')
    #         if var.ui.chkCargoCuenta.isChecked():
    #             print('Has marcado cargo cuenta')
    #         if var.ui.chkTransferencia.isChecked():
    #             print('Has marcado transferencia')
    #     except Exception as error:
    #         print('Error en modulo seleccionar sexo', error)

    def cargaProv(self):

        try:

            var.ui.cmbProv.clear()
            Clientes.prov = conexion.Conexion.cargarProv(self)
            provincias = list(Clientes.prov.keys())
            var.ui.cmbProv.addItem('')
            for i in provincias:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en modulo cargar provincia', error)

    def cargaMun(self):

        try:

            var.ui.cmbMun.clear()
            mun = Clientes.prov[var.ui.cmbProv.currentText()]
            municipios = conexion.Conexion.cargarMun(mun)
            var.ui.cmbMun.addItem('')
            for i in municipios:
                var.ui.cmbMun.addItem(i)

        except Exception as error:
            print('Error en modulo cargar provincia', error)

    # def selProv(prov):
    #     try:
    #         print ('has seleccionado la provincia de ', prov)
    #         return prov
    #     except Exception as error:
    #         print('Error en modulo selecionar provincia', error)

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    def priMay():
        try:
            nome = var.ui.txtNome.text()
            var.ui.txtNome.setText(nome.title())
            nome = var.ui.txtApel.text()
            var.ui.txtApel.setText(nome.title())
        except Exception as error:
            print('Error en modulo primera Mayuscula', error)

    def envio(self):
        try:
            if var.ui.spinEnvio.value() == 0:
                var.ui.lblRecogida.setText('Recogida por cliente')
            elif var.ui.spinEnvio.value() == 1:
                var.ui.lblRecogida.setText('Envío Nacional Paquetería Express Urgente')
            elif var.ui.spinEnvio.value() == 2:
                var.ui.lblRecogida.setText('Envío Nacional Paquetería Normal')
            elif var.ui.spinEnvio.value() == 3:
                var.ui.lblRecogida.setText('Envío Interncional')
        except Exception as error:
            print('Error en modulo envío', error)


    def guardaCli(self):
        try:
            if dnivalido:
                newcli = []
                cliente = [var.ui.txtDni, var.ui.txtFechaAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
                for i in cliente:
                    newcli.append(i.text())
                newcli.append(var.ui.cmbProv.currentText())
                newcli.append(var.ui.cmbMun.currentText())
                if var.ui.rbtHom.isChecked():
                    newcli.append('Hombre')
                elif var.ui.rbtFem.isChecked():
                    newcli.append('Mujer')
                else:
                    newcli.append('')
                pagos = []
                if var.ui.chkCargoCuenta.isChecked():
                    pagos.append('Cargo Cuenta')
                if var.ui.chkTarjeta.isChecked():
                    pagos.append('Tarjeta')
                if var.ui.chkEfectivo.isChecked():
                    pagos.append('Efectivo')
                if var.ui.chkTransferencia.isChecked():
                    pagos.append('Transferencia')
                newcli.append('; '.join(pagos))
                newcli.append(var.ui.spinEnvio.value())
                print(newcli)
                conexion.Conexion.altaCli(newcli)
                conexion.Conexion.cargarTablaCli(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI no Válido')
                msg.exec()
        except Exception as error:
            print('Error en modulo guardar cliente', error)

    def modifCli(self):
        try:
            modifcli = []
            cliente = [var.ui.txtDni, var.ui.txtFechaAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            for i in cliente:
                modifcli.append(i.text())
            modifcli.append(var.ui.cmbProv.currentText())
            modifcli.append(var.ui.cmbMun.currentText())
            if var.ui.rbtHom.isChecked():
                modifcli.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                modifcli.append('Mujer')
            else:
                modifcli.append('')
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTransferencia.isChecked():
                pagos.append('Transferencia')
            pagos = set(pagos)
            modifcli.append('; '.join(pagos))
            modifcli.append(var.ui.spinEnvio.value())
            conexion.Conexion.modifCli(modifcli)
            conexion.Conexion.cargarTablaCli(self)

        except Exception as error:
            print('Error en modificar datos de cliente', error)

    def bajaCli(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargarTablaCli(self)
        except Exception as error:
            print('Error en modulo borrar cliente', error)

    def limpiaFrormCli(self):
        try:
            cajas = [var.ui.txtDni, var.ui.txtNome, var.ui.txtApel, var.ui.txtFechaAltaCli, var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.cmbMun.setCurrentText('')
            var.ui.cmbProv.setCurrentText('')
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkTransferencia.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
        except Exception as error:
            print('Error en modulo limpiar formulario', error)

    def cargaCli(self):
        try:
            fila = var.ui.tableCliente.selectedItems()
            datos = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAltaCli]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            if 'Efectivo' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            else:
                var.ui.chkEfectivo.setChecked(False)
            if 'Transferencia' in row[4]:
                var.ui.chkTransferencia.setChecked(True)
            else:
                var.ui.chkTransferencia.setChecked(False)
            if 'Tarjeta' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            else:
                var.ui.chkTarjeta.setChecked(False)
            if 'Cargo Cuenta' in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)
            else:
                var.ui.chkCargoCuenta.setChecked(False)
            registro = conexion.Conexion.cargaCli(row[0])
            var.ui.txtDir.setText(registro[0])
            var.ui.cmbProv.setCurrentText(registro[1])
            var.ui.cmbMun.setCurrentText(registro[2])
            if registro[3] == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            elif registro[3] == 'Mujer':
                var.ui.rbtFem.setChecked(True)
            var.ui.spinEnvio.setValue(registro[4])
        except Exception as error:
            print('Error en cargar datos de cliente', error)
