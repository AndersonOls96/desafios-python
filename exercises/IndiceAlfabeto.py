class Alfabeto:
    def __init__(self):
        self.letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def indice_para_letra(self, indice):
        if 1 <= indice <= 26:
            return self.letras[indice - 1]
        else:
            return ''