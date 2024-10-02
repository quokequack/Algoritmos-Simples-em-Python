usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")
confirmacaoSenha = input("Confirme a senha: ")

if(senha == confirmacaoSenha):
    print("Cadastro efetuado com sucesso!");
else:
    print("Cadastro não realizado: senhas diferem!")