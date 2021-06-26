import tkinter
from tkinter import *
import requests
from datetime import datetime
from tkinter import messagebox

def weather_data():
    city = city_entry.get()
    user_api = "832d6852f929bc0767e280c5386545e4"
    api_link = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api
    api_get_link = requests.get(api_link)
    api_data = api_get_link.json()
    if api_data['cod'] == '404':
        tkinter.messagebox.showerror("weather_prediction","City not found please check spelling!!")
    else:
        temp_city = api_data['main']['temp'] - 273.5
        format_temp_city = "{:.2f}".format(temp_city)
        weather_descriptions = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %y | %I:%M:%S:%P")

        temp_city_lbl = Label(window,font="Times 30 bold",text=f"Temperature :{format_temp_city} C")
        weather_descriptions_lbl = Label(window,font="Times 30 bold",text=f"Weather :{weather_descriptions}")
        humidity_lbl = Label(window,font="Times 30 bold",text=f"Humidity :{humidity}")
        wind_speed_lbl = Label(window,font="Times 30 bold",text=f"Wind :{wind_speed} km/h")
        date_time_lbl = Label(window,font="Times 30 bold",text=f"date_time :{date_time}")
        temp_city_lbl.grid(row=4,column=0)

        weather_descriptions_lbl.grid(row=5,column=0)
        humidity_lbl.grid(row=6,column=0)
        wind_speed_lbl.grid(row=7,column=0)
        date_time_lbl.grid(row=8,column=0)

window = tkinter.Tk()
window.title("Weather report")
window.minsize(500,500)

city_label = Label(window,text="Enter City Name ", width="30",font="Times 30 bold", bg='black', fg='white', height=1)
city_label.grid(row=0,column=0)

city_entry = tkinter.Entry(window,text="City",width=30,borderwidth=5)
city_entry.config(font=("Arial",25,"bold"))
city_entry.grid(row=1)

submit_btn = Button(window,text="get weather data",bd=3, bg='Black',fg='white',command=weather_data)
submit_btn.grid(row=2)

window.mainloop()

