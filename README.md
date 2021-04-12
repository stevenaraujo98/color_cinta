# Proyecto
Para procesado de imagen seleccionando rois dentro de la imagen.  
Al presionar "Enter" se guardan las imagenes RGB, HSV y un txt con el HSV de los rois ya elegidos.

#### Necesario:
- En la carpeta **"img"** se situan las imagenes a procesar y una ves ya procesadas son eliminadas
- En la carpeta **"result"** se crearan las respuesta de las imagenes con nombre  
- Se puede usar la carpeta **"originals"** la cual se encuentra ignorada por git para almacenar las imagenes originales y no perderlas  

```
"NOMBREIMAGENORIGEN_dia-mes-año-hora-minutos-segundos_NUMEROITERACION"  
```  

##### ejemplo de nombres origen y resultados:
- img1.jpg
- hsv_img1_02-04-2021-13-26-41_1.jpg
- rgb_img1_02-04-2021-13-26-41_1.jpg
- img1_02-04-2021-13-26-41_1.txt


## Grafico
Lee todas las carpetas de colores en **"results"**, que dentro tienen los archivos con los HSV.
Guarda el resultado de los datos usados para el grafico de frecuencia en la carpeta **"result"**.