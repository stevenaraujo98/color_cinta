import cv2
import tkinter as tk
import PIL.Image, PIL.ImageTk
import glob

class Aplicacion:
    def __init__(self, dir_image):
        self.window=tk.Tk()
        self.window.title("Ventana")

        img_color = cv2.imread(dir_image)
        h, w, _ = img_color.shape

        self.canvas1=tk.Canvas(self.window, width=w, height=h, background="black")
        self.canvas1.grid(column=0, row=0)
        self.rImg = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)))
        self.canvas1.create_image(0, 0, image=self.rImg, anchor="nw")# 0, 0, de donde se ubica image, anchor 

        #bindear
        self.canvas1.bind('<Double-Button-1>', self.enter)
        self.window.bind('<Return>', self.close)

        self.window.mainloop()

    def enter(self, event):
        print('enter')

    def close(self, event):
        print('close')
        self.window.destroy()
       
raiz = '.\\img\\*'
rutas = glob.glob(raiz, recursive=False)

for i in rutas:
    aplicacion1=Aplicacion(i)