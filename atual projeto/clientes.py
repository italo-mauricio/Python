import os
from validacoes import *
from time import sleep
import pickle






                
def listararquivo(): # Função para listar os itens dos arquivos
    try:
        listclient = open("clientelist.dat", "rb")
        registro1 = pickle.load(listclient)
        listclient.close()
    except:
        listclient = open("clientelist.dat", "wb")
        listclient.close()

    return registro1




def gravaarquivo(registro1): # Função para gravar
    listclient = open("clientelist.dat", "wb")
    pickle.dump(registro1, listclient)
    listclient.close()



registro1 = listararquivo()


#função de cadastro do cliente.
def cadastrocliente(): # Função de cadastro de cliente!
    os.system('cls')
    print("=="*30)
    print('''   Bem vindo ao nosso Sistema Integrado!
    Aqui você será muito bem atendido
    Vamos cadastrar você em instantes!
    Carregando...
    ''')
    print("=="*30)
    sleep(1)
    while True:
        nome = input("Por favor, digite o nome do cliente: ") # Usuário vai digitar o nome dele
        if (validstring(nome)): # Vai veirificar se é uma sting ou não
            break
        else:
            print('Nome inválido')
    while True:
        data = input('Digite o dia do seu nascimento ex("05/05/2005"): ') # Usuário vai digitar sua data de nascimento
        #Optamos por sugerir o formato para o usuário mesmo colocar a /
        if data_valida(data): # Vai verificar se a data é válida
            break
        else:
            print('Data inválida!')
    while True:
        email = input("Digite o email do cliente: ") # O usuário vai digitar o email dele
        if (validemail(email)): # chama a função que valida o email
            break
        else:
            print("Email inválido!")
            
    endereco = input("Digite o endereço do cliente: ") # Aqui o cliente irá digitar o seu endereço
    complemento = input("Digite o complemento(Opcional): ") # Aqui o cliente vai digitar um possível complemento
    
    while True:
        cpf = input("Por favor, digite um CPF válido: ") #aqui o cliente vai digitar o seu cpf
        if (cadastrocpf(cpf)):
            if cpf not in registro1: #caso ele não esteja no dicionário, ele irá colocar
                registro1[cpf] = [nome, data, email,endereco,complemento] #dicionário recebe as informações
                print(registro1[cpf]) # irá mostrar o dicionário
                print('Parabéns, você foi cadastrado com sucesso!')
                gravaarquivo(registro1) # Vai salvar os dados no arquivo
                break
            elif(cpf == registro1):#caso o cpf digitado for igual a algum já cadastrado, retorna o erro.
                print('CPF Já registrado, tente novamente!')
        else:
            print('CPF inválido!') 

    sleep(3) # decidimos usar sleep para facilitar a visualização final
    telaprincipalcliente()
        
        


#Essa função é responsável por atualizar os dados do cliente a partir da chave
def atualizarcliente():
    os.system('cls')
#optamos por alterar cada item de forma separada a partir de uma posição no dicionário pré determinada no cadastro 
    print("=="*30)
    print('''   Olá, você está na sessão de atualização de cadastro.
    Vamos atualizar seu cadastro em instantes!
    Carregando...   
          ''')
    print("=="*30)
    sleep(1)
   
    while True:
        cpf = input("Por favor, insira um CPF já cadastrado: ")#cliente vai digitar qual cpf ele cadastrou
        if cpf in registro1.keys(): #se ele estiver no dicionário ele entra
            print(registro1[cpf][0]) #exibe o dicionário
            print('Perfeito, localizamos o cliente no nosso sistema!')
            sleep(1)
            cadastro_novo = ' '
            cadastro_novo = input('Digite qual informação você deseja atualizar: ').upper() #cliente digita qual informação ele quer alterar
            #============================================================================================================
            if cadastro_novo == 'nome'.upper(): #caso ele queira o nome, irá entrar na parte de alteração do nome
                while True:
                    nome_novo = input("Digite um novo nome: ") # Usuário vai digitar o nome dele
                    if (validstring(nome_novo)): # Vai veirificar se é uma sting ou não
                        break
                    else:
                        print('Nome inválido') #ele insere o novo nome
                registro1[cpf][0] = nome_novo # o novo nome vai ser inserido no dicionário
                print('Nome atualizado com sucesso!')
                print(f'O novo nome cadastrado é {nome_novo}')
                gravaarquivo(registro1)
                break
            #============================================================================================================
            elif cadastro_novo == 'data de nascimento'.upper(): #caso ele queira a data de nascimento, ele entra na parte de alteração da data de nascimento.
                while True:
                    data_novo = input('Digite o dia do seu nascimento ex("05/05/2005"): ') # Usuário vai digitar sua data de nascimento
        #Optamos por sugerir o formato para o usuário mesmo colocar a /
                    if data_valida(data_novo): # Vai verificar se a data é válida
                        break
                    else:
                        print('Data inválida!')
                registro1[cpf][1] = data_novo # armazena no dicionário posição data a nova data
                print('Sua data de nascimento foi atualizada!')
                print(f'Sua nova data de nascimento é {data_novo}')
                gravaarquivo(registro1) # Vai salvar a nova data de nascimento
                break
                
            #====================================================================================================
            elif cadastro_novo == 'email'.upper(): #caso ele queira mudar o email, ele entra na parte de alteração de email
                while True:
                    email_novo = input("Digite o novo email do cliente: ") # O usuário vai digitar o email dele
                    if (validemail(email_novo)): # chama a função que valida o email
                        break
                    else:
                        print("Email inválido!") # digita o novo email
                registro1[cpf][2] = email_novo # novo email é adicionado na posição email
                print('Seu email foi atualizado com sucesso!')
                print(f'Seu novo email é {email_novo}')
                gravaarquivo(registro1) # Vai salvar o novo email no arquivo
                break
            #======================================================================================================  
            elif cadastro_novo == 'endereço'.upper(): # caso ele queira alterar o seu endereço, entra na parte de alteração de endereço
                endereco_novo = input('Digite seu novo endereço: ') # digita o endereço novo
                registro1[cpf][3] = endereco_novo # adiciona a lista o novo endereço digitado
                print("Seu endereço foi atualizado!")
                print(f'Seu novo endereço é {endereco_novo}')
                gravaarquivo(registro1) # Vai salvar o novo endereço no arquivo
                break
            #=======================================================================================================   
            elif cadastro_novo == 'opcional endereço'.upper(): # caso ele queria adicionar algum endereço opcional
                opendereco_novo = input('Digite seu endereço opcional novo: ') # digita o novo endereço opcional
                registro1[cpf][4] = opendereco_novo # adiciona o endereço opcional ao dicionário
                print("Seu endereço opcional foi atualizado com sucesso!")
                print(f'Seu novo endereço opcional é {opendereco_novo}')
                gravaarquivo(registro1) # Vai salvar o endereço opcional no arquivo
                break
            #=======================================================================================================   
            else:
                print('Opção inválida, por favor tente novamente!') # caso digite uma opção não condizente com os ifs
                
      
                
                
        else:
            print('Usuário não cadastrado, tente novamente!') # caso o cpf não esteja cadastrado no sistema
    
    sleep(3)  # decidimos usar sleep para facilitar a visualização final      
    telaprincipalcliente()
    

        
        


