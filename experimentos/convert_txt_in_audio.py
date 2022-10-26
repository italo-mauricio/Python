from gtts import gTTS
from playsound import playsound


audio = 'audioteste.mp3'
language = 'pt-br'
usuario = input("Digite o que você quer falar: ")
sp = gTTS(
    
    text = usuario,
    lang = language
    
)

sp.save(audio)
playsound(audio)