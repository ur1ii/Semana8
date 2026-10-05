#Leer los nombres, apellidos, edad y carrera de un estudiante
#Guardarlo en un archivo llamado estudiante.txt

nombres = input("Ingrese sus nombres: ")
apellidos = input("Ingrese sus apellidos: ")
edad = input("Ingrese tu edad: ")
carrera = input("Ingresa tu carrera: ")

datos = f"Nombres: {nombres.title()}\n Apellidos: {apellidos.title()}\n Edad: {edad.title()}\n Carrera: {carrera.title()}\n"

with open("estudiante.txt", "a+", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo creado satisfactoriamente...")