import pyautogui, time
time.sleep(5)
file = open("C:\VScode\JavaScript\Python\Text\geemovie.txt", 'r')
for word in file:
     pyautogui.typewrite(word)
     pyautogui.press("enter")
