class Alfabeto:
    def __init__(self):
       self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     

    def indice_para_letra(self, indice):
        if 1 <= indice <= 26:
            return self.alfabeto[indice - 1]
        else:
            return ''