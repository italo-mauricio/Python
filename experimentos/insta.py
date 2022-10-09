from datetime import datetime
import instaloader
import pwinput


L = instaloader.Instaloader()
log = input('Digite o user do seu insta: ')
senha = pwinput.pwinput("Digite a senha do seu insta: ")


L.login(log, senha)


followers = instaloader.Profile.from_username(L.context, log).get_followers()
followees = instaloader.Profile.from_username(L.context, log).get_followees()


print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followees._data['count']))
print('\n')
print('Lista e informações de seguidores: ')
print('\n')

print(followers._data['edges'])