class FechaHora:
    __segundo=0
    __minuto=0
    __hora=0
    __dia =0
    __mes=0
    __anio=0
    def __init__(self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):

        if self.validarDato(dia,mes,anio,hora,minuto,segundo): # si devuelve true se ejecuta
            self.__segundo = segundo
            self.__minuto = minuto
            self.__hora = hora
            self.__dia = dia
            self.__mes = mes
            self.__anio = anio
            print('Fecha valida')
        else:
            print('Fecha invalida, devuelve todo 0')



    def validarDato(self,dia,mes,anio,hora,minuto,segundo):
        bandera = False
        if segundo in range(0,60):
            if minuto in range(0,60):
                if hora in range(0,24):
                    if anio > 0:
                        if mes in range(1,13):
                            if mes == 2:
                                bisiesto = self.anioBisiesto(anio)
                                if not bisiesto:
                                    if dia in range(1,29):
                                        bandera = True
                                elif dia in range(1,30):
                                    bandera = True
                            if mes in [1, 3, 5, 7, 8, 10, 12]:
                                if dia in range(1, 32):
                                    bandera = True
                            if mes in [4,6,9,11]:
                                if dia in range(1,31):
                                    bandera = True
        return bandera




    def ajustarFecha(self):
        bandera= False
        bandera = self.anioBisiesto(self.__anio)
        if self.__segundo >= 60:
            entero = self.__segundo // 60
            resto = self.__segundo % 60

            self.__minuto += entero
            self.__segundo = resto
        if self.__minuto >= 60:
            entero = self.__minuto // 60
            resto = self.__minuto % 60
            self.__hora += entero
            self.__minuto = resto
        if self.__hora >= 24:
            entero = self.__hora // 24
            resto = self.__hora % 24
            self.__dia += entero
            self.__hora = resto
        if self.__mes in [1,3,5,7,8,10,12]:
            if self.__dia > 31:
                self.__mes+=1
                self.__dia -= 31
        if self.__mes in [4,6,9,11]:
            if self.__dia > 30:
                self.__mes +=1
                self.__dia -=30

        if self.__mes == 2:
            if not bandera:
                if self.__dia > 28:
                    self.__mes +=1
                    self.__dia -=28
            elif self.__dia > 29:
                self.__mes += 1
                self.__dia -= 29

        if self.__mes > 12:
            entero = self.__mes // 12
            resto = self.__mes % 12
            self.__anio += entero
            self.__mes = resto


    def Mostrar(self):
        print('La hora es {}:{}:{} con fecha {}/{}/{} '.format(self.__hora,self.__minuto,self.__segundo,self.__dia,self.__mes,self.__anio))

    def PonerEnHora(self,hora=0,minuto=0,segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def anioBisiesto(self,anio):
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            print('Es año biciesto')
            return True
        else:print('No es año biciesto')

    def AdelantarHora(self,hora=0,minuto=0,segundo=0):
        self.__hora += hora
        self.__minuto += minuto
        self.__segundo += segundo