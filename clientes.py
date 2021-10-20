'''

'''
from window import *
import var

class Clientes():

    def validarDNI():

        try:
            global dnivalido
            dnivalido = False
            dni = var.ui.txtDni.text()
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'   #
            dig_ext = 'XYZ'                     #
            reemp_dig_ext = { 'X':'0', 'Y':'1', 'Z':'2'}
            numeros = '1234567890'
            dni = dni.upper()   #Convertir Letra a Mayusculas
            var.ui.txtDni.setText(dni)
            if len(dni) == 9:

                dig_control = dni[8]
                dni =dni[:8]

                if dni[0] in dig_ext:

                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) %23] == dig_control:

                    var.ui.lblValidoDni.setStyleSheet('QLabel {color: green}')
                    var.ui.lblValidoDni.setText('V')
                    var.ui.txtDni.setStyleSheet('background-color: rgb(255, 255, 255)')
                    dnivalido=True
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

        except Exception as error:

            print("Error en modulo dni", error)
    def selSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcado Femenino')
            if var.ui.rbtHom.isChecked():
                print('Marcado Masculino')
        except Exception as error:
            print('Error en modulo seleccionar sexo',error)

    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print ('Has marcado efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Has marcado tarjeta')
            if var.ui.chkCargoCuenta.isChecked():
                print('Has marcado cargo cuenta')
            if var.ui.chkTransferencia.isChecked():
                print('Has marcado transferencia')
        except Exception as error:
            print('Error en modulo seleccionar sexo', error)
    def cargaProv(self):
        try:
            var.ui.cmbProv.clear()
            prov = ['','A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en modulo cargar provincia', error)
    def selProv(prov):
        try:
            print ('has seleccionado la provincia de ', prov)
            return prov
        except Exception as error:
            print('Error en modulo selecionar provincia', error)
    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtFechaAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha', error)
    def priMay():
        try:
            nome=var.ui.txtNome.text()
            var.ui.txtNome.setText(nome.title())
            nome=var.ui.txtApel.text()
            var.ui.txtApel.setText(nome.title())
        except Exception as error:
            print('Error en modulo primera Mayuscula', error)
    def guardaCli(self):
        try:
            if dnivalido :
                newcli = []
                tablecli=[]
                client =[var.ui.txtDni,var.ui.txtApel,var.ui.txtNome,var.ui.txtFechaAltaCli]
                for i in client:
                    tablecli.append(i.text())
                pagos = []
                if var.ui.chkCargoCuenta.isChecked():
                    pagos.append('Cargo Cuenta')
                if var.ui.chkTarjeta.isChecked():
                    pagos.append('Tarjeta')
                if var.ui.chkEfectivo.isChecked():
                    pagos.append('Evectivo')
                if var.ui.chkTransferencia.isChecked():
                    pagos.append('Transferencia')
                #pagos= set(pagos)
                tablecli.append('; '.join(pagos))
                row = 0
                colum=0
                var.ui.tableCliente.insertRow(row)
                for campo in tablecli:
                    cell =QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tableCliente.setItem(row, colum,cell)
                    colum += 1
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI ni Válido')
                msg.exec()
        except Exception as error:
            print('Error en modulo guardar cliente', error)
    def limpiaFrormCli(self):
        try:
            cajas = [var.ui.txtDni,var.ui.txtNome,var.ui.txtApel,var.ui.txtFechaAltaCli,var.ui.txtDir]
            for i in cajas:
                i.setText('')

        except Exception as error:
            print('Error en modulo limpiar formulario', error)
