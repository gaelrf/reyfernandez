import locale

import clientes
import articulo
import conexion
import informes
from window import *
from aviso import *
from windowcal import *
import sys, var, events
from datetime import *
locale.setlocale(locale.LC_ALL, 'es-ES')


class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_Dialog()
        var.dlgaviso.setupUi(self)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_DialogCal()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        annoactual = datetime.now().year
        var.dlgcalendar.calendar.setSelectedDate((QtCore.QDate(annoactual, mesactual, diaactual)))
        var.dlgcalendar.calendar.clicked.connect(clientes.Clientes.cargarFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):

        super(FileDialogAbrir, self).__init__()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargarTablaCli(self)
        conexion.Conexion.cargarTablaArt(self)

        var.ui.btnSalir.clicked.connect(events.Eventos.salir)
        var.ui.btnCalen.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnGrabaCli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnLimpiaForm.clicked.connect(clientes.Clientes.limpiaFrormCli)
        var.ui.btnBajaCli.clicked.connect(clientes.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clientes.Clientes.modifCli)
        var.ui.btnSalirArt.clicked.connect(events.Eventos.salir)
        var.ui.btnGrabaArt.clicked.connect(articulo.Articulo.guardaArt)
        var.ui.btnBajaArt.clicked.connect(articulo.Articulo.bajaArt)
        var.ui.btnModifArt.clicked.connect(articulo.Articulo.modifArt)
        var.ui.btnBuscaArt.clicked.connect(articulo.Articulo.buscaArt)

        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.abrir)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionBarImprimir.triggered.connect(events.Eventos.imprimir)
        var.ui.actionImportar_Datos.triggered.connect(events.Eventos.importarDatos)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.exportarDatos)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listadoClientes)

        var.ui.txtDni.editingFinished.connect(clientes.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clientes.Clientes.priMay)
        var.ui.txtApel.editingFinished.connect(clientes.Clientes.priMay)
        var.ui.spinEnvio.valueChanged.connect(clientes.Clientes.envio)

        clientes.Clientes.cargaProv(self)
        var.ui.cmbProv.currentIndexChanged.connect(clientes.Clientes.cargaMun)

        events.Eventos.resizeTableCli(self)
        events.Eventos.resizeTableArt(self)
        var.ui.tableCliente.clicked.connect(clientes.Clientes.cargaCli)
        var.ui.tableCliente.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tableArt.clicked.connect(articulo.Articulo.cargaArt)
        var.ui.tableArt.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha)
        day=datetime.now()
        var.ui.lblFecha.setText(day.strftime('%A, %d de %B de %Y').capitalize())

        var.ui.actionBarSalir.triggered.connect(events.Eventos.salir)
        var.ui.actionBarAbrir.triggered.connect(events.Eventos.abrir)
        var.ui.actionBarCrearBackup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionBarRestaurarBackup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionBarImprimir.triggered.connect(events.Eventos.imprimir)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width())//2
    y = (desktop.height() - window.height())//2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
