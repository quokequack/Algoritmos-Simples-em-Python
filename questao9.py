anuidade = input('''Você possui a anuidade de associação de produtor rural (AAPR) em dia?
                 [1] Sim 
                 [2] Não
                 ''')
if(anuidade == "1"):
    print("Você entrou na festa!")
elif(anuidade == "2"):
    desejaPagar = input('''Deseja pagar R$25,00 para entrar então?
                 [1] Sim 
                 [2] Não
                 ''')
    if(desejaPagar == "1"):
        print("Você entrou na festa!")
    else: 
        print("Não entrou na festa!")
