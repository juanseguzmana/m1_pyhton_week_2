print("==========SUPERMERCADO DATAMARKET==========")
# PREGUNTAR CANTIDAD DE PRODUCTOS DE MANERA VALIDA
while True:
    try:
        products_quantity =int(input("¿Cuantos productos desea registrar? "))

        if products_quantity > 0 :
            print(f"Perfecto, registraras {products_quantity} productos")
            break
        else :
            print("La cantidad debe ser mayor a 0")
    except ValueError:
        print("Error: Debe ingresar un numero entero")
#LISTA PARA ALMACENAR LOS PRODUCTOS
products = []
#REGISTRAR CADA PRODUCTO
for i in range(products_quantity): 
    print(f"\n--- Producto {i+1} de {products_quantity}")
    #SOLICITAR NOMBRE 
    name = input("Nombre del producto: ")
    #SOLICITAR PRECIO CON VALIDACION
    while True:
        try:
            price = float(input("Precio del producto: "))
            if price > 0:
                break
            else:
                print("El precio debe ser mayor a 0")
        except ValueError:
            print("Error: Ingrese un numero valido para el precio")
    #SOLICITAR SI ESTA VENCIDO
    while True:
        expired = input("¿Esta vencido? (si/no): ").lower()
        if expired in ["si","no"]:
            break
        else:
            print("Error: Responda 'si' o 'no'")
    
    #CREAR DICCIONARIO CON LOS DATOS
    product = {
        'name': name,
        'price': price,
        'expired': expired in ["si"] 
    }
    #AGREGAR A LA LISTA
    products.append(product)
    print("Producto registrado correctamente")
print("\n=== REGISTRO COMPLETADO ===")
#FILTRAR SOLO PRODUCTOS NO VENCIDOS
not_expired = []
for product in products:
    if not product['expired']:
        not_expired.append(product)
#CALCULAR COSTO TOTAL
total_price = 0
for product in not_expired:
    total_price += product['price'] 
#MOSTRAR RESULTADOS
print(f"\n=== PRODUCTOS VÁLIDOS (NO VENCIDOS) ===")
print(f"Total de productos no vencidos: {len(not_expired)}")
for product in not_expired:
    print(f"- {product['name']}: ${product['price']}")
print(f"\nCOSTO TOTAL: ${total_price}")
#PREGUNTAR SI DESEA INGRESAR MAS PRODUCTOS SI - NO
#DESPEDIDA







    
