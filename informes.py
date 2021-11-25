import os,var
from reportlab.pdfgen import canvas

class Informes():

    def listadoClientes(self):

        try:
            var.cv = canvas.Canvas('informes\listadoclientes.pdf')
            Informes.cabecera(self)
            var.cv.setFont('Helvetica',8)
            var.cv.setTitle('Listado Clientes')
            var.cv.save()
            rootpath = '.\\informes'
            cont = 0
            for file in os.listdir(rootpath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootpath,file))
                cont = cont + 1
        except Exception as error:
            print('Error en modulo listar clientes, ', error)

    def cabecera(self):
        try:
            logo = '.\\img\calendario.png'
            var.cv.line(40,800,500,800)
            var.cv.setFont('Helvetica-Bold',14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50,770,'CIF:A0000000H')
            var.cv.drawString(50,755,'Dirección: Avenida de Galicia 101')
            var.cv.drawString(50,740,'Vigo-36216-Spain')
            var.cv.drawString(50,725,'e-mail: micorreo@gmail.com')
            var.cv.drawImage(logo, 425,720)
            var.cv.line(40,710,500,710)
        except Exception as error:
            print('Error en modulo cabecera, ', error)
