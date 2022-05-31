calif = int(input ("Calificación de AZ-900: ")) # Todo lo que viene de la entrada estandar (teclado) es un String
if calif < 700:
    print("No pasaste")
elif calif > 1000:
    print("No se puede obtener más de 1000 puntos")
else:
    print("Felicidades!!!, Pasaste")


# ------------------------ Verificador de edad ------------------------
# En Python no hay switch - case
edad = int(input("Ingresa edad:"))
if edad >= 18 and edad <= 100: # Uso de operador AND (&)
    print("Mayor de edad")
elif edad >= 100:
    print("Demasiado viejo")
elif edad < 0:
    print("Imposible")
else:
    print("Menor de edad")