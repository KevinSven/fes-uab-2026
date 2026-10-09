###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic, nom_xarxa = input("Quin és el teu nom i el nom de la xarxa que estàs instal·lant? ").split()
print(f"El nom del tecnic és {nom_tecnic} i el de la xarxa és {nom_xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud, v_trans = map(float,input("Introdueix la longitud de l'enllaç de fibra en km i la velocitat de transmissió en Gbps: ").split())
#map. aplica una función a cada elemento de un iterable, en este código aplica float a cada texto que devuelve .split
temps = 8 / v_trans
print(f"Caldrien {temps} segons per transmetre 1GB de dades")
# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

nombre_hores, preu_hora = map(float, input("Quantes hores de feina hi haurà i quin es el preu per hora d'una instal·lació de xarxa? ").split())
preu_material = float(input("Quin és el preu del material? "))
cost_total = (nombre_hores*preu_hora)+preu_material
print(f"El cost total de la instal·lació és de: {cost_total}€")