from datetime import datetime
import calendar
#https://www.geeksforgeeks.org/calendar-in-python/
#https://www.w3schools.com/python/python_datetime.asp

class Data:
    def __init__(self, data: str) -> None:
        self.data = data
        self.data_atual = datetime.today().strftime('%d-%m-%Y')
    
    def data_correta(self):
        if self.data != self.data_atual:
            self.data = '01-01-0001'
            return self.data
        else:
            return self.data
    
    def getDia(self):
        data_objeto = self.data
        dia = data_objeto.split('-')
        return dia[0]
    
    def getMes(self):
        data_objeto = self.data
        mes = data_objeto.split('-')
        return mes[1]

    def getMesExtenso(self):
        data_objeto = self.data
        mes = data_objeto.split('-')[1]
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        
        mes_extenso = meses[int(mes) - 1] #associando o mes á lista de meses
        return mes_extenso
    
    def validar_datas(self):
        dia, mes, ano = map(int, self.data.split('-'))
        ultimo_dia = calendar.monthrange(ano, mes)[1]
        print(ultimo_dia)
        if not (1 <= mes <= 12) or not (1 <= dia <= ultimo_dia ):
            raise ValueError("data invalida")
    
    def getAno(self):
        data_objeto = self.data
        ano = data_objeto.split('-')[2]
        return ano
    
    def isBissexto(self):
        ano_atual = self.getAno()
        ano_convertido = int(ano_atual)
        if ano_convertido % 4 == 0 or ano_convertido % 400 == 0:
            return True
        return False

    def clone(self):
        criar_objeto = Data(self.data).data
        return criar_objeto
    
    def compara(self, objeto_data):
        tranformar_atual = datetime.strptime(self.data_atual, '%d-%m-%Y').date()
        transformar_objeto = datetime.strptime(objeto_data.data, '%d-%m-%Y').date()

        if tranformar_atual == transformar_objeto:
            return 0
        
        elif tranformar_atual > transformar_objeto:
            return 1
        
        elif tranformar_atual < transformar_objeto:
            return -1

if __name__ == '__main__':
    teste1 = Data('23-09-2023')
    teste2 = Data('22-08-2023')
    print(teste1.compara(teste2))
    teste1.validar_datas()
    print(teste1.data)
    print(teste1.data_atual)
    #(teste1.data_correta())
    print(teste1.getDia())
    print(teste1.getMes())
    print(teste1.getAno())
    print(teste1.getMesExtenso())
    print(teste1.isBissexto())
    print(teste1.clone())

