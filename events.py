import var


class Eventos():
    def Salir(self):
        try:
            var.ui.lblTitulo.setText('Hola mundo')
        except Exception as error:
            print("Error en módulo salir")