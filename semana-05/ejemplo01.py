# While - Siempre que no sepamos la cantidad de repeticiones
# For   - Recorrer algo o cuando sabemos la cantidad de repeticiones

while condicion:
  # código a repetir
  # Seguna linea

contador = 10
while contador <= 5:
  print(contador)
  # contador += 1

print (contador)

contador = 1
while False: ## hay que tener cuidado de que no sea siempre verdadero
  print(contador)
  contador += 1


numero = int(input("Ingrese numero: "))

while numero != 0:
  numero = int(input("Ingrese numero: "))

# Debe ingresar numero positivo
numero = int(input("Ingrese numero positivo: "))

while numero <= 0:
  numero = int(input("Dije que sea positivo: "))

print("Gracias por ingresar numero correcto!")


for variable in iterable:
  # código a repetir

# Iterables 
## Rage 

for i in range(5): # 0 - 4
  print(i)

for i in range(5, 15): # inicial hasta el final-1
  print(i)

for i in range(5, 15, 2): # inicial hasta el final-1 , con pasos de 2
  print(i)

for i in range(15, 5, -1): 
  print(i)

for i in range(1, 8, 1): 
  print(i)

inicio = 5
fin = 10
for i in range(inicio, fin + 1): # inicial hasta el final-1
  print(i)

# Recorrer Texto
nombre = "Brian"

for i in nombre:
  print(i)

texto = "Hola mundo"
contador = 0
for letra in texto:
  if letra.lower() in "aeiou":
    contador += 1

print("Cantidad de vocales:", contador)

# Recorrer Listas
numeros = [1, 2, 3, 20, 60]

for i in numeros:
    print(i)

# continue - trata de dar la siguiente iteracion
# break    - termina el ciclo

for i in range(10):
  if i == 5:
    break
  
  if i % 2 == 0:
    continue

  print(i)


for i in range(3):
    print(i)
    #if i == 2:
    #  break
else:
    print("El for terminó sin cortes")
