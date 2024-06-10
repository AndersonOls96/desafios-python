class FormatarPercentual:
    def __init__(self):
        self.aumento_vendas = 0

    def definir_aumento_vendas(self, aumento):
        self.aumento_vendas = aumento

    def exibir_aumento_formatado(self):
        aumento_formatado = "{:.2f}%".format(self.aumento_vendas)
        return aumento_formatado
    
# Teste da classe
formatador = FormatarPercentual()
formatador.definir_aumento_vendas(8.9)
print(formatador.exibir_aumento_formatado())  # Saída esperada: 8.90%
