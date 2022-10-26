from gtts import gTTS
from playsound import playsound

while True:
    audio = 'audioteste.mp3'
    language = 'pt-br'
    usuario = input("Digite o que você quer falar: ")

    sp = gTTS(
        
        text = usuario,
        lang = language
    )

    sp.save(audio)
    playsound(audio)
 
    conti = input("Deseja falar novamente? [Y/N] ")
    if conti == 'Y':
        continue
    elif conti == 'N':
        print("Obrigado!")
        break
 