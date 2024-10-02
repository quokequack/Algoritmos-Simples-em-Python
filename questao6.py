produtos = {'Milho': 35, "Arroz": 53, 'Feijão': 100}

produto = input('''Digite o número do produto que deseja comprar:
                [1] Milho - R$ 35,00 (kg)
                [2] Arroz - R$ 53,00 (kg)
                [3] Feijão - R$ 100,00 (kg)
                ''')


quantidade = int(input("Digite a quantidade (kg): "))

subtotal = 0

if(produto == "1"):
    subtotal = produtos['Milho'] * quantidade
elif(produto == "2"):
    subtotal = produtos['Arroz'] * quantidade
elif(produto == "3"):
    subtotal = produtos["Feijão"] * quantidade
    
print(f"O subtotal é: R${subtotal},00")


pagamento = input('''Digite o número que representa a opção de pagamento: 
                  [1] À vista
                  [2] Cartão
                  ''')

if pagamento == "1":
    print("Pagamento à vista realizado com sucesso!")
else:
    print("Opção de pagamento inválida no momento! Por favor, escolha a opção 1 para pagar à vista.")