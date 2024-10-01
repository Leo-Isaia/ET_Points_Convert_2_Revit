# 👷🏻‍♂️ - Convertir Puntos de Estación Total a Revit - 👩‍💻
Herramienta desarrollada en Python para convertir archivos CSV/TXT en formato legible por Revit para generar Topografías.


![Descripción de la imagen](https://github.com/Leo-Isaia/ET_Points_Convert_2_Revit/blob/main/images/Screen%20Convert%20ET%20Points.png?raw=true)


En la labor de los Arquitectos / Ingenieros al momento de trabajar con archivos exportados desde un instrumento como un Estación Total, muchas veces los archivos que éstos generan no pueden ser importados a AutoDesk Revit directamente, sino que deben ser manipulados/corregidos/normalizados para que el Software pueda reconocerlos en el formato necesario y así generar correctamente la topografía en 3D.

Con este simple proyecto, usando Python se puede seleccionar el archivo, abrir el mismo, leer su contenido, eliminar la numeración (que es la que genera el desfase por el cual el programa malinterpreta los puntos) y genera un archivo *.txt para ser importado directamente a Revit sin inconvenientes.
Todo ello desde una simple interfaz para el usuario donde podrá consultar los puntos debidamente listados.

Espero les sirva para evitar tener copiar, pegar o manipular los datos en alguna planilla de cálculos, con el posible error humano de por medio.


[Descargar Convertir Puntos ET](https://github.com/Leo-Isaia/ET_Points_Convert_2_Revit/blob/main/Convertir%20Coordenadas%20ET%20para%20Revit.exe)
