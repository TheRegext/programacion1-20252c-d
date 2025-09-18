'''
 Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana.
'''

ventas = [
    [10, 15, 20, 12, 18, 25, 14],  # Producto 1
    [5, 8, 12, 10, 15, 9, 7],      # Producto 2
    [20, 18, 15, 22, 19, 17, 21],  # Producto 3
    [12, 14, 16, 18, 20, 13, 15]   # Producto 4
]

#Mostrar el total vendido por cada producto. 
#numeroProducto = 0
max = 0
pmax = 0

for i, producto in enumerate(ventas):
  total = 0
 # numeroProducto += 1
  for dia in producto:
   total += dia
   
  print (f"Ventas del producto #{i + 1}: {total}")
  if total > max:
    max = total
    pmax = i + 1

#Mostrar el día con mayores ventas totales.
max = 0
dmax = 0

for dia in range(7): # 0 - 6 
  total = 0
  for prod in range(4):
    total += ventas[prod][dia]
  # en total lo que se vendio durante ese dia
  if total > max:
    max = total
    dmax = dia + 1

print(f"El dia con mayor ventas fue el {dmax} ")

#Indicar cuál fue el producto más vendido en la semana
print(f"El producto mas vendido fue el #{pmax}")