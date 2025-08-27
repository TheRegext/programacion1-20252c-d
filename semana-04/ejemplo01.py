# hacer un programa que dado un numero positivo indique el nivel de peligrosidad
# si el unmero esta entre 0 y 50 - Nada peligroso
# Si esta entre 51 y 100 - Potencial peligroso
# Si esta entre mas que 100 - Muy peligroso
 
nivel = int(input("Ingrese nivel de peligrosidad: "))

if nivel <= 50:
  print("Nada peligroso")
elif nivel <= 100:
  print("Potencial peligroso")
else:
  print("Muy peligroso")

