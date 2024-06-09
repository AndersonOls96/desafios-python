class ComparadorDeGastos:
    def __init__(self):
        self.gastos_joao = []
        self.gastos_pedro = []

    def adicionar_gastos_joao(self, gastos):
        self.gastos_joao.append(gastos)

    def adicionar_gastos_pedro(self, gastos):
        self.gastos_pedro.append(gastos)

    def calcular_total_gastos(self, gastos):
        return sum(gastos) 

    def quem_gastou_mais(self):
        # Implemente o método quem_gastou_mais
        # Dica 1: você pode usar o método calcular_total_gastos para calcular os gastos de João e Pedro
        # Dica 2: você pode usar uma estrutura condicional para comparar os gastos de João e Pedro

        total_joao = self.calcular_total_gastos(self.gastos_joao)
        total_pedro = self.calcular_total_gastos(self.gastos_pedro)

        if total_joao > total_pedro:
            return "João"
        elif total_joao < total_pedro:
            return "Pedro"
        else:
            return "Empate"
