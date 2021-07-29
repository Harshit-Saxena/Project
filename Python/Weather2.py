from tkinter import * 
from tkinter.font import Font
from PIL import Image,ImageTk
from requests.api import request
from requests.models import RequestField
import weatherapi
import requests
import time


class MyWeather:
    def __init__(self,master):
        self.master = master

        # ---------------------------------------------------------------------------- #
        #                                     Icon                                     #
        # ---------------------------------------------------------------------------- #
        
        self.img = Image.open("C:\VScode\JavaScript\images\search.jpg")
        self.img = self.img.resize((30,30),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

        # ---------------------------------------------------------------------------- #
        #                                   Variable                                   #
        # ---------------------------------------------------------------------------- #

        self.city = StringVar()
        style_font = Font(
            family = "poppins",
            size = 30,
            weight = "bold",
            slant = "italic"
        )

        # ---------------------------------------------------------------------------- #
        #                                    Labels                                    #
        # ---------------------------------------------------------------------------- #

        title = Label(master,text="Weather Pal",font=style_font,bg="#3493eb",fg="lightblue").place(x=0,y=0,relwidth=1,height=60)

        lbl_city = Label(master,text="City Name",font=("poppins",18,"bold"),bg="#1c7fa3",fg="white",padx=10,pady=8,anchor="w").place(x=0,y=60,relwidth=1,height=45)

        input_city = Entry(master,textvariable=self.city,font=("poppins",16),bg="white",fg="black").place(x=135,y=68,width=270,height=30)

        btn = Button(master,cursor = "hand2",image=self.img,bd=0,command = self.get_weather).place(x=410,y=68,width=30,height=30)


        # ---------------------------------------------------------------------------- #
        #                                    Content                                   #
        # ---------------------------------------------------------------------------- #

        self.lbl_city = Label(master,font=("poppins",30),bg="white",fg="green",padx=10,pady=8)
        self.lbl_city.place(x=0,y=110,relwidth=1,height=50)

        self.lbl_country = Label(master,font=("poppins",20),bg="white",fg="gold",padx=10,pady=8)
        self.lbl_country.place(x=0,y=160,relwidth=1,height=50)
        
        self.icons = Label(master,font=("poppins"),bg="white",padx=10,pady=8)
        self.icons.place(x=0,y=220,relwidth=1,height=100)

        self.temp = Label(master,font=("poppins",20),bg="white",fg="brown",padx=10,pady=8)
        self.temp.place(x=0,y=330,relwidth=1,height=30)

        self.weather = Label(master,font=("poppins",18),bg="white",fg="#262626",padx=10,pady=8)
        self.weather.place(x=0,y=370,relwidth=1,height=30)

        self.wind = Label(master,font=("poppins",18),bg="white",fg="lightblue",padx=10,pady=8)
        self.wind.place(x=0,y=410,relwidth=1,height=30)

        self.humidity = Label(master,font=("poppins",15),bg="white",fg="#db1d89",padx=10,pady=8)
        self.humidity.place(x=0,y=450,relwidth=1,height=30)

        self.sunrise = Label(master,font=("poppins",22),bg="white",fg="orange",padx=10,pady=8)
        self.sunrise.place(x=0,y=490,relwidth=1,height=30)

        self.sunset = Label(master,font=("poppins",20),bg="white",fg="orangered",padx=10,pady=8)
        self.sunset.place(x=0,y=530,relwidth=1,height=30)

        self.error = Label(master,font=("poppins",25),bg="white",fg="red",padx=10,pady=8)
        self.error.place(x=0,y=570,relwidth=1,height=30)

        # ---------------------------------------------------------------------------- #
        #                                    Footer                                    #
        # ---------------------------------------------------------------------------- #
        lbl_footer = Label(master,text="Made By Pulkit",font=("poppins",20,"italic"),bg="#262626",fg="lightblue",pady=10).pack(side=BOTTOM,fill=X)


# ---------------------------------------------------------------------------- #
#                             Information function                             #
# ---------------------------------------------------------------------------- #

    def get_weather(self):
        api_key = weatherapi.api_key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city.get()}&appid={api_key}"

        if self.city.get() == "":
            self.lbl_city.config(text="")
            self.lbl_country.config(text="")
            self.icons.config(image="")
            self.temp.config(text="")
            self.weather.config(text="")
            self.wind.config(text="")
            self.humidity.config(text="")
            self.sunrise.config(text="")
            self.sunset.config(text="")
            self.error.config(text="Location Required")
        else:
# ---------------------------------------------------------------------------- #
#                     Information we get from the json file                    #
# ---------------------------------------------------------------------------- #
            result = requests.get(url)
            if result:
                json = result.json()
                city_name = json["name"]
                country_name = json["sys"]["country"]
                icons = json["weather"][0]["icon"]
                temp_c = json["main"]["temp"] - 273.15
                temp_f = (json["main"]["temp"] - 273.15) *9/5 + 32
                weather = json["weather"][0]["description"]
                wind = json["wind"]["speed"]
                humidity = json["main"]["humidity"]
                sunrise = time.strftime("%I:%M:%S",time.gmtime(json["sys"]["sunrise"] - 19800))
                sunset = time.strftime("%I:%M:%S",time.gmtime(json["sys"]["sunset"] - 19800))

# ---------------------------------------------------------------------------- #
#                Setting the information from json to the labels               #
# ---------------------------------------------------------------------------- #

                self.lbl_city.config(text=city_name)

                self.lbl_country.config(text=country_name)

              
                self.img2 = Image.open(f"C:\VScode\JavaScript\Python\images\{icons}.png")    # Always write {icons} aftr folder name...cz we want the icons
                self.img2 = self.img2.resize((120,120),Image.ANTIALIAS)
                self.img2 = ImageTk.PhotoImage(self.img2)

                self.icons.config(image=self.img2)

                deg = u"\N{DEGREE SIGN}"
                self.temp.config(text= "Temperature: "+(str(round(temp_c,2))+deg+"C | "+str(round(temp_f,2))+deg+" F"))

                self.weather.config(text= "Weather: "+weather)

                self.wind.config(text= "Wind Speed: "+str(wind))

                self.humidity.config(text= "Humidity: "+str(humidity) + "%")

                self.sunrise.config(text= "Sunrise: " + sunrise)

                self.sunset.config(text= "Sunset: "+ sunset)

                self.error.config(text= "")
            else:
                self.lbl_city.config(text="")
                self.lbl_country.config(text="")
                self.icons.config(image="")
                self.temp.config(text="")
                self.weather.config(text="")
                self.wind.config(text="")
                self.humidity.config(text="")
                self.sunrise.config(text="")
                self.sunset.config(text="")
                self.error.config(text="Invalid Entry")



# ---------------------------------------------------------------------------- #
#                          Setting of the main screen                          #
# ---------------------------------------------------------------------------- #

master = Tk()
obj=MyWeather(master)                               # !  IMP
master.geometry("450x700+500+250")
master.config(bg="white")
master.title("Weather Pal")
master.mainloop()