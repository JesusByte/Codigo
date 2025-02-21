# Esta clase llamada producto, asigna una serie de atributos base que se utilzaran mas adelante
class Producto:
    def __init__(self, nombre, precio, cantidad, atributo_extra=None, valor_extra=None):  #Se agrega el espacio para posibles atributos adicionales
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        if atributo_extra:
            setattr(self, atributo_extra, valor_extra) #En caso de atributo extra se agrega 

def main(): #En esta funcion se inicia y dentro se crea la lista del inventario
    inventario = [
        Producto("Pan", 10, 20),
        Producto("Leche", 30, 15),
        Producto("Arroz", 18.50, 30)
    ]

    while True: #Bucle condicional tipo while para mantener al usuario hasta que decida salir del programa
        print("\n=== La Tienda de la Esquina ===")
        print("1. Agregar nuevo producto")
        print("2. Ver inventario completo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1': #Condicional para opcion numero 1, donde se agrega un nuevo producto y sus atributos
            nombre = input("\nNombre del producto: ")
            
            while True:
                try:
                    precio = float(input("Precio del producto: "))
                    break
                except ValueError:
                    print("Error: Ingrese un valor numérico válido para el precio")
            
            while True:
                try:
                    cantidad = int(input("Cantidad en stock: "))
                    break
                except ValueError:
                    print("Error: Ingrese un valor entero válido para la cantidad")
            
            agregar_extra = input("¿Desea agregar un atributo adicional? (s/n): ").lower() #Aqui el programa pregunta al usuario si requiere un atributo adicional
            
            if agregar_extra == 's':
                while True:
                    atributo = input("Nombre del atributo adicional: ")
                    if atributo.lower() in ['nombre', 'precio', 'cantidad']: #Aqui evita que se usen nombres reservados para otros atributos
                        print("Error: Este nombre está reservado para atributos básicos")
                    else:
                        break
                valor = input(f"Valor para '{atributo}': ")
                nuevo_producto = Producto(nombre, precio, cantidad, atributo, valor)
            else:
                nuevo_producto = Producto(nombre, precio, cantidad)
            
            inventario.append(nuevo_producto)
            print(f"\nProducto '{nombre}' agregado exitosamente!")
        
        elif opcion == '2': #Opcion para visualizar el inventario de la tienda incluyendo productos agregados
            print("\n=== Inventario de la Tienda ===")
            for producto in inventario:
                print(f"\nNombre: {producto.nombre}")
                print(f"Precio: ${producto.precio:.2f}")
                print(f"Stock: {producto.cantidad} unidades")
                
              
                atributos = vars(producto)   # Muestra atributos adicionales
                for attr in ['nombre', 'precio', 'cantidad']:
                    atributos.pop(attr, None)
                
                for atributo, valor in atributos.items():
                    print(f"{atributo.capitalize()}: {valor}")
            
            print("\n" + "="*30)
        
        elif opcion == '3': #Sale del programa
            print("\nGracias por usar nuestro sistema. ¡Hasta pronto!")
            break
        
        else:
            print("\nOpción no válida. Por favor seleccione 1, 2 o 3")
