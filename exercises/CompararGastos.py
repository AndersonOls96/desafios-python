class ComparadorDeGastos:
    def __init__(self):
        # Adicione os atributos necessários
        # Dica: você pode usar listas para armazenar os gastos de João e Pedro
        self.gastos_joao = []
        self.gastos_pedro = []

    def adicionar_gastos_joao(self, gastos):
        # Implemente o método adicionar_gastos_joao
        # Dica: você pode usar o método append para adicionar um gasto à lista de gastos de João
        self.gastos_joao.append(gastos)      

    def adicionar_gastos_pedro(self, gastos):
        # Implemente o método adicionar_gastos_pedro
        # Dica: você pode usar o método append para adicionar um gasto à lista de gastos de Pedro
       self.gastos_pedro.append(gastos)

    def calcular_total_gastos(self, gastos):
        # Implemente o método calcular_total_gastos
        # Dica: você pode usar o método sum para somar os valores da lista de gastos
        return sum(gastos)

    def quem_gastou_mais(self):
        # Implemente o método quem_gastou_mais
        # Dica 1: você pode usar o método calcular_total_gastos para calcular os gastos de João e Pedro
        # Dica 2: você pode usar uma estrutura condicional para comparar os gastos de João e Pedro
        total_joao = self.calcular_total_gastos(self.gastos_joao)
        total_pedro = self.adicionar_gastos_pedro(self.gastos_pedro)

        if total_joao > total_pedro:
            return "João"
        elif total_pedro > total_joao:
            return "Pedro"
        else:
            return "Empate"

