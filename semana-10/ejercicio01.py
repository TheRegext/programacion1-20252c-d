# Crear un programa que permita registrar las notas de varios alumnos y luego mostrar algunos resultados.
# Por cada nota se carga:
# Legajo
# Codigo de Materia
# Nota
# Dispone de las siguientes materias:
#    120 - Matemáticas
#    300 - Programación
#    301 - Arquitectura y Sistemas operativos
#    304 - Organización Empresarial
# El programa debe finalizar cuando se ingrese un legajo igual a cero
# El programa debe mostrar:
# A) Listado de todos los alumnos (legajos) que hicieron examenes.
# B) Mostrar las materias que no registraron exámenes.
# C) Por cada alumno, el promedio de notas.

list = set()
materias_registradas = set()
materias = {
  120:"Matematica",
  300:"Programación",
  301:"Arquitectura y Sistemas operativos",
  304:"Organización Empresarial"
}

alumnos = {}

for codigo, nombre in materias.items():
  print(f"#{codigo} - {nombre}")

while True:
  legajo = input("Ingrese legajo: ")

  if(legajo == "0"):
    break

  codigoMateria = int(input("Ingrese Materia: "))
  nota = int(input("Ingrese nota: "))
  
  #proceso
  list.add(legajo)
  materias_registradas.add(codigoMateria)

  if legajo in alumnos:
    alumnos[legajo]["cantidad"] += 1 
    alumnos[legajo]["suma"] += nota
  else:
    alumnos[legajo] = {"cantidad":1, "suma": nota}


print("A) ----------")
#mostrar los legajos
for legajo in list:
  print(f"Alumno con legajo #{legajo}")

print("B) ----------")
#mostrar las que no estan?
materias_faltantes = set(materias.keys()) - materias_registradas

for codigo in materias_faltantes:
  print(materias[codigo])

print("C) ----------")

for legajo, valores in alumnos.items():
  print(f"El alumno #{legajo:} obtuvo:{valores["suma"] / valores["cantidad"]} " )