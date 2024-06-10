class ComparadorDeGastos:
    def __init__(self):
        self.gastos_joao = []  # Lista para armazenar os gastos de João
        self.gastos_pedro = []  # Lista para armazenar os gastos de Pedro

    def adicionar_gastos_joao(self, gastos):
        self.gastos_joao.extend(gastos)

    def adicionar_gastos_pedro(self, gastos):
        self.gastos_pedro.extend(gastos)

    def calcular_total_gastos(self, gastos):
        return sum(gastos)

    def quem_gastou_mais(self):
        total_gastos_joao = self.calcular_total_gastos(self.gastos_joao)
        total_gastos_pedro = self.calcular_total_gastos(self.gastos_pedro)

        if total_gastos_joao > total_gastos_pedro:
            return "João gastou mais."
        elif total_gastos_joao < total_gastos_pedro:
            return "Pedro gastou mais."
        else:
            return "João e Pedro gastaram a mesma quantidade."
#Teste 
comparador = ComparadorDeGastos()

comparador.adicionar_gastos_joao([50, 30, 20])
comparador.adicionar_gastos_pedro([40, 45, 25])

print(comparador.quem_gastou_mais())  # Saída: "Pedro gastou mais."
