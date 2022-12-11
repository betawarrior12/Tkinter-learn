from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Code with Betawarrior12")
root.geometry("520x80")
root.iconbitmap("Images\\betawarrior.ico")

def weather(zipcode):
    global myLabel
    try:
        myLabel.grid_forget()
        URL = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=1000&API_KEY=D28546FF-8DB8-49EC-A1BB-AF50A0074A6D"
        api_request = requests.get(URL)
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        AQI = api[0]["AQI"]
        Category = api[0]["Category"]["Name"]
        color = ""
        if Category.lower() == "good":
            color = "green"
        elif Category.lower() == "moderate":
            color = "orange"
        elif Category.lower() == "unhealthy for sensitive groups":
            color = "magenta"
        myLabel = Label(root, text=city + " Air Quality " + str(AQI) +  " " + Category, font=("romans", 20), background=color)
        root.configure(background=color)
        myLabel.pack(row=0, column=0, columnspan=2)
        print(myLabel.size())
    except Exception as e:
        print(e)

myLabel = Label(root, text="")
myLabel.grid(row=0, column=0)
zipcode = Entry(root, text="Enter zipcode", width=25)
zipcode.grid(row=1, column=0)
submit = Button(root, text="Enter zipode for weather", command=lambda: weather(zipcode.get()), width=39)
submit.grid(row=1, column=1)

root.mainloop()
