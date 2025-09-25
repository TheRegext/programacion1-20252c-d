'''
Un almacén realiza ventas durante todo el día y necesita un programa que le 
permita obtener reportes de manera sencilla.
El programa debe ofrecer un menú de opciones con la siguiente funcionalidad:
1- Cargar productos
    Se debe ingresar el código y el precio de cada producto.
    La carga finaliza cuando se ingresa un código igual a 0.
2- Registrar una venta
    El programa debe solicitar al usuario el código del producto y la cantidad vendida.
    Luego, informar el monto total de la venta.
3- Informe de recaudación
    Mostrar el monto total recaudado hasta el momento.
4- Salir
    Finalizar el programa mostrando un mensaje de agradecimiento:
    “Gracias por utilizar nuestra aplicación :)”
'''

## 100 -- $2000 -> 3 -> $6000
# listas en paralelo
lista_codigos = [100,600]
lista_precios = [2000,1500]
monto_total_recaudado = 0

while True:
  print("------------------")
  print("1- Cargar Producto")
  print("2- Registrar venta")
  print("3- Informe")
  print("4- Salir")
  print("------------------")
  opcion = int(input("Opcion: "))
  print()

  match opcion:
    case 1:
      print ("--- Carga de datos ----")

      while True:
        codigo = int(input("Ingrese codigo de producto: "))
        if codigo == 0:
          break

        precio = float(input("Ingrese precio del producto: "))

        if codigo not in lista_codigos:
          lista_codigos.append(codigo)
          lista_precios.append(precio)
        else:
          print("El codigo ya existe...")

    case 2:
      print("--- Registrar venta ---")
      codigo = int(input("Ingrese codigo de producto: "))
      cantidad = int(input("Ingrese cantidad vendida: "))

      if codigo not in lista_codigos:
        print("El codigo no es valido")
        continue
        
      indice = lista_codigos.index(codigo)
      precio = lista_precios[indice]

      monto = precio * cantidad

      print (f"El monto de la venta es {monto}")

      monto_total_recaudado += monto

    case 3: 
      print("---- Informes ----")
      print(f"El monto recaudado es: {monto_total_recaudado}")
    case 4:
      print("Gracias por utilizar nuestra aplicación :)")
      break # corta el ciclo principal
    case _: #caso por defecto
      print("Opcion no valida...")