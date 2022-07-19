
from clientes import telaprincipalcliente
import os
from time import sleep
from validacoes import*
import pickle



def listarpromo(): # Função para listar os itens dos arquivos
    try:
        listpromo = open("promolist.dat", "rb")
        dicionariopromocao = pickle.load(listpromo)
        listpromo.close()
    except:
        listpromo = open("promolist.dat", "wb")
        listpromo.close()

    return dicionariopromocao




def gravapromo(dicionariopromocao): # Função para gravar
    listpromo = open("promolist.dat", "wb")
    pickle.dump(dicionariopromocao, listpromo)
    listpromo.close()

dicionariopromocao = listarpromo()
    

def cadastropromocao(): # Para o cadastramento das promoções!
    os.system("cls")
    print('=='*30)
    print(''' Bem vindo(a), aqui você poderá cadastrar
            suas promoções da maneira que desejar.''')
    print('=='*30)
    
    promocao = input('Digite a promoção que você quer inserir: ') # insere o nome da promoção
    while True:
        senha = input('Digite o código da promoção: ') # insere o código para acessar as promoções
        if validnum(senha):
            break
        else:
            print('Senha inválida!')
    while senha != dicionariopromocao: # compara se o código é diferente do dicionário
        
        if senha not in dicionariopromocao: # se ele não estiver no dicionário, ele entra e cadastra.
            dicionariopromocao[senha] = [promocao]
            print(dicionariopromocao)
            gravapromo(dicionariopromocao)

            print('Promoção cadastrada!')
            break

        else:
            print("Promoção não encontrada!")
    sleep(3)
    menupromocoes()


        
    

def atualizarpromocao(): # atualizar as promoções
    print('=='*30)
    print("""Seja bem vindo(a), aqui você pode
atualizar as promoções da maneira que você quiser""")
    print('=='*30)
    while True:
        senha = input("Por favor, insira uma senha da sua promoção já cadastrada: ") # informa o código de uma promoção já cadastrada
        if senha in dicionariopromocao: 
            print(dicionariopromocao[senha][0]) 
            print('Perfeito, a promoção em questão foi localizada')
            promocao_nova = input('Digite uma nova promoção: ') # aqui você insere a nova promoção
            if promocao_nova == 'promocao'.upper():
                dicionariopromocao[senha][1]= promocao_nova 
                print('Promoção atualizada com sucesso')
                print(f'A promoção nova é essa: {promocao_nova}')
                gravapromo(dicionariopromocao)
                break
        else:
            print('Senha inválida!')
            
        sleep(3)
        menupromocoes()
        
        
            

    
def visualizarpromocao(): # função para visualizar as promoções
    os.system('cls')
    print('=='*30)
    print("""Bem vindo(a), aqui você poderá visualizar
    todas as promoções ativas no sistema!""")
    senha = input('Digite sua senha de administrador para ter acesso: ') # pede a senha de acesso do administrador
    if senha == '12345678':
        while senha != 0:
            codigo = input("Digite o código da promoção que você quer visualizar: ") # pede o código vinculado a promoção
            if codigo not in dicionariopromocao:
                print('Promoção não encontrada!')
                continuar = input('Deseja continuar procurando[S/N]: ')
                if continuar == 'S':
                    return True
                if continuar == 'N':
                    print('Okay, aguarde...')
                    break

                if codigo == '0':
                    break
                
            else:
                print("Promoção encontrada!")
                print(f"Promoção consta no sistema, com o código de {codigo}")
                break
    else:
        print("Senha inválida!")
    sleep(3)
    menupromocoes()
                



def deletarpromocao(): # função para deletar uma promoção
    os.system('cls')
    print('=='*30)
    print("""Bem vindo(a), aqui você poderá excluir as promoções que
    já foram cadastradas no sistema a partir da senha cadastradas anterior-
    mente""")
    print('=='*30)
    
    senha = input("""Digite o código da promoção que você cadastrou: """)
    if senha in dicionariopromocao:
        del dicionariopromocao[senha]
        print('Promoção excluída com sucesso')
        gravapromo(dicionariopromocao)
    else:
        print('Não foi encontrada nenhuma promoção ativa')
    sleep(3)
    menupromocoes()



def menupromocoes():
    os.system('cls')
    print('''
        = SISTEMA DE GERENCIAMENTO DE CLIENTES =
        ========================================
        ===== Cadastrar Promoção  [1] ========== 
        ===== Atualizar Promoção  [2] ==========
        ===== Visualizar Promoção [3] ==========
        ===== Remover Promoção    [4] ==========
        ===== Retornar ao menu    [5] ==========
        ========================================
        ========================================
    ''')
    usuario = input("Escolha uma opção válida: ")
    while usuario != "5":

        if usuario == '1': # se ele cadastrar alguma promoção no sistema digita 1
            cadastropromocao()
        elif usuario == '2': # se ele quiser atualizar alguma promoção no sistema digita 2
            atualizarpromocao()
        elif usuario == '3': # se ele quiser visualizar promoção ativa no sistema digita 3
            visualizarpromocao()
        elif usuario == '4': # se ele quiser deletar a promocao no sistema digita 4
            deletarpromocao()
        elif usuario == '5':
            print('Obrigado, volte sempre!')
            print('Retornando ao nosso menu principal...')
            sleep(2)
            telaprincipalcliente()
            break
        else:
            print('Opção inválida!') # caso digite qualquer outra opção, retorna inválida
            return False 