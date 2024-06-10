class Alfabeto:
    def __init__(self):
        # Criando uma lista com as letras do alfabeto
        self.letras = [chr(i) for i in range(97, 123)]

    def indice_para_letra(self, indice):
        if 1 <= indice <= 26:
            return self.letras[indice - 1]
        else:
            return ''

# Testes
alfabeto = Alfabeto()

# Teste para índices válidos
for i in range(1, 27):
    print(f"Letra correspondente ao índice {i}: {alfabeto.indice_para_letra(i)}")

# Teste para índices inválidos
print("Letra correspondente ao índice 0:", alfabeto.indice_para_letra(0))
print("Letra correspondente ao índice 27:", alfabeto.indice_para_letra(27))
