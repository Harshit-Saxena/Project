from tkinter import *


def btn_clicked():
    print("Its working")


window = Tk()
window.title(f"Signup Page")
window.geometry("1000x640")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 640,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    709.0, 238.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#edecec",
    highlightthickness = 0)

entry0.place(
    x = 571.5, y = 214,
    width = 275.0,
    height = 47)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    711.0, 340.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#edecec",
    highlightthickness = 0)

entry1.place(
    x = 576.5, y = 316,
    width = 269.0,
    height = 47)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    714.0, 442.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#edecec",
    highlightthickness = 0)

entry2.place(
    x = 582.5, y = 418,
    width = 263.0,
    height = 47)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 624, y = 497,
    width = 196,
    height = 50)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    385.0, 320.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()