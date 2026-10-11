#Cree una aplicacion que lea los datos de un estudiante: nombres, apellidos, nota. calcular el promedio de las notas, la nota mas alta y la nota mas baja. Mostrar los 3 estudiantes con mayor nota.
print("=== Datos de Estudiantes ===")
Estudiantes = int(input("Ingrese el numero de estudiantes: "))
datos = []
for i in range(Estudiantes):
    print(f"=== Estudiante #{i+1} ===")
    nombres = input("Ingrese sus 2 nombres: ")
    apellidos = input("Ingrese sus 2 apellidos: ")
    print("=== Nota ===")
    nota = float(input(f"Ingrese la nota del estudiante: "))
    datos.append({
        "nombre":f"{nombres} {apellidos}",
        "nota": nota
    })
notas = [est["nota"] for est in datos]
print("=== Promedio de notas ===")
promedio = sum(notas) / len(notas)
print(f"El promedio de notas es: {promedio:F2}")

print("=== Nota mas alta ===")
notaMasAlta = max(notas)
print(f"La nota mas alta es: {notaMasAlta}")

print("=== Nota mas baja ===")
notaMasBaja = min(notas)
print(f"La nota mas baja es: {notaMasBaja}")

print("=== Los 3 Estudiantes con notas mas altas ===")
estudiantesMayorNota = sorted(datos, key=lambda x: x["nota"], reverse=True)[:3]

for posi, est in enumerate(estudiantesMayorNota, start=1):
    print(f"{posi}. {est['nombre']} | Nota: {est['nota']}")

