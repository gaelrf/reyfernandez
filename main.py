import locale

import clientes
import conexion
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

        var.ui.btnSalir.clicked.connect(events.Eventos.salir)
        var.ui.btnCalen.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnGrabaCli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnLimpiaForm.clicked.connect(clientes.Clientes.limpiaFrormCli)
        var.ui.btnBajaCli.clicked.connect(clientes.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clientes.Clientes.modifCli)

        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.abrir)

        var.ui.txtDni.editingFinished.connect(clientes.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clientes.Clientes.priMay)
        var.ui.txtApel.editingFinished.connect(clientes.Clientes.priMay)

        clientes.Clientes.cargaProv(self)
        var.ui.cmbProv.currentIndexChanged.connect(clientes.Clientes.cargaMun)

        events.Eventos.resizeTableCli(self)
        var.ui.tableCliente.clicked.connect(clientes.Clientes.cargaCli)
        var.ui.tableCliente.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha)
        day=datetime.now()
        var.ui.lblFecha.setText(day.strftime('%A, %d de %B de %Y').capitalize())


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
