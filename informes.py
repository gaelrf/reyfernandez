import os,var
from datetime import datetime
from PyQt5 import QtSql
from reportlab.pdfgen import canvas

class Informes():

    def listadoClientes(self):

        try:
            textotitulo = 'LISTADO CLIENTES'
            var.cv = canvas.Canvas('informes\listadoclientes.pdf')
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Departamento de Administracion')
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            var.cv.setFont('Helvetica-Bold',size=9)
            var.cv.line(40,700,530,700)
            var.cv.drawString(255, 690, textotitulo)
            var.cv.line(40,685,530,685)
            items = ['DNI', 'Nombre', 'Formas de Pago']
            var.cv.drawString(65,675,items[0])
            var.cv.drawString(210,675,items[1])
            var.cv.drawString(370,675,items[2])
            var.cv.line(40,670,530,670)
            var.cv.setFont('Helvetica', size = 8)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellido, nombre, pago from clientes order by apellido, nombre')
            if query.exec_():
                x=50
                y=655
                while query.next():
                    if y<= 80:
                        var.cv.setFont('Helvetica', size=6)
                        var.cv.drawString(460,30,'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        var.cv.setFont('Helvetica-Bold', size=9)
                        var.cv.line(40, 700, 530, 700)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de Pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        Informes.pie(textotitulo)
                        var.cv.setFont('Helvetica', size=8)
                        y = 655
                    var.cv.drawString(x, y, str(query.value(0)))
                    var.cv.drawString(x+140,y , str(query.value(1) + ', ' + query.value(2)))
                    var.cv.drawString(x+310, y, str(query.value(3)))
                    y = y-15
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
            var.cv.line(40,800,530,800)
            var.cv.setFont('Helvetica-Bold',14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50,770,'CIF:A0000000H')
            var.cv.drawString(50,755,'Dirección: Avenida de Galicia 101')
            var.cv.drawString(50,740,'Vigo-36216-Spain')
            var.cv.drawString(50,725,'e-mail: micorreo@gmail.com')
            var.cv.drawImage(logo, 425,720)
            var.cv.line(40,710,530,710)
        except Exception as error:
            print('Error en modulo cabecera, ', error)

    def pie (texto):
        try:
            var.cv.line(40,50,530,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y  %H:%M:%S')
            var.cv.setFont('Helvetica', size= 6)
            var.cv.drawString(70,40,str(fecha))
            var.cv.drawString(255, 40, str(texto))
            var.cv.drawString(500,40, str('Página %s' % var.cv.getPageNumber()))
        except Exception as error:
            print('Error en pie de informe clientes ', error)
