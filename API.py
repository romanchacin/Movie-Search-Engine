import requests
from PIL import Image
import requests
from io import BytesIO
import tkinter.messagebox as tkM

api_key = 'dc60b9cc'
api_url = f"http://www.omdbapi.com/?apikey={api_key}"

def getMovie(nombre,year):
    newNombre = nombre.replace(" ","+")
    Movie = api_url + "&t=" + newNombre + "&y=" + year + "&plot=full"
    if not year.isdigit() or int(year) < 1900:
        print("El año no es valido")
        tkM.showerror("ERROR", "Datos no validos o no se encontro la pelicula")
        return 0
    movieInfo = requests.get(Movie).json()
    return (movieInfo)

def info(title, year, date, duration, plot, rating):
    information = f"""
Name of the Movie: {title}
Year: {year}
Date: {date}
Duration: {duration}
Plot: {plot}
Rating: {rating}
"""
    return information


def load_image_from_url(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    return image

def get_data(name,year):
    try:
        movie = getMovie(name,year)
        if movie == 0:
            return 0
        else:
            url_image = movie['Poster']
            title = movie['Title']
            year = movie['Year']
            date = movie['Released']
            duration = movie['Runtime']
            plot = movie['Plot']
            rating = movie['Ratings'][0]['Value']
            valores = [url_image, title, year, date, duration, plot, rating]
            return valores
    except:
        print("No se encontro la pelicula o alguno de los datos es incorrecto\n")

