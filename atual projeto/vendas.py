import os
from time import sleep
from validacoes import *
from clientes import telaprincipalcliente
import pickle



#FUNÇÃO PARA O MENU DE VENDAS!
#PARTE EXCLUSIVA DOS FUNCIONÁRIOS

def listarvendas(): # Função para listar os itens dos arquivos
    try:
        listvendas = open("vendaslist.dat", "rb")
        dicionarioproduto = pickle.load(listvendas)
        listvendas.close()
    except:
        listvendas = open("vendaslist.dat", "wb")
        listvendas.close()

    return dicionarioproduto




def gravavendas(dicionarioproduto): # Função para gravar os itens
    listvendas = open("vendaslist.dat", "wb")
    pickle.dump(dicionarioproduto, listvendas)
    listvendas.close()


dicionarioproduto = listarvendas()





#FUNÇÃO PARA CADASTRAR PRODUTOS!
def cadastroproduto(): # cadastra um produto no sistema
    os.system('cls')
    print(''' Bem vindo ao cadastramento de produto!
    Vamos cadastrar o produto desejado!
    ''')
    
    while True:
        produto = input('Digite o nome do produto: ')
        if validstring(produto):
            break
        else:
            print('Produto inválido!')
    while True:
        categoria = input('Digite a categoria do produto: ')
        if validstring(categoria):
            break
        else:
            print("Categoria inválida!")
             
    while True:
        preco = input('Digite o preço do produto em R$: ')
        if validnum(preco):
            break
        else:
            print("Preço inválido!")
             
    marca = input('Digite a marca do produto: ')
    dicionarioproduto[produto] = [categoria, preco, marca]
    print('Produto cadastrado com sucesso!')
    gravavendas(dicionarioproduto)
    

        
    sleep(3) # decidimos usar sleep para facilitar a visualização final
    sistemavendas()



#FUNÇÃO PARA VISUALIZAR OS PRODUTOS CADASTRADOS!
def visualizarproduto():
    os.system('cls')
    print(''' Bem vindo, vamos visualizar o produto cadastrado!
          ''')
    produto = input('Qual produto você deseja visualizar: ') # digita qual produto ele quer visualizar
    while produto != dicionarioproduto: # enquanto o produto não estiver no dicionario
        if produto not in dicionarioproduto:
            print('Produto não encontrado!')
            return False
        else:
            print("Produto encontrado")
            print(dicionarioproduto[produto])
            break
    
    sleep(3)  # decidimos usar sleep para facilitar a visualização final      
    sistemavendas()

#FUNÇÃO PARA ATUALIZAR OS PRODUTOS CADASTRADOS!
def atualizarproduto():
    os.system('cls')
    print('''Bem vindo, vamos atualizar algum produto já cadastrado!
        ''')
    produto = input('Por favor, digite um produto já cadastrado: ')
    while True: # digita o produto que está cadastrado
        if produto in dicionarioproduto.keys(): # se o produto estiver no dicionário 
            print(dicionarioproduto[produto]) # exibe o produto na chave zero
            if produto in dicionarioproduto.keys(): # se o produto estiver dentro do dicionário ele localiza
                print('Localizamos o produto cadastrado!')
                produto_novo = ' '
                produto_novo = input('Qual informação você deseja alterar do produto: ').upper()# escolhe qual informação ele quer atualizar
                if produto_novo == 'categoria'.upper(): # se for a categoria, ele acessar a parte de categorias
                    categoria_nova = input('Digite a nova categoria: ') # digita a nova categoria
                    dicionarioproduto[produto][0] = categoria_nova # adiciona a nova categoria
                    print('Categoria atualizada com sucesso!')
                    print(f'Sua nova categoria é {categoria_nova}') # exibe a nova categoria
                    break
                elif produto_novo == 'preço'.upper(): # se ele quiser mudar o preço, digita preço
                    preco_novo = input('Digite um preço novo: ') # digita o novo preço
                    dicionarioproduto[produto][1] = preco_novo # guarda o novo preço
                    print('Preço ajustado com sucesso!')
                    print(f'Seu novo preço é de {preco_novo}') # exibe o novo preço
                    break
                elif produto_novo == 'marca'.upper(): # caso ele queira alterar a marca do produto
                    marca_nova = input('Digite a nova marca do seu produto: ') # digita a nova marca para o produto
                    dicionarioproduto[produto][2] = marca_nova # insere a nova marca do produto
                    print('Marca alterada com sucesso!')
                    print(f'Sua nova marca é {marca_nova}') # exibe a nova marca
                    break
                elif produto_novo == 'durabilidade'.upper(): # caso queira modificar a durabilidade do produto
                    durabi_nova = input('Digite a nova durabilidade do seu produto: ') # insere a nova durabilidade
                    dicionarioproduto[produto][3] = durabi_nova # insere no dicionário a nova durabilidade
                    print('Durabilidade alterada com sucesso!')
                    print(f"Sua durabilidade foi alterada para {durabi_nova}") # exibe a nova durabilidade
                    break
                else:
                    print('Opção não consta no nosso sistema!') # caso ele digite uma opção diferente
                    return False
            print('Obrigado!')
    
    sleep(3)  # decidimos usar sleep para facilitar a visualização final 
    sistemavendas()


#FUNÇÃO PARA DELETAR PRODUTOS CADASTRADOS!
def deletarproduto():
    os.system('cls')
    print('Bem vendo, vamos deletar um produto do seu sistema!')
    deletar = input('Digite o nome do produto que você quer deletar do sistema: ') # digita o produto que ele quer deletar do sistema
    if deletar in dicionarioproduto: # se o produto estiver no sistema ele deleta
        del dicionarioproduto[deletar] # deleta especificamente o produto digitado
        print('Produto deletado com sucesso!')
        print(f'Você deletou o seguinte produto: {deletar}') # exibe o produto no qual foi deletado
        
    else:
        print("Produto não encontrado em nosso sistema!") # caso ele não encontre o produto no sistema
    
    sleep(3) # decidimos usar sleep para facilitar a visualização final
    sistemavendas()



def sistemavendas():
    os.system('cls')
    sistema = ' '
    while sistema != 0:

        print('=='*28)
        print('''
            = SISTEMA DE GERENCIAMENTO DE CLIENTES =
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ===== Cadastrar Produto  [1] ============ 
            ===== Atualizar Produto  [2] ============
            ===== Visualizar Produto [3] ============
            ===== Remover Produto    [4] ============
            ===== Sair do Sistema    [5] ============
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            =========================================
        ''')
        print('=='*28)
        sistema = input('Escolha uma opção: ')
        if sistema == '1': # acessa a parte de cadastrar os produtos caso digite 1
            cadastroproduto()

        elif sistema == '2': # acessa a parte de visualizar o produto cadastrado caso digite 2
            atualizarproduto()

        elif sistema == '3': # acessa a parte de atualizar o produto cadastrado caso digite 3
            visualizarproduto()

        elif sistema == '4': # acessa a parte de atualizar o produto cadastrado caso digite 4
            deletarproduto()
        
        elif sistema == '5': # caso queira sair do sistema
            print('Obrigado, volte sempre!')
            break
        else:
            print('Opção inválida') # retorna inválido caso digite uma opção inválida



