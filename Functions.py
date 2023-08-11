import API
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
import tkinter.messagebox as tkM

def load_image_from_url(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    return image

def DELETE_ALL(labelImage,entryName,entryYear,entryDate,entryDuration,textPlot,entryRating):
    entryName.config(state="normal")
    entryYear.config(state="normal")
    entryDate.config(state="normal")
    entryDuration.config(state="normal")
    textPlot.config(state="normal")
    entryRating.config(state="normal")

    entryName.delete(0,END)
    entryYear.delete(0,END)
    entryDate.delete(0,END)
    entryDuration.delete(0,END)
    textPlot.delete(1.0,END)
    entryRating.delete(0,END)
    
    entryDate.config(state="readonly")
    entryDuration.config(state="readonly")
    textPlot.config(state="disabled")
    entryRating.config(state="readonly")

    image1 = Image.open("FondoAzul.png")
    image1 = image1.resize((300,400), Image.Resampling.LANCZOS)
    image2 = ImageTk.PhotoImage(image1)
    labelImage = labelImage.config(image=image2)
    labelImage.image = image2


def SEARCH(labelImage,entryName,entryYear,entryDate,entryDuration,textPlot,entryRating):
    try:
        entryDate.config(state="normal")
        entryDuration.config(state="normal")
        textPlot.config(state="normal")
        entryRating.config(state="normal")

        name = entryName.get()
        year = entryYear.get()
        #image, title, year, date, duration, plot, rating = API.get_data(name,year)
        values = API.get_data(name,year)
        print(values)
        imageMovie = values[0]    #link of the img
        title = values[1]
        year = values[2]
        date = values[3]
        duration = values[4]
        plot = values[5]
        rating = values[6]

        print(API.info(title, year, date, duration, plot, rating))

        entryDate.delete(0,END)
        entryDuration.delete(0,END)
        textPlot.delete(1.0,END)
        entryRating.delete(0,END)
        
        image1 = load_image_from_url(imageMovie)
        image1 = image1.resize((300,400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image1)

        labelImage.config(image=photo)
        labelImage.image = photo

        entryDate.insert(0,date)
        entryDuration.insert(0,duration)
        textPlot.insert(1.0,plot)
        entryRating.insert(0,rating)  

        entryDate.config(state="readonly")
        entryDuration.config(state="readonly")
        textPlot.config(state="disabled")
        entryRating.config(state="readonly")

    except Exception as e:
        print(e)
        tkM.showerror("ERROR", "Datos no validos o no se encontro la pelicula")
        print("No se encontro la pelicula o alguno de los datos es incorrecto\n")
        DELETE_ALL(labelImage,entryName,entryYear,entryDate,entryDuration,textPlot,entryRating)
        entryDate.config(state="readonly")
        entryDuration.config(state="readonly")
        textPlot.config(state="disabled")
        entryRating.config(state="readonly")

