print("Bem vindo ao site da Vinheria Agnello")

nome = input("Diga seu nome completo: ")
idade = int(input("Diga sua idade: "))

if idade <= 17:
    print("O comprador deve ser maior de idade")
    exit()

endereco = input("Diga seu endereço residêncial: ")
entrega = input("Diga o endereço de entrega: ")

print("\nCATÁLOGO DE VINHOS")
print("1 - Vinho Tinto - R$ 50,00")
print("2 - Vinho Branco - R$ 45,00")
print("3 - Vinho Rosé - R$ 40,00")
print("4 - Espumante - R$ 60,00")
print("5 - Vinho do Porto - R$ 75,00")

quantidade_vinhos = []
valor_vinhos = [50, 45, 40, 60, 75]

for i in range(5):
    qtd = int(input(f"Digite a quantidade de vinhos do tipo {i+1}: "))
    quantidade_vinhos.append(qtd)

valor_total = sum([qtd * valor_vinhos[i] for i, qtd in enumerate(quantidade_vinhos)])

if valor_total < 100:
    print("O valor mínimo para compra é de R$ 100,00")
    exit()
    
if valor_total > 200:
    frete = 0
    print("Frete Grátis!")
else:
    frete = 10

print(f"\nVocê comprou:")
for i in range(5):
    if quantidade_vinhos[i] > 0:
        print(f"{quantidade_vinhos[i]} vinhos do tipo {i+1}")
print(f"\nValor total do pedido: R$ {valor_total + frete:.2f}")
print(f"Endereço de entrega: {entrega}")
print("\nObrigado pela compra!")
