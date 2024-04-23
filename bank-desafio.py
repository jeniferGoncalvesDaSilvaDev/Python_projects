class User:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Account:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        self.limite = 500
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    def sacar(self, valor):
        # Implement sacar method

    def exibir_extrato(self):
        # Implement exibir_extrato method

class Bank:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.AGENCIA = "0001"
        self.numero_conta = 1

    def criar_usuario(self, cpf, nome, data_nascimento, endereco):
        user = User(cpf, nome, data_nascimento, endereco)
        self.users.append(user)
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self, cpf):
        user = self.get_user_by_cpf(cpf)
        if user:
            account = Account(self.AGENCIA, self.numero_conta, user)
            self.accounts.append(account)
            self.numero_conta += 1
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
    def get_user_by_cpf(self, cpf):
        for user in self.users:
            if user.cpf == cpf:
                return user
        return None

    # Implement other bank operations like deposit, withdraw, etc.

def main():
    bank = Bank()

    while True:
        # Menu options and operations
