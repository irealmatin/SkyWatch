#Import required modules
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#==============================Function===============================================#
# Define function to get weather information based on user input 
# Fetch data
def GetWeather():
    #Location
    # Get user input for city name and use geopy to get latitude and longitude
    try:
        city = text_field.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        lat = location.latitude
        lng = location.longitude
        # Use timezonefinder to get the timezone at the user's location
        obj = TimezoneFinder()

     # retrieve timezone based on latitude and longitude using timezonefinder library
        res = obj.timezone_at(lng=lng , lat=lat)
        # update city label with city name
        continent_lbl.config(text=res.split("/")[0])
        
        print(res)

        #time
        # Get current time based on timezone and update clock label
        home = pytz.timezone(res)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        # update clock label with local time
        clock.config(text=current_time)
        # update time label
        time_lbl.config(text="Local Time :")

         # Use OpenWeatherMap API to get weather information for the given location
        api_key = "b7ef86b3524a1fb0cbe7093a298d9516"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        json_data = requests.get(api).json()

        # retrieve weather condition, temperature, pressure, humidity, and wind speed
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        # update labels with weather information
        tmp_lbl.config(text=f"{temp} °")
        condition_lbl.config(text=f"{condition} | FEELS LIKE {temp} °")
        wind_lbl.config(text=wind)
        humidity_lbl.config(text=humidity)
        description_lbl.config(text=description)
        pressure_lbl.config(text=pressure)

    except Exception as error:
        # display error message if location is not found or if there is an issue with retrieving weather information
        print(error)
        messagebox.showerror("Sky Watch","invalid entry")

#==========================================Design==========================================================#
# Create tkinter window
window = tk.Tk()

# Set window title, size, and prevent resizing
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

# continent name
continent_lbl = tk.Label(window , font=("Helvetica" ,35 , "bold" ), fg="#2F2F4F" )
continent_lbl.place(x=25 , y=175)

# city name
# city_lbl = tk.Lable(window , font=("Helvetica" , 35 , "bold") , fg="#2F2F4F")
# city_lbl.place(x= , y=)

# time
time_lbl = tk.Label(window , font=("arial",15, "bold") , fg="#2F2F4F") 
time_lbl.place(x=30 , y=240)

clock = tk.Label(window, font=("Helvetica" , 40, "bold") , fg="orange")
clock.place(x=30,y=270)

# labels for Box Line
lbl1 = tk.Label(window , text="WIND:" , font=("Helvetica",15,"bold"), fg="#F8F8F8" ,bg="#1ab5ef")
lbl1.place(x=120,y=403)

lbl2 = tk.Label(window , text="HUMIDITY:" , font=("Helvetica",15,"bold"), fg="#F8F8F8" ,bg="#1ab5ef")
lbl2.place(x=280,y=403)

lbl3 = tk.Label(window , text="DESCRIPTION:" , font=("Helvetica",15,"bold"), fg="#F8F8F8" ,bg="#1ab5ef")
lbl3.place(x=450,y=403)

lbl4 = tk.Label(window , text="PRESSURE:" , font=("Helvetica",15,"bold"), fg="#F8F8F8" ,bg="#1ab5ef")
lbl4.place(x=670,y=403)

# tempreture Lable
tmp_lbl = tk.Label(window , font=("arial",70,"bold"),fg="orange")
tmp_lbl.place(x=600 , y=170)

# condition lable
condition_lbl = tk.Label(window , font=("arial" , 15 , "bold"), fg="#2F2F4F")
condition_lbl.place(x=590 , y=270)

# wind lable
wind_lbl = tk.Label(window , text="   " , font=("arial" , 20 , "bold") , bg="#1ab5ef" , fg="#2F2F4F")
wind_lbl.place(x=120 , y=438)

# humidity lable
humidity_lbl = tk.Label(window , text="   " , font=("arial" , 20 , "bold") , bg="#1ab5ef" , fg="#2F2F4F")
humidity_lbl.place(x=305 , y=438)

# description lable
description_lbl = tk.Label(window , text="   " , font=("arial" , 20,"bold" ) , bg="#1ab5ef" , fg="#2F2F4F")
description_lbl.place(x=465 , y=438)

#pressure lable
pressure_lbl = tk.Label(window , text="   " , font=("arial" , 20 ,"bold" ) , bg="#1ab5ef" , fg="#2F2F4F")
pressure_lbl.place(x=700 , y=438)


window.mainloop()
