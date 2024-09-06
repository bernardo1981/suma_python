# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Preguntar al usuario si quiere sumar o restar
operacion = input("¿Quieres sumar o restar el número consigo mismo? (Escribe 'sumar' o 'restar'): ").lower()

# Realizar la operación según la elección del usuario
if operacion == 'sumar':
    resultado = numero + numero
    print("El resultado de la suma es:", resultado)
elif operacion == 'restar':
    resultado = numero - numero
    print("El resultado de la resta es:", resultado)
else:
    print("Operación no válida. Debes escribir 'sumar' o 'restar'.")
