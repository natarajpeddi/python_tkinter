import io

import requests
import webbrowser
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk

class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get(url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=<API_key>').json()
        #print(data)

        # initial GUI load
        self.load_gui()

        # load the 1st news item
        self.load_news_items(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='black')
        self.root.title("Latest News by 'Nataraj Peddi'")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_items(self, index):
        #clear the screen for the new news item
        self.clear()

        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
        except:
            img_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAACUCAMAAAD4QXiGAAAAVFBMVEXu7u5mZmbx8fFUVFT19fXQ0NDX19e3t7e8vLzg4OBgYGBPT09ZWVljY2NdXV2qqqrJyclra2uxsbGioqKXl5d2dnbDw8NISEg8PDzn5+d/f3+Ojo7nOqfoAAACRUlEQVR4nO3Z7XKqMBSFYQjRFkoSRGiL3v99NiDKp+dM48xiM13vv2ZQH+M2tjWKdpraGhAc5fgox0c5PsrxUY6PcnyU46McH+X4KMdHOT7K8VGOj3J8lOOjHB/l+CjHRzk+yvFRjo9yfJTjoxwf5fj+sFwFt7FcNcfQNpbr8isJ6zt97bFflr9Z9x5S9bG5PDvqkN4FyA8h96HfKA+N8t8HkLefOYvPnT3IVVpWVTln7kGe1jaztm6mV+1Ari829tmLnt1Oulw1Sdx1Ok4u24E8zXv5YbLpMuXjn1XzcZPHqfg9V9FkQVfdpueV+DlXysXFeKW52tzm10j62eLhmTkVow1WTeFc0Ug/z1Xk/CFo7Jgerf3pJk3ud7w7BE1WrN3x6AkIk3t4fwaa06deXlsOL4U0ucv6IzA2ppjTdZkMh7oouVLnJH5kkvnA+HeAsXe6JPkwKvc+J+e6M6adop4uSj6MSr/r8WhgtLOmW6xvdEny82zH24F5vE37M8eXZd3zESP3M76At4fjfWCcHS22uy5FvpzxyeF4m/HHYu13XYo8Ots1eHs4erqePS3/NlUy5HplxodZL6LF69H+diBBftTP4e0GV2uLBxH/nXNPRqUvW1kz9TXZXn75N/zJS5Ftv+e5+b9zLQHyMDjllP+izc+W3X7DpdJDaK8+8ou33+83udtFOT7K8VGOj3J8lOOjHB/l+CjHRzk+yvFRjo9yfJTjoxwf5fgox0c5PsrxUY6PcnyU46McH+X4KMdHOT7K8akfEtUesfz45NkAAAAASUVORK5CYII="
            raw_data = urlopen(img_url).read()
        image = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(image)
        image_label = Label(self.root, image=photo)
        image_label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350, justify='center', font=('vardana',15))
        heading.pack(pady=(10,2))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350, font=('vardana',12))
        details.pack()

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        left_button = Button(frame, text="Prev", bg='white', fg='black', font=('vardana',10), height=3, width=13, justify='center', command=lambda : self.load_news_items(len(self.data['articles'])-1 if index == 0 else index-1))
        left_button.pack(side='left')

        read_more_button = Button(frame, text='Read More...', bg='white', fg='black', font=('vardana', 10), height=3,width=15, justify='center',command=lambda: self.open_link(self.data['articles'][index]['url']))
        read_more_button.pack(side="left")

        right_button = Button(frame, text='Next', bg='white', fg='black', font=('vardana', 10), height=3, width=13, justify='center', command=lambda : self.load_news_items(0 if index == len(self.data['articles']) - 1 else index + 1))
        right_button.pack(side='left')

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)

obj = NewsApp()