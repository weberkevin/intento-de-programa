from tkinter import *
import tkinter as tk 
from ventas import Ventas
from inventario import Inventario
from PIL import Image,ImageTk

class Container (tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0 , y=0, width=800, height=400)
        self.config(bg="#C6D9E3")
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650")
        top_level.resizable(False,False)

    def ventas (self):
        self.show_frames(Ventas)

    def inventario (self):
        self.show_frames(Inventario)        

    def widgets(self):

        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)
        
        btnventas = Button(frame1, bg="green", fg="black",font="sans 18 bold" , text="ir a ventas", command=self.ventas)
        btnventas.place(x=500, y=30, width=240, height=60)

        btninventario = Button(frame1, bg="blue", fg="black",font="sans 18 bold" , text="ir a inventario", command=self.inventario)
        btninventario.place(x=500, y=130, width=240, height=60)

        self.logo_image=Image.open("imagenes/images.jfif")
        self.logo_image= self.logo_image.resize((280,280))
        self.logo_image= ImageTk.PhotoImage(self.logo_image)
        self.logo_label= tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=100, y=30)

        copyright_label= tk.Label(frame1,text="Copyright 2025 InnovaSoft Code. No me copie gato", fg="gray", font=("sans 12 bold"),bg="#C6D9E3" )
        copyright_label.place(x=180, y=350)