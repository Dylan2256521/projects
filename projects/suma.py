#suma de numeros
cantidad = int(input("Cuantos numeros quieres sumar"))

suma = 0

for i in range(cantidad):
    numero = float(input(f"Introduce el numero {i+1}: "))
    suma += numero
print("La suma de los numeros es:", suma)