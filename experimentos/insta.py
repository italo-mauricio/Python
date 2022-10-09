from datetime import datetime
import instaloader
import pwinput
from datetime import date


hora_atual = datetime.now()
hora = hora_atual.strftime('%H:%M')
data = date.today()


def instagram():
    while True:
        
        print(f'''
        | =========================================================== |
        | ---------------- Verificador de Instagram ----------------- |
        |                                                             |
        | Requisitos: pip3 install instaloader                        |
        |                                                             |
        | A biblioteca retorna informações dos seus seguidores como,  |
        | nome, id, bio, user etc. Lembrando, que é totalmente seguro |
        | pois ele só retorna informações publicas.                   |
        |                                                             |
        | ----------------------------------------------------------- |
        | =========================================================== |
        |                since 2022, by italo-mauricio                |
        | =========================================================== |
            
        ''')
        
        L = instaloader.Instaloader()
        log = input('Digite o user do seu insta: ')
        senha = pwinput.pwinput("Digite a senha do seu insta: ")


        L.login(log, senha)


        followers = instaloader.Profile.from_username(L.context, log).get_followers()
        followees = instaloader.Profile.from_username(L.context, log).get_followees()


        print(f'''
            
            Data da verificação: {data}
            Hora da verificação: {hora}
            
            Seguidores: ''' + str(followers._data['count']))
        print('Seguindo: ' + str(followees._data['count']))
        print('\n')
        print('Lista e informações de seguidores: ')
        print('\n')
        print(followers._data['edges'])
       
        conti = input("Deseja verificar novamente: [Y,N] ").strip().lower()
        
        if conti == 'Y'.lower():
            instagram()
            break
        if conti == 'N'.lower():
            print("Obrigado!")
            break
        else:
            print("Tente novamente!")
            
                
                
instagram()
                