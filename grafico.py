# visualizar los H
import glob
import time
from os import remove
import matplotlib.pyplot as plt
import numpy as np

class Lectura:
    def __init__(self, lista_archivos):
        print(len(lista_archivos))
        self.color = lista_archivos[0].split('\\')[2]
        self.dic = {}
        for i in lista_archivos:
            fic = open(i, "r")
            for j in fic.readlines():
                lista = j.strip().split(',')
                k = int(lista[0])
                if k in self.dic:
                    self.dic[k] += 1
                else:
                    self.dic[k] = 1
            fic.close()

    def graficar(self):
        print(self.color)
        self.claves = list(self.dic.keys())
        self.claves.sort()
        x = np.array(self.claves)
        valores = []
        for i in self.claves:
            valores.append(self.dic[i])
        y = np.array(valores)
        plt.bar(x, y, align='center')
        plt.xlim(-1,180)
        plt.title(self.color)
        plt.show()
    
    def guardar(self):
        fic = open('.\\result\\'+self.color+'.txt', 'w')
        fic.write('valor,frecuencia\n')
        for i in self.claves:
            fic.write(str(i) + ',' + str(self.dic[i]) + '\n')
        fic.close()
       
raiz = '.\\results\\*'
rutas = glob.glob(raiz, recursive=False)

saltos = 0
for i in rutas:
    print('='*25)
    rutasImgs = glob.glob(i+'\\*', recursive=False)
    lectura = Lectura(rutasImgs)
    lectura.graficar()
    lectura.guardar()