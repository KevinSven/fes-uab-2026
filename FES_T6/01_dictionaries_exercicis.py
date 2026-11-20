###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.
estudiant = {
    "nom": "Kevin",
    "edat": 19,
    "assignatures": ["FES", "CiCE", "RiOG"]
}
print(estudiant["nom"])
print(estudiant["edat"])
print(estudiant["assignatures"])

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.
print(estudiant["assignatures"][1])
estudiant["edat"] = 21
print(estudiant["edat"])
# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.
estudiant["grau"] = "Enginyeria de Telecomunicacions"
del estudiant["edat"]
# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print("nom" in estudiant)
print("email" in estudiant)

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".
for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")
# Exercici 6: Comptar paraules
# Donada la llista de paraules:
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
comptador = {}
for paraula in paraules:
    if paraula in comptador:
        comptador[paraula] +=1
    else:
        comptador[paraula] = 1
print(comptador)