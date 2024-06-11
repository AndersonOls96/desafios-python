class Cliente:
    def __init__(self, nome, telefone, email):
        # Adicione os atributos necessários
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        # Implemente o método exibir_informacoes
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"
    

    