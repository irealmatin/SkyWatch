import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def GetWeather():
    pass

window = tk.Tk()


window.title("Weather App")
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


window.mainloop()


