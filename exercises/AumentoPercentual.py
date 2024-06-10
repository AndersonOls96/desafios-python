class FormatarPercentual:
    def __init__(self):
        # Adicione o(s) atributo(s) necessário(s)
        self.aumento_vendas = 0.0

    def definir_aumento_vendas(self, aumento):
        # Implemente o método definir_aumento_vendas com o(s) parâmetro(s) e atribuição(ões) necessária(s)
        self.aumento_vendas = aumento

    def exibir_aumento_formatado(self):
        aumento_formatado = "{:.2f}".format(self.aumento_vendas)
        return f"O aumento percentual de vendas foi de {aumento_formatado}%"
       