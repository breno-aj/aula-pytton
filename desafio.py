class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.extrato.append(f'Saque: R${valor:.2f}')
                print(f'Saque de R${valor:.2f} realizado com sucesso!')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser positivo.')

    def visualizar_extrato(self):
        print(f'\nExtrato de {self.titular}:')
        for operacao in self.extrato:
            print(operacao)
        print(f'Saldo atual: R${self.saldo:.2f}\n')

def main():
    conta = ContaBancaria('breno')

    while True:
        print('Escolha uma operação:')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Visualizar Extrato')
        print('4. Sair')
        escolha = input('Digite o número da operação: ')

        if escolha == '1':
            valor = float(input('Digite o valor a ser depositado: '))
            conta.depositar(valor)
        elif escolha == '2':
            valor = float(input('Digite o valor a ser sacado: '))
            conta.sacar(valor)
        elif escolha == '3':
            conta.visualizar_extrato()
        elif escolha == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()