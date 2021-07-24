from tkinter import Tk
from tkinter import Label
import requests
import time
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
from playsound import playsound

def getweather():
     playsound('C:\VScode\JavaScript\Python\Sound\storm.mp3')
     page = requests.get(url)
     soup = BeautifulSoup(page.content, "html.parser") # * passed all html in soup variable

     # * getting info from site and assigning to variable

     location = soup.find('h1',class_="CurrentConditions--location--2_osB").text
     temperature = soup.find('span',class_="CurrentConditions--tempValue--1RYJJ").text
     time = soup.find('div',class_="CurrentConditions--timestamp--3_-CV").text
     weatherstate = soup.find('div',class_="CurrentConditions--phraseValue--17s79").text


     locationLabel.config(text=location)
     temperatureLabel.config(text=temperature)
     weatherPredictionLabel.config(text=weatherstate)
     timeLabel.config(text=time)

     # * The app should update aftr every 1 min and fetch data from website again
     temperatureLabel.after(60000,getweather)
     master.update() 

url = "https://weather.com/en-IN/weather/today/l/6a6f9bf8a5d6b2953fd3a5e17b0d4bc9d4eb2f4265f03368500f754be20d0958"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

# * Image 

img = Image.open("C:\VScode\JavaScript\images\Weather.png")

img = img.resize((250,250))
img = ImageTk.PhotoImage(img) # * Imp for placing the image on the screen

# * Creating the labels

locationLabel = Label(master, font=("Calibri bold italic",25),bg="white")
locationLabel.grid(row=0,sticky="N",padx=100)

timeLabel = Label(master,font=("Calibri italic",20),bg="white")
timeLabel.grid(row=1,sticky="N",pady=10)

temperatureLabel = Label(master, font=("Calibri bold",50),bg="white")
temperatureLabel.grid(row=1,sticky="W",padx=40)

Label(master,image=img,bg="white").grid(row=2,sticky="E") # * Image 

weatherPredictionLabel= Label(master,font=("Calibri bold",30),bg="white")
weatherPredictionLabel.grid(row=2,sticky="W",pady=100) 

getweather()

master.mainloop() # * Imp otherwise the app will close as soon as it opens