import os

line = '=' * 50

contas = {}


# limpar tela
def limpar():
    os.system('cls')


# menu principal
def menu_principal():

    while True:

        limpar()

        print(line)
        print('✅ Lista de Tarefas ✅'.center(50))
        print(line)

        print(
            '1 - Criar conta 🚹',
            '\n2 - Faça login 🏠',
            '\n3 - Sair 🏃'
        )

        print(line)

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            criar_conta()

        elif opcao == '2':
            login()

        elif opcao == '3':

            print(line)
            print('Bye Bye 👋')
            print(line)

            input('Saindo...')
            break

        else:

            print(line)
            print('Opção inválida ❌')
            print(line)

            input()


# sistema de criação de conta
def criar_conta():

    limpar()

    print(line)
    print('⚒️ Crie sua conta 🛠️'.center(50))
    print(line)

    nome = input('Digite o seu nome: ').strip()

    # impede nome vazio
    if nome == '':

        print(line)
        print('O nome não pode ficar vazio ❌')
        print(line)

        input()
        return

    # impede conta duplicada
    if nome in contas:

        print(line)
        print('Essa conta já existe ❌')
        print(line)

        input()
        return

    senha = input('Crie uma senha: ').strip()

    # impede senha vazia
    if senha == '':

        print(line)
        print('A senha não pode ficar vazia ❌')
        print(line)

        input()
        return

    contas[nome] = {
        "senha": senha,
        "tarefas": []
    }

    print(line)
    print('Conta criada com sucesso ✅')
    print(line)

    input('Voltando...')


# sistema de login
def login():

    while True:

        limpar()

        print(line)
        print('🏠 Faça Login 🏠'.center(50))
        print(line)

        nome = input('Digite seu nome: ').strip()

        if nome in contas:

            print(line)
            print(f'Olá, {nome} !')
            print(line)

            senha = input('Digite a sua senha: ').strip()

            if contas[nome]["senha"] == senha:

                print(line)
                print('Login feito com sucesso ✅')
                print(line)

                input('Entrando...')

                menu_tarefas(nome)

            else:

                print(line)
                print('Senha incorreta ❌')
                print(line)

                input()

        else:

            print(line)
            print('Conta não encontrada ❌')
            print(line)

            input()


# menu de tarefas
def menu_tarefas(nome):

    while True:

        limpar()

        print(line)
        print('✅ Menu de Tarefas ☑️'.center(50))
        print(line)

        # mostra tarefas do usuário
        if len(contas[nome]["tarefas"]) == 0:

            print('Nenhuma tarefa criada.')

        else:

            for indice, tarefa in enumerate(contas[nome]["tarefas"], start=1):

                if tarefa["concluida"]:
                    status = '✅'

                else:
                    status = '❌'

                print(f'{indice} - {status} {tarefa["nome"]}')

        print(line)

        print(
            '1 - Criar tarefa 🛠️',
            '\n2 - Marcar tarefa como concluída ✅',
            '\n3 - Remover tarefa ❌',
            '\n4 - Editar tarefa ⚒️',
            '\n5 - Logout 🏃'
        )

        print(line)

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            criar_tarefa(nome)

        elif opcao == '2':
            marcar_tarefa(nome)

        elif opcao == '3':
            remover_tarefa(nome)

        elif opcao == '4':
            editar_tarefa(nome)

        elif opcao == '5':

            print(line)
            print('Logout realizado 👋')
            print(line)

            input()
            break

        else:

            print(line)
            print('Opção inválida ❌')
            print(line)

            input()


# criar tarefa
def criar_tarefa(nome):

    limpar()

    print(line)
    print('🛠️ Crie uma nova tarefa 🛠️'.center(50))
    print(line)

    tarefa = input('Digite sua nova tarefa: ').strip()

    # impede tarefa vazia
    if tarefa == '':

        print(line)
        print('A tarefa não pode ficar vazia ❌')
        print(line)

        input()
        return

    nova_tarefa = {
        "nome": tarefa,
        "concluida": False
    }

    contas[nome]["tarefas"].append(nova_tarefa)

    print(line)
    print(f'Tarefa "{tarefa}" criada com sucesso ✅')
    print(line)

    input('Voltando...')


# marcar tarefa
def marcar_tarefa(nome):

    limpar()

    print(line)
    print('✅ Marcar tarefa como concluída ✅'.center(50))
    print(line)

    # verifica se há tarefas
    if len(contas[nome]["tarefas"]) == 0:

        print('Nenhuma tarefa encontrada ❌')

        print(line)

        input()
        return

    for indice, tarefa in enumerate(contas[nome]["tarefas"], start=1):

        if tarefa["concluida"]:
            status = '✅'

        else:
            status = '❌'

        print(f'{indice} - {status} {tarefa["nome"]}')

    print(line)

    try:

        escolha = int(input('Qual tarefa deseja concluir?: '))

        # verifica se índice existe
        if escolha < 1 or escolha > len(contas[nome]["tarefas"]):

            print(line)
            print('Tarefa inválida ❌')
            print(line)

            input()
            return

        contas[nome]["tarefas"][escolha - 1]["concluida"] = True

        print(line)
        print('Tarefa concluída ✅')
        print(line)

        input()

    except ValueError:

        print(line)
        print('Digite apenas números ❌')
        print(line)

        input()


# remover tarefa
def remover_tarefa(nome):

    limpar()

    print(line)
    print('❌ Remover tarefa ❌'.center(50))
    print(line)

    if len(contas[nome]["tarefas"]) == 0:

        print('Nenhuma tarefa encontrada ❌')

        print(line)

        input()
        return

    for indice, tarefa in enumerate(contas[nome]["tarefas"], start=1):

        print(f'{indice} - {tarefa["nome"]}')

    print(line)

    try:

        escolha = int(input('Qual tarefa deseja remover?: '))

        if escolha < 1 or escolha > len(contas[nome]["tarefas"]):

            print(line)
            print('Tarefa inválida ❌')
            print(line)

            input()
            return

        removida = contas[nome]["tarefas"].pop(escolha - 1)

        print(line)
        print(f'Tarefa "{removida["nome"]}" removida ✅')
        print(line)

        input()

    except ValueError:

        print(line)
        print('Digite apenas números ❌')
        print(line)

        input()


# editar tarefa
def editar_tarefa(nome):

    limpar()

    print(line)
    print('⚒️ Editar tarefa ⚒️'.center(50))
    print(line)

    if len(contas[nome]["tarefas"]) == 0:

        print('Nenhuma tarefa encontrada ❌')

        print(line)

        input()
        return

    for indice, tarefa in enumerate(contas[nome]["tarefas"], start=1):

        print(f'{indice} - {tarefa["nome"]}')

    print(line)

    try:

        escolha = int(input('Qual tarefa deseja editar?: '))

        if escolha < 1 or escolha > len(contas[nome]["tarefas"]):

            print(line)
            print('Tarefa inválida ❌')
            print(line)

            input()
            return

        print(line)

        nova_tarefa = input('Digite o novo nome da tarefa: ').strip()

        if nova_tarefa == '':

            print(line)
            print('O nome não pode ficar vazio ❌')
            print(line)

            input()
            return

        contas[nome]["tarefas"][escolha - 1]["nome"] = nova_tarefa

        print(line)
        print('Tarefa editada com sucesso ✅')
        print(line)

        input()

    except ValueError:

        print(line)
        print('Digite apenas números ❌')
        print(line)

        input()


menu_principal()