###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets = input("Quants paquets ha rebut l'encaminador? ")
total_paquets = int(paquets) + 1200
print(f"El total de paquets és: {total_paquets}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.

velocitat_Mbps = float(input("Introdueix la velocitat d'una connexió en Mbps: "))
velocitat_MB = velocitat_Mbps / 8
print(f"La velocitat equivalent en MB/s és: {velocitat_MB}")