import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = open("C:\VScode\JavaScript\Python\File.pdf",'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

print("Playing Audio Book")

for num in range(num_pages):
    page = pdf_reader.getPage(num)
    data = page.extractText()
    play = pyttsx3.init()
    play.say(data)
    play.runAndWait()