from claseFechaHora import FechaHora

def test():

    anio=2000; mes=12 ; dia =28; hora = 22; minuto=2; segundo=20
    print('1er Fecha: año={} mes={} dia={} hora={} minuto={} segundo={} '.format(anio,mes,dia,hora,minuto,segundo))
    fecha1= FechaHora(dia,mes,anio,hora,minuto,segundo)
    fecha1.Mostrar()

    anio = 2001; mes = 2; dia = 29; hora = 22; minuto = 2; segundo = 20
    print('2da Fecha: año={} mes={} dia={} hora={} minuto={} segundo={} '.format(anio, mes, dia, hora, minuto, segundo))
    fecha2= FechaHora(dia,mes,anio,hora,minuto,segundo)
    fecha2.Mostrar()


if __name__ == '__main__':
    p =input('Desea ejecutar test?: 1:si 2:no   :')
    if p =='1':
        test()

    d = int(input("Ingrese Dia: "))

    mes = int(input("Ingrese Mes: "))

    a = int(input("Ingrese Año: "))

    h = int(input("Ingrese Hora: "))

    m = int(input("Ingrese Minutos: "))

    s = int(input("Ingrese Segundos: "))


    r = FechaHora()  # inicilizar día, mes, año con 1/1/2020, y hora, minutos y

    r1 = FechaHora(d, mes, a)  # inicializar con 0h 0m 0s

    r2 = FechaHora(d, mes, a, h, m, s)

    r.Mostrar()

    r1.Mostrar()
    print('Fecha ingresada por teclado: ')
    r2.Mostrar()


    input()

    r.PonerEnHora(5)  # solamente la hora

    r.Mostrar()

    input()

    #r2.PonerEnHora(13, 30)  # hora y minutos

    r2.Mostrar()

    input()

    r.PonerEnHora(14, 30, 25)  # hora, minutos y segundos

    r.Mostrar()

    input()

    r.AdelantarHora(3)  # sumar 3 horas a la hora actual

    r.ajustarFecha()

    r.Mostrar()

    input()

    r1.AdelantarHora(1, 15)  # sumar 1 hora y 15 minutos a la hora actual

    r1.ajustarFecha()

    r1.Mostrar()

    input()

    r2.AdelantarHora(2,20)
    r2.ajustarFecha()
    r2.Mostrar()