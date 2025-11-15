invoices = int(input("Cuantas facturas va a ingresar? "))
total = 0
for invoice in range(invoices):
    print(f"Factura {invoice + 1}: ")
    client = input("Cliente: ")
    value = float(input("Valor: $ "))
    type = input("Tipo (normal/premium):  ").lower
    if type == "premium":
        discount = value * 0.10
    else:
        discount = value * 0.05   
    final_value = value - discount
    total += final_value
    print(f"Descuento: ${discount: .0f}")
    print(f"Total a pagar: ${final_value: .0f}")
print(f"\nTOTAL GENERAL: ${total: .0f}")