from controller import *


while True:
    menu_principal = int(input("""
    1 - CADASTRAR USUÁRIO
    2 - LOGIN
    3 - SAIR
    DIGITE UM NÚMERO: """))

    if menu_principal == 1:
        nome = input('Nome: ')
        email = input('E-mail: ')
        senha = input('Senha: ')
        cadastrar = ControllerCadastro.cadastrar(nome, email, senha)
        if cadastrar == 2:
            print('Tamanho de nome inválido!')
        elif cadastrar == 3:
            print('Tamanho de E-mail inválido!')
        elif cadastrar == 4:
            print('Senha deve conter mais de 6 caracteres!')
        elif cadastrar == 5:
            print('O e-mail já está em uso!')
        elif cadastrar == 6:
            print('Erro interno do sistema!')
        elif cadastrar == 1:
            print('Usuário cadastrado com sucesso!')    

    elif menu_principal == 2:
        email = input('E-mail: ')
        senha = input('Senha: ')
        login = ControllerLogin.login(email, senha)
        if not login:
            print('E-mail ou senha inválida!')
        else:
            print(login)

    else:
        break
