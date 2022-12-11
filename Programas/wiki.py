import wikipedia
from wikipedia import search
import os

def search():
    os.system("cls")
    while True:
        
        search = input("Do your search: ")
        result = wikipedia.summary(search)
        print(result)
        
        conti = input('Do you want to do another search? [Y/N] ')
        if conti == 'Y':
            continue
        elif conti == 'N':
            print('Thanks')
            break
        else:
            print("Please enter a valid option!")
            
            
search()