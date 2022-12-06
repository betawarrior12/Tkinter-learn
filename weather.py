from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Code with Betawarrior12")
root.geometry("650x40")
root.iconbitmap("Images\\betawarrior.ico")



try:
    URL = #your query url
    api_request = requests.get(URL)
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    AQI = api[0]["AQI"]
    Category = api[0]["Category"]["Name"]
    #Add checks

    myLabel = Label(root, text=city + "," + " " + str(AQI) +  " " + "Degrees" "," + "Category:" + " " + Category + "," + " " , font=("romans",(20)), background="green")
    myLabel.pack()

except Exception as e:
    print(e)


root.mainloop()
