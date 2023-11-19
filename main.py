#Import Modules
import pyautogui as pag
from time import sleep as t
import keyboard as kb #pip install keyboard

#Cool Text-Graphic
print("---:REBOOT SYSTEM:---")
print("---:.PLEASE WAIT.:---")
print("▒▒▒▒▒▒▒▒▒▒ 0%")
t(0.5)
print("█▒▒▒▒▒▒▒▒▒ 10%")
t(0.5)
print("██▒▒▒▒▒▒▒▒ 20%")
t(0.5)
print("███▒▒▒▒▒▒▒ 30%")
t(0.5)
print("████▒▒▒▒▒▒ 40%")
t(0.5)
print("█████▒▒▒▒▒ 50%")
t(0.5)
print("██████▒▒▒▒ 60%")
t(0.5)
print("███████▒▒▒ 70%")
t(0.5)
print("████████▒▒ 80%")
t(0.5)
print("█████████▒ 90%")
t(0.5)
print("██████████ 100%")
print("---:!SYSTEM READY!:---")
print("---:!!!STAND BY!!!:---")

#Variables
current = pag.position()
counter = 0
sec = 1
min = 0
min_counter = 59
t(0.5)
#Main Code
while not kb.is_pressed("p"):
    while 1:
        if pag.position() == current:
            t(0.5)
            counter += 1
            print(f"[AFK DETECTION : {counter}/30]")
            if counter >= 30:
                print("---:!ACTIVATE!:---")
                print(f"[!AFK : {min} m : {sec} s!]")
                sec += 1
                pag.keyDown("d") #right
                pag.keyUp("d")
                pag.keyDown("a") #left
                pag.keyUp("a")
                counter = 29
                if sec > min_counter:
                    sec = 0
                    min += 1
        else:
            counter = 0
            sec = 0
            current = pag.position()
            print("---:!!!RESET!!!:---")