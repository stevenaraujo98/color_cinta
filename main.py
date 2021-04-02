import cv2
import tkinter as tk
import PIL.Image, PIL.ImageTk
import glob
import time

class Aplicacion:
    def __init__(self, dir_image):
        self.click = 0, 0
        self.click_number = 0
        self.list_rois = []
        self.name_image = dir_image.split('\\')[2].split('.')

        self.window=tk.Tk()
        self.window.title("Ventana")

        self.img_color = cv2.imread(dir_image)
        h, w, _ = self.img_color.shape

        self.canvas1=tk.Canvas(self.window, width=w, height=h, background="black")
        self.canvas1.grid(column=0, row=0)
        self.rImg = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(cv2.cvtColor(self.img_color, cv2.COLOR_BGR2RGB)))
        self.canvas1.create_image(0, 0, image=self.rImg, anchor="nw")# 0, 0, de donde se ubica image, anchor 

        #bindear
        self.canvas1.bind('<Double-Button-1>', self.enter)
        self.window.bind('<Return>', self.close)

        self.window.mainloop()

    def enter(self, event):
        x_tmp = event.x
        y_tmp = event.y
        print("clicked at", x_tmp, y_tmp)
        if(self.click_number == 0):
            self.click = x_tmp, y_tmp
        elif(self.click_number == 1):
            x1, y1 = self.click
            self.canvas1.create_rectangle(x1, y1, x_tmp, y_tmp, fill="#18c194",width=1, stipple="gray50")
            self.list_rois.append((x1, y1, x_tmp, y_tmp))
            self.click = 0, 0
            print(self.list_rois)
        
        self.click_number += 1
        if(self.click_number == 2):
            self.click_number = 0

    def close(self, event):
        print('close')
        format_time = time.strftime("%d-%m-%Y-%H-%M-%S")
        contador = 0
        for i in self.list_rois:
            x1, y1, x2, y2 = i
            new_name = self.name_image[0] + '_' + format_time + '_' + str(contador)
            new_img = self.img_color[y1:y2, x1:x2]

            frameHSV = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
            fic = open('./result/' + new_name + '.txt', "w")
            for j in frameHSV.reshape(-1, 3):
                fic.write(str(j[0]) + ',' + str(j[1]) + ',' + str(j[2]) + '\n')
            fic.close()

            cv2.imwrite('./result/hsv_' + new_name + '.' + self.name_image[1], frameHSV)
            cv2.imwrite('./result/rgb_' + new_name  + '.' + self.name_image[1], new_img)
            contador+=1
        self.list_rois = []
        self.window.destroy()
       
raiz = '.\\img\\*'
rutas = glob.glob(raiz, recursive=False)

for i in rutas:
    aplicacion1=Aplicacion(i)