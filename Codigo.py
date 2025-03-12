# Clase base para los productos
class Producto:
    def __init__(self, nombre, precio, cantidad, atributo_extra=None, valor_extra=None):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        if atributo_extra:
            setattr(self, atributo_extra, valor_extra)  # Añadir atributo extra

# Clase derivada para productos electrónicos
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo, garantia):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de Producto
        self.marca = marca
        self.modelo = modelo
        self.garantia = garantia

    def probar(self):
        print(f"{self.nombre} prende y funciona correctamente")

# Función principal
def main():
    # Lista inicial de productos
    inventario = [
        Producto("Pan", 10, 20),
        Producto("Leche", 30, 15),
        Producto("Arroz", 18.50, 30),
        ProductoElectronico("TV", 1500, 1, "Sony", "X100", "2 años"),
        ProductoElectronico("Cafetera", 350, 1, "Oster", "Model 3000", "1 año")
    ]

    while True:
        print("\n=== La Tienda de la Esquina ===")
        print("1. Agregar nuevo producto")
        print("2. Ver inventario completo")
        print("3. Comprobar producto electronico")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':  # Opción para agregar un nuevo producto
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
            
            agregar_extra = input("¿Desea agregar un atributo adicional? (s/n): ").lower()
            
            if agregar_extra == 's':
                while True:
                    atributo = input("Nombre del atributo adicional: ")
                    if atributo.lower() in ['nombre', 'precio', 'cantidad']:  
                        print("Error: Este nombre está reservado para atributos básicos")
                    else:
                        break
                valor = input(f"Valor para '{atributo}': ")
                nuevo_producto = Producto(nombre, precio, cantidad, atributo, valor)
            else:
                nuevo_producto = Producto(nombre, precio, cantidad)
            
            inventario.append(nuevo_producto)
            print(f"\nProducto '{nombre}' agregado exitosamente!")

        elif opcion == '2':  # Opción para ver el inventario
            print("\n=== Inventario de la Tienda ===")
            for producto in inventario:
                print(f"\nNombre: {producto.nombre}")
                print(f"Precio: ${producto.precio:.2f}")
                print(f"Stock: {producto.cantidad} unidades")
                
                # Si el producto es electrónico, mostrar detalles adicionales
                if isinstance(producto, ProductoElectronico):
                    print(f"Marca: {producto.marca}")
                    print(f"Modelo: {producto.modelo}")
                    print(f"Garantía: {producto.garantia}")
                
                # Mostrar atributos adicionales, si existen
                for atributo, valor in vars(producto).items():
                    if atributo not in ['nombre', 'precio', 'cantidad', 'marca', 'modelo', 'garantia']:
                        print(f"{atributo.capitalize()}: {valor}")

            print("\n" + "="*30)

        elif opcion == '3':  # Opción para verificar si un producto electronico funciona
            producto_funciona = input("\nNombre del producto: ")
            # Buscar el producto en el inventario
            producto_encontrado = None
            for producto in inventario:
                if producto.nombre.lower() == producto_funciona.lower() and isinstance(producto, ProductoElectronico):
                    producto_encontrado = producto
                    break
            
            if producto_encontrado:
                producto_encontrado.probar()
            else:
                print("Producto no encontrado o no es un producto electrónico")
        
        elif opcion == '4':  # Opción para salir
            print("\nGracias por usar nuestro sistema. ¡Hasta pronto!")
            break
        
        else:
            print("\nOpción no válida. Por favor seleccione 1, 2, 3 o 4")

# Iniciar el programa
if __name__ == "__main__":
    main()
