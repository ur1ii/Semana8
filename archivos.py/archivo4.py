#Crear un programa que permita guardar n cantidad de notas en un archivo, leer las notas, calcular el promedio, la nota mas alta y la nota mas baja
guardarNota = []
Nnotas = input("Ingrese la cantidad de notas: ")
for notas in range(len(Nnotas)):
    notes = input("Ingrese una nota: ")
    guardarNota = notes
    
with open("notasEstudiantes.txt", "a+", encoding="utf-8") as archivo:
    archivo.writelines(guardarNota) 
print("Archivo creado satisfactoriamente...")

with open("notasEstudiantes.txt", "a+", encoding="utf-8") as archivo:
    contenido = archivo.read()
    archivo.read(contenido)
    SumaN = sum(notes)
    promedio = SumaN/len(notes)
with open("notasEstudiantes.txt", "a+", encoding="utf-8") as archivo:
    archivo.writelines(promedio) 
print("Promedio guardado satisfactoriamente...")



