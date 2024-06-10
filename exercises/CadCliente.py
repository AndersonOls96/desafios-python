class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"

# Exemplo de uso:
cliente1 = Cliente("Ketlen", "123456789", "Ketlen@example.com")
print(cliente1.exibir_informacoes())

# Criando outro cliente
cliente2 = Cliente("Andersson", "987654321", "Andersson@example.com")

# Exibindo as informações do segundo cliente
print(cliente2.exibir_informacoes())
    
