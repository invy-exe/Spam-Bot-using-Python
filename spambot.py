import pyautogui, time

time.sleep(10)

s = open(r"C:\Users\User\OneDrive\Desktop\japbible.txt", "r")

for word in s:
    pyautogui.typewrite(word)
    pyautogui.press("enter")