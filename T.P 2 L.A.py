Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Saludar")
    print("2. Calcular suma")
    print("3. Mostrar números del 1 al 10")
...     print("4. Salir")
...     print("====================================")
... 
... def opcion_1():
...     nombre = input("Ingrese su nombre: ")
...     print(f"¡Hola, {nombre}! Bienvenido al programa")
... 
... def opcion_2():
...     try:
...         a = float(input("Ingrese el primer número: "))
...         b = float(input("Ingrese el segundo número: "))
...         print(f"La suma de {a} + {b} es = {a + b}")
...     except ValueError:
...         print("⚠️ Error: Debe ingresar solo números.")
... 
... def opcion_3():
...     print("Números del 1 al 10:")
...     for i in range(1, 11):
...         print(i, end=" ")
...     print("\n")
... 
... def main():
...     while True:
...         mostrar_menu()
...         opcion = input("Seleccione una opción: ")
... 
...         if opcion == "1":
...             opcion_1()
...         elif opcion == "2":
...             opcion_2()
...         elif opcion == "3":
...             opcion_3()
...         elif opcion == "4":
...             print("Saliendo del programa... adios")
...             break
...         else:
...             print("Opción no válida. Intente nuevamente.")
... 
... if __name__ == "__main__":
