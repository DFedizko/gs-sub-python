# FUNÇÃO PARA EXIBIR UM INPUT MOSTRANDO UM MENU DE OPÇÕES PARA O USUÁRIO

total_produtos = []
produtos_escolhidos = []

def menu():
    lista_produtos = ['Pneu', 'Multi Mídia', 'Freio', 'Óleo', 'Retrovisor', 'Alto Falante']
    
    escolha = input('''\nQual dos itens você deseja escolher:
                    
1. Pneu
2. Multi Mídia
3. Freio
4. Óleo
5. Retrovisor
6. Alto Falante
7. Sair do Programa
                    
-> ''')
    
    if escolha == '1':

        print(f'\nVocê escolheu o {lista_produtos[0]}, Que custa R$800.')
        servico = input('Deseja obter o serviço para instalação? 1.Sim 2.Não\n')
        
        if servico == '1':
            print('\nÓtimo, o preço para a instalação é R$100.')
            total = 100 + 800
            print(f'O total ficaria então ficaria R${total}.\n')
            produtos_escolhidos.append(lista_produtos[0])
            total_produtos.append(total)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 

        elif servico == '2':
            print('\nTudo bem, sem serviços.')
            print('O total ficaria então ficaria R$800\n') # MUDAR AQUI
            produtos_escolhidos.append(lista_produtos[0])
            total_produtos.append(800)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 
                
        else:
            ('\nVocê precisa digitar 1 ou 2.')


    elif escolha == '2':
        print(f'\nVocê escolheu o {lista_produtos[1]}, Que custa R$700.')
        servico = input('Deseja obter o serviço para instalação? 1.Sim 2.Não\n')
        
        if servico == '1':
            print('\nÓtimo, o preço para a instalação é R$100.')
            total = 100 + 700
            print(f'O total ficaria então ficaria R${total}.\n')
            produtos_escolhidos.append(lista_produtos[1])
            total_produtos.append(total)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()
            else:
                print('Você precisa digitar um número, 1 ou 2.') 

        elif servico == '2':
            print('\nTudo bem, sem serviços.')
            print('O total ficaria então ficaria R$700\n') # MUDAR AQUI
            produtos_escolhidos.append(lista_produtos[1])
            total_produtos.append(700)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 
            
        else:
            ('\nVocê precisa digitar 1 ou 2.')


    elif escolha == '3':
        print(f'\nVocê escolheu o {lista_produtos[2]}, Que custa R$400.')
        servico = input('Deseja obter o serviço para instalação? 1.Sim 2.Não\n')
        
        if servico == '1':
            print('\nÓtimo, o preço para a instalação é R$100.')
            total = 100 + 400
            print(f'O total ficaria então ficaria R${total}.\n')
            produtos_escolhidos.append(lista_produtos[2])
            total_produtos.append(total)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()
            else:
                print('Você precisa digitar um número, 1 ou 2.') 

        elif servico == '2':
            print('\nTudo bem, sem serviços.')
            print('O total ficaria então ficaria R$400\n') # MUDAR AQUI
            produtos_escolhidos.append(lista_produtos[2])
            total_produtos.append(400)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 
            
        else:
            ('\nVocê precisa digitar 1 ou 2.')


    elif escolha == '4':
        print(f'\nVocê escolheu o {lista_produtos[3]}, Que custa R$50.')
        servico = input('Deseja obter o serviço para instalação? 1.Sim 2.Não\n')
        
        if servico == '1':
            print('\nÓtimo, o preço para a instalação é R$50.')
            total = 50 + 50
            print(f'O total ficaria então ficaria R${total}.\n')
            produtos_escolhidos.append(lista_produtos[3])
            total_produtos.append(total)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()
            else:
                print('Você precisa digitar um número, 1 ou 2.') 

        elif servico == '2':
            print('\nTudo bem, sem serviços.')
            print('O total ficaria então ficaria R$50\n') # MUDAR AQUI
            produtos_escolhidos.append(lista_produtos[3])
            total_produtos.append(50)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 
            
        else:
            ('\nVocê precisa digitar 1 ou 2.')


    elif escolha == '5':
        print(f'\nVocê escolheu o {lista_produtos[4]}, Que custa R$ 500.')
        servico = input('Deseja obter o serviço para instalação? 1.Sim 2.Não\n')
        
        if servico == '1':
            print('\nÓtimo, o preço para a instalação é R$100.')
            total = 100 + 500
            print(f'O total ficaria então ficaria R${total}.\n')
            produtos_escolhidos.append(lista_produtos[4])
            total_produtos.append(total)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()
            else:
                print('Você precisa digitar um número, 1 ou 2.') 

        elif servico == '2':
            print('\nTudo bem, sem serviços.')
            print('O total ficaria então ficaria R$500\n') # MUDAR AQUI
            produtos_escolhidos.append(lista_produtos[4])
            total_produtos.append(500)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 
            
        else:
            ('\nVocê precisa digitar 1 ou 2.')


    elif escolha == '6':
        print(f'\nVocê escolheu o {lista_produtos[5]}, Que custa R$ 300.')
        servico = input('Deseja obter o serviço para instalação? 1.Sim 2.Não\n')
        
        if servico == '1':
            print('\nÓtimo, o preço para a instalação é R$100.')
            total = 100 + 300
            print(f'O total ficaria então ficaria R${total}.\n')
            produtos_escolhidos.append(lista_produtos[5])
            total_produtos.append(total)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()
            else:
                print('Você precisa digitar um número, 1 ou 2.') 

        elif servico == '2':
            print('\nTudo bem, sem serviços.')
            print('O total ficaria então ficaria R$300\n') # MUDAR AQUI
            produtos_escolhidos.append(lista_produtos[5])
            total_produtos.append(300)
            mais_produto = input('Deseja escolher mais algum produto? 1.Sim 2.Não\n')
            
            if mais_produto == '1': 
                quantos = int(input('Quantos produtos a mais deseja comprar?\n'))
                for i in range(quantos):
                    menu()

            elif mais_produto == '2':
                print('Tudo bem, sem mais produtos.\n')
                
            else:
                print('\nVocê precisa digitar um número, 1 ou 2.') 
            
        else:
            ('\nVocê precisa digitar 1 ou 2.')

    elif escolha == '7':
        print('\nPrograma finalizado.\n')


    else:
        print('\nPor favor digite um número entre 1 a 7.\n')

# FUNÇÃO PARA DEFINIR UM INPUT DE QUANTIDADE DE CLIENTES, SE 5, 5 MENUS SERÃO EXIBIDOS SENDO UM DE CADA VEZ, ATENDENDO CADA CLIENTE POR VEZ

def quantidade_clientes():
    clientes = int(input('''Vocês estão em quantos clientes?
                        
-> '''))
        
    contador = 1
    for i in range(clientes):
        if contador >= 2:
            print('\n ** Próximo Cliente **')
        menu()
        for i in range(clientes):
            resultado = sum(total_produtos)
            numUsuario = contador + i
            print('''\nTotal usuário {}: 
                    
O preço total dos produtos e serviços foi de R${}.'''.format(numUsuario, resultado))
            print(f'\nOs produtos escolhidos pelos usuários foram: \n')
            for produto in (produtos_escolhidos):
                print(produto)
    print()

#Iinializa todo o programa

quantidade_clientes()