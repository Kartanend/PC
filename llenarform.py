import pyautogui, time

contador=0
while contador<2:
    frase=input("Ingresa frase: ")
    correo=input("Ingresa direccion de correo falsa: ")
    pyautogui.click(x=375, y=530, clicks=1)
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.typewrite(frase)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(3)
    
    pyautogui.typewrite(correo)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(4)
    if contador<1:
        pyautogui.click(x=449, y=553, clicks=1)
        
    time.sleep(4)
    contador+=1


