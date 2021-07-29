from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title(f"Weather App 1")
window.geometry("355x638")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 638,
    width = 355,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    177.5, 258.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 49, y = 542,
    width = 265,
    height = 47)

window.resizable(False, False)
window.mainloop()
