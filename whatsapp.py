import pyautogui
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com/")
time.sleep(30)
for i in range(20):
    pyautogui.press("h")
    pyautogui.press("i")
    pyautogui.press("enter")
    pyautogui.press("p")
    pyautogui.press("a")
    pyautogui.press("p")
    pyautogui.press("p")
    pyautogui.press("a")
    pyautogui.press("enter")

