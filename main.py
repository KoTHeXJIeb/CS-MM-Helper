
# Importing neccassary modules
import time # For delays
from colorama import init, Fore, Back, Style # For colorized text
init() # Colorama`s function for Windows user`s to colorize text 


# Some useless variables :D


# Some useless functions

# I`ll do some localization soon (I`m from Ukraine, so if there will be mistakes, don`t argue me :3)

def start(): # It might be start function, but...
    print('Начальные деньги 800$. Вы выиграли первый раунд? (Да/Нет)') 
    round1 = str(input()) # For future calculatin`
    if round1 == 'Да':
        print('Сколько у Вас осталось денег?')
        buy1 = int(input()) # How much money do you have after first round
        if buy1 <= 100:
            print(Fore.GREEN + 'Идёт подсчёт...')
            time.sleep(3) # Delay (idk why)
        if buy1 > 150:
            print(Fore.GREEN + 'Вы умерли в пистолетном раунде?') 
            if buy1 > 300:
                time.sleep(3) # Again useless delay :D
                print(Fore.GREEN + 'Отлично, на съекономленые деньги можно купить отличный закуп!')      
    if round1 == 'Нет':
        print('Плохо :( ') # Bad, if you lost the round ;( (crying)


# Footer of the whole script (usually, I`m using it as initializin` all the functions)

start()