#Essa função é responsável por visualizar os dados do Cliente.   
def visualizarcliente():

    print("=="*30)
    print('''Olá, você escolheu a opção de visualizar um usuário já cadastrado!
            Para isso precisamos de um CPF cálido de usuário!
            Carregando..
        ''')
    print("=="*30)
    sleep(1)
    cpf = input('Digite o CPF que foi cadastrado por gentileza!: ') # cliente digita qual cliente quer visualizar a partir de seu cpf
    while cpf != registro1: #enquanto o cpf for diferente de dicionário, ele entra
        if cpf not in registro1:
            print('Usuário não encontrado!')
            return False
        else:
            print('Usuário encontrado!')
            print(registro1[cpf])
            break
    
    sleep(3) # decidimos usar sleep para facilitar a visualização final
    telaprincipalcliente()   
       

    




#Essa função deleta qualquer cliente do banco de dados, a partir da chave do CPF
def deletarcliente():
    os.system('cls')
    print("=="*30)
    print(''' Olá, você deseja apagar um banco de dados!
              Em instantes vamos realizar esta operação!
              Carregando
        ''')
    print("=="*30)
    sleep(1)
    cliente = input('Por favor, digite o CPF do cliente que você deseja apagar: ') # cliente vai digitar o cpf que ele quer tirar do sistema
    if cliente in registro1: # se ele estiver no dicionário (sistema)
        del registro1[cliente] # deleta o cliente
        print('Perfeito, usuário encontrado e excluído com sucesso!')
    else:
        print("Infelizmente não encontramos este usuário em nosso sistema!")  # caso não exista o usuário no sistema
    
    sleep(3) # decidimos usar sleep para facilitar a visualização final
    telaprincipalcliente()
          





#Função de chamada da tela principal de menu clientes
def telaprincipalcliente(): # Aréa do cliente
    os.system('cls')
    usuário = ' '
    print('=='*28)
    print('''
        = SISTEMA DE GERENCIAMENTO DE CLIENTES =
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ===== Cadastrar Cliente [1] ============ 
        ===== Atualizar Dados   [2] ============
        ===== Visualizar Dados  [3] ============
        ===== Remover Dados     [4] ============
        ===== Sair do Sistema   [5] ============
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ========================================
    ''')
    print('=='*28)
    usuário = ' '
    usuário = input('Por favor, escolha uma das 5 opções: ')
    while usuário != '5':

        if usuário == '1': # se ele quiser se cadastrar no sistema digita 1
            cadastrocliente()
        elif usuário == '2': # se ele quiser atualizar alguma informação no sistema digita 2
            atualizarcliente()
        elif usuário == '3': # se ele quiser visualizar alguma informação no sistema digita 3
            visualizarcliente()
        elif usuário == '4': # se ele quiser deletar o seu perfil no sistema digita 4
            deletarcliente()
        elif usuário == '5':
            print('Obrigado, volte sempre!') # caso queira sair, digita 5
            break
        else:
            print('Opção inválida!') # caso digite qualquer outra opção, retorna inválida
            return False 

        










    