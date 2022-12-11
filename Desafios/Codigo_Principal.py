import re
from time import sleep
from validacoes import *
import os



dicionario = {
               
            '183.305.880-17': ['Erick Bezerra Ribeiro Trindade', '04/06/2003', 'erickbrtrindade@gmail.com', 'Rua Olegário Vale 1290 Centro', ''],
            '316.267.110-89': ['Manuelly Rodrigues Victor', '24/06/2000', 'manuellyrodrigues@gmail.com', 'Rua Capitão antonio Martins 88', 'apartamento'],
            '059.509.594-18': ['Italo Mauricio ', '30/30/1998', 'italomauricio@gmail.com', 'Rua dos Potros 1340', 'casa']

            }
#função de cadastro do cliente.
def cadastrocliente():
    os.system("cls")
    print('''
    
            Bem vindo ao nosso Sistema Integrado!
            Aqui você será muito bem atendido
            Vamos cadastrar você em instantes!
            Carregando...

    ''')
    sleep(1)
    os.system("cls")
    while True:
        nome = input("Por favor, digite o seu nome: ")
        if validstring(nome):
            break
        else:
            print("Nome inválido!")
    while True:
        nascimento = input("Digite o dia do seu nascimento (d/m/y): ")   
        if data_valida(nascimento):
            break
        else:
            print("Data inválida")
    while True:
        email = input("Digite o seu email: ")
        if validemail(email):
            break
        else:
            print("Email inválido")
    endereco = input("Digite o seu endereço: ")
    complemento = input("Digite o seu complemento(Opcional): ")
    cpf=' '

    while cpf != cadastrocpf(cpf):
        cpf = input("Por favor, digite um CPF válido: ")
        if cadastrocpf(cpf):
            dicionario[cpf] = [nome,nascimento,email,endereco,complemento]
            print(dicionario[cpf])
            break
            
        else:
            print('CPF inválido!')
            print('')

    print('Parabéns, cadastro Realizado com Sucesso!!!')
    print('Aqui você terá tudo de melhor que podemmos oferecer!')
    input("Pressione qualquer tecla para sair... ")
    os.system("cls")




#Essa função é responsável por atualizar os dados do cliente a partir da chave
def atualizarcliente():
#optamos por alterar cada item de forma separada a partir de uma posição no dicionário pré determinada no cadastro 
    print('''Olá, você está na sessão de atualização de cadastro.
             Vamos atualizar seu cadastro em instantes!
             Carregando...   
          ''')
    sleep(1)
    cpf = input("Por favor, insira um CPF já cadastrado: ")
    if cpf in dicionario.keys():
        print(dicionario[cpf][0])
        if cpf in dicionario.keys():
            print('Perfeito, localizamos o cliente no nosso sistema!')
            sleep(1)
            cadastro_novo = ' '
            cadastro_novo = input('Digite qual informação você deseja atualizar: ')
            if cadastro_novo == 'Nome'.lower():
                nome_novo = input('Digite um novo nome: ')
                dicionario[cpf][0] = nome_novo 
                print('Nome atualizado com sucesso!')
                return True   
            if cadastro_novo == 'Data de Nascimento'.lower():
                data_novo = input('Digite uma nova data de nascimento: ')
                dicionario[cpf][1] = data_novo
                print('Sua data de nascimento foi atualizada!')
                return True
            if cadastro_novo == 'Email'.lower():
                email_novo = input('Digite um novo email: ')
                dicionario[cpf][2] = email_novo
                print('Seu email foi atualizado com sucesso!')
                return True
            if cadastro_novo == 'Endereço'.lower():
                endereco_novo = input('Digite seu novo endereço: ')
                dicionario[cpf][3] = endereco_novo
                print("Seu endereço foi atualizado!")
                return True
            if cadastro_novo == 'Opcional Endereço'.lower():
                opendereco_novo = input('Digite seu endereço opcional novo: ')
                dicionario[cpf][4] = opendereco_novo
                print("Seu endereço opcional foi atualizado com sucesso!")
                return True
            else:
                print('Opção inválida, por favor tente novamente!')
                return False
        print('Obrigado pela preferência de sempre!')
            
            
    else:
        print('Usuário não cadastrado, tente novamente!')
        return False
        
        


 #Essa função é responsável por visualizar os dados do Cliente.   
def visualizarcliente():
    os.system("cls")
    print('''Olá, você escolheu a opção de visualizar um usuário já cadastrado!
            Para isso precisamos do CPF do usuário!
            Carregando..
        ''')
    sleep(1)
    cpf = input('Digite o CPF cadastrador por gentileza!: ')
    if cpf in dicionario:
        print('Perfeito, encontramos este usuário(a) em nosso sistema!')
        print(dicionario[cpf])
        return True

    else:
        print('Infelizmente o CPF não foi encontrado, tente novamente!')
        return False



#Essa função deleta qualquer cliente do banco de dados, a partir da chave do CPF
def deletarcliente():
    os.system("cls")
    print('''
              Olá, você deseja apagar um banco de dados!
              Em instantes vamos realizar esta operação!
              Carregando
        ''')
    sleep(1)
    cliente = input('Por favor, digite o CPF do cliente que você deseja apagar: ')
    if cliente in dicionario:
        del dicionario[cliente]
        print('Perfeito, usuário encontrado e excluído com sucesso!')
        return True
    else:
        print("Infelizmente não encontramos este usuário em nosso sistema!")
        return False
    


#Função de chamada da tela principal de Menu.
def telaprincipal():
    print('=='*28)
    print('''
    |-----------------------------------------------|
    |   = SISTEMA DE GERENCIAMENTO DE CLIENTES =    |
    |                                               |
    |          Cadastrar Cliente [1]                |    
    |          Atualizar Dados   [2]                |
    |          Visualizar Dados  [3]                |
    |          Remover Dados     [4]                |
    |          Sair do Sistema   [0]                |
    |                                               |
    |-----------------------------------------------|
    ''')
    print('=='*28)

    usuário = input('Por favor, escolha uma das 5 opções: ')
    return usuário



#Essa função é a do Menu em si.
def menuprincipal():

    usuário = telaprincipal()

    while True:

        if usuário == '1':
            cadastrocliente()
        elif usuário == '2':
            atualizarcliente()
        elif usuário == '3':
            visualizarcliente()
        elif usuário == '4':
            deletarcliente()
        elif usuário == '0':
            break
        else:
            os.system("cls")
            print('Opção inválida!')

        usuário = telaprincipal()


## principal
menuprincipal()


    