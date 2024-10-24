# Inicializa uma lista vazia para a lista de compras
lista_de_compras = []

# Função para adicionar produtos à lista
def adicionar_produto(produto, preco):
    lista_de_compras.append({"produto": produto, "preço": preco})

# Loop para inserir produtos
while True:
    produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
    if produto.lower() == 'sair':
        break
    preco = float(input(f"Digite o preço de {produto}: "))
    adicionar_produto(produto, preco)

# Exibir a lista de compras
print("\nSua lista de compras:")
for item in lista_de_compras:
    print(f"{item['produto']}: R${item['preço']:.2f}")

# calculo do total
def calcular_total(lista):
    return sum(item["preço"] for item in lista)

total = calcular_total(lista_de_compras)
print(f"\nO total da sua lista de compras é: R${total:.2f}")
