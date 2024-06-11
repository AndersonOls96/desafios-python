class Alfabeto:
    def __init__(self):
        # Adicione os atributos necessários
        # Dica: você pode adicionar as letras do alfabeto em uma lista
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def indice_para_letra(self, indice):
        if 1 <= indice <= 26:
            return self.alfabeto[indice - 1] # Implemente o método indice_para_letra
        else: 
            return ''