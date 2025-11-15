packs = int(input("¿Cuántos paquetes? "))
normal = 0
express = 0
urgent = 0
for pack in range(packs):
    print(f"\nPaquete {pack + 1}: ")
    type = input("Tipo (normal/express/urgente): ").lower()
    if type == "normal":
        normal +=1
    elif type == "express":
        express +=1
    elif type == "urgent":
        urgent +=1
    else:
        print("Tipo no valido. ")
print("\nRESULTADOS ")
print(f"Normal: {normal} ")
print(f"Express: {express}")
print(f"Urgent: {urgent} ")
