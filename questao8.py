possuiBolsaFamilia = input('''Você possui bolsa família?
                 [1] Sim 
                 [2] Não
                 ''')

possuiMaisTresFilhos = input('''Você possui mais de três filhos?
                 [1] Sim 
                 [2] Não
                 ''')

if(possuiBolsaFamilia == "1" and possuiMaisTresFilhos == "1"):
    print("Você pode acessar a vaga de cotista!")
else:
    print("Você não pode ser cotista!")