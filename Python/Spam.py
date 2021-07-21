import pyautogui, time
time.sleep(5)
file = open("C:\VScode\JavaScript\Python\Text\geemovie.txt", 'r')  # * r is for read the file
for word in file:
     pyautogui.typewrite(word)
     pyautogui.press("enter")