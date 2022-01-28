import os,var
from datetime import datetime
from PyQt5 import QtSql
from reportlab.pdfgen import canvas

import conexion


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

    def listadoProductos (self):
        try:
            textotitulo = 'LISTADO PRODUCTOS'
            var.cv = canvas.Canvas('informes\listadoclientes.pdf')
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Departamento de Administracion')
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            var.cv.setFont('Helvetica-Bold',size=9)
            var.cv.line(40,700,530,700)
            var.cv.drawString(255, 690, textotitulo)
            var.cv.line(40,685,530,685)
            items = ['Codigo', 'Articulo', 'Precio']
            var.cv.drawString(65,675,items[0])
            var.cv.drawString(210,675,items[1])
            var.cv.drawString(370,675,items[2])
            var.cv.line(40,670,530,670)
            var.cv.setFont('Helvetica', size = 8)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio_unidad from articulos order by nombre')
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
                        var.cv.drawRightString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        Informes.pie(textotitulo)
                        var.cv.setFont('Helvetica', size=8)
                        y = 655
                    var.cv.drawString(x, y, str(query.value(0)))
                    var.cv.drawString(x+140,y , str(query.value(1)))
                    var.cv.drawString(x+310, y, str(query.value(2)))
                    y = y-15
            var.cv.save()
            rootpath = '.\\informes'
            cont = 0
            for file in os.listdir(rootpath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootpath,file))
                cont = cont + 1
        except Exception as error:
            print('Error en modulo listar productos, ', error)

    def factura(self):
        try:
            var.cv = canvas.Canvas('informes/factura.pdf')
            var.cv.setTitle('Factura')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold',size=12)
            textotitulo = 'FACTURA'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            codfac = var.ui.lblNumfac.text()
            var.cv.drawString(260, 694, textotitulo+': '+(str(codfac)))
            var.cv.line(30, 685, 550, 685)
            items = ['Venta', 'Articulo', 'Precio', 'Cantidad', 'Total']
            var.cv.drawString(65, 673, items[0])
            var.cv.drawString(165, 673, items[1])
            var.cv.drawString(270, 673, items[2])
            var.cv.drawString(380, 673, items[3])
            var.cv.drawString(490, 673, items[4])
            suma = 0.0
            query = QtSql.QSqlQuery()
            query.prepare('select codven,precio,cantidad,codpro from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    codventa = query.value(0)
                    precio = query.value(1)
                    cantidad = query.value(2)
                    nombre = conexion.Conexion.buscaArt(int(query.value(3)))
                    total = round(precio * cantidad, 2)
                    suma += total
                    var.cv.setFont('Helvetica', size=9)
                    var.cv.drawString(i + 20, j, str(query.value(0)))
                    var.cv.drawString(i + 100, j, str(nombre))
                    var.cv.drawString(i + 219, j, str(precio)+'€/kg')
                    var.cv.drawString(i + 340, j, str(cantidad))
                    var.cv.drawString(i + 442, j, str(total))
                    j = j - 20
            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error creación informe facturas', error)