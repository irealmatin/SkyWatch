import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def GetWeather():
    #Location
    try:
        city = text_field.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        lat = location.latitude
        lng = location.longitude
        obj = TimezoneFinder()
        res = obj.timezone_at(lng=lng , lat=lat)
        city_lbl.config(text=res.split("/")[1])
        print(res)

        #time
        home = pytz.timezone(res)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        time_lbl.config(text="Local Time :")

        api_key = "b7ef86b3524a1fb0cbe7093a298d9516"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        tmp_lbl.config(text=f"{temp} °")
        condition_lbl.config(text=f"{condition} | FEELS LIKE {temp} °")
        wind_lbl.config(text=wind)
        humidity_lbl.config(text=humidity)
        description_lbl.config(text=description)
        pressure_lbl.config(text=pressure)
    except Exception as error:
        print(error)
        messagebox.showerror("Sky Watch","invalid entry")



window = tk.Tk()


window.title("SKY  WATCH")
window.geometry("900x500+300+200")
window.resizable(False,False)

# Search box :
search_img = tk.PhotoImage(file="search.png")
search_img_lbl = tk.Label(window , image=search_img)
search_img_lbl.pack(pady=20,side=tk.TOP)

text_field = tk.Entry(window,justify="center" , width=17,
                      font=("poppins",25,"bold"),
                      bg= "#404040",fg="white",border=0)

text_field.place(x=280 , y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_btn = tk.Button(window , image=search_icon , border=0 ,
                            cursor="hand2" , bg="#404040" ,command=GetWeather)

search_icon_btn.place(x=590 , y=34)

# Logo 
logo_img = tk.PhotoImage(file="logo.png" )

logo_label = tk.Label(window , image=logo_img)
logo_label.pack(side=tk.TOP)

# box line
frame_img = tk.PhotoImage(file="box.png")
frame_label = tk.Label(window,image=frame_img)
frame_label.pack(pady=10 ,side=tk.BOTTOM)

# City name
city_lbl = tk.Label(window , font=("arial" ,40 , "bold" ), fg="#4b4bcc" )
city_lbl.place(x=25 , y=140)

# time
time_lbl = tk.Label(window , font=("arial",20, "bold") , fg="#4b4bcc") 
time_lbl.place(x=30 , y=230)

clock = tk.Label(window, font=("Helvetica" , 35, "bold") , fg="orange")
clock.place(x=95,y=270)

# labels for Box Line
lbl1 = tk.Label(window , text="WIND:" , font=("Helvetica",15,"bold"), fg="#404040" ,bg="#1ab5ef")
lbl1.place(x=120,y=403)

lbl2 = tk.Label(window , text="HUMIDITY:" , font=("Helvetica",15,"bold"), fg="#404040" ,bg="#1ab5ef")
lbl2.place(x=280,y=403)

lbl3 = tk.Label(window , text="DESCRIPTION:" , font=("Helvetica",15,"bold"), fg="#404040" ,bg="#1ab5ef")
lbl3.place(x=450,y=403)

lbl4 = tk.Label(window , text="PRESSURE:" , font=("Helvetica",15,"bold"), fg="#404040" ,bg="#1ab5ef")
lbl4.place(x=670,y=403)

tmp_lbl = tk.Label(window , font=("arial",70,"bold"),fg="orange")
tmp_lbl.place(x=600 , y=170)

condition_lbl = tk.Label(window , font=("arial" , 15 , "bold"), fg="#4b4bcc")
condition_lbl.place(x=590 , y=270)

wind_lbl = tk.Label(window , text="---" , font=("arial" , 20 ) , bg="#1ab5ef" , fg="#404040")
wind_lbl.place(x=120 , y=430)

humidity_lbl = tk.Label(window , text="---" , font=("arial" , 20 ) , bg="#1ab5ef" , fg="#404040")
humidity_lbl.place(x=305 , y=430)

description_lbl = tk.Label(window , text="---" , font=("arial" , 20 ) , bg="#1ab5ef" , fg="#404040")
description_lbl.place(x=450 , y=430)

pressure_lbl = tk.Label(window , text="---" , font=("arial" , 20 ) , bg="#1ab5ef" , fg="#404040")
pressure_lbl.place(x=700 , y=430)



window.mainloop()

