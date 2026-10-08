###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = 'Router XX'
ubi = 'Segona Planta'
nombre_ports = 4
ences = True
print(f'Encaminador: {nom_encaminador}, ubicació: {ubi}, nombre ports: {nombre_ports}, engegat: {ences}')


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB_pla_dades = 100.0
GB_consumits = 84.6
GB_restants = GB_pla_dades - GB_consumits
print(f"Els GB consumits són: {GB_consumits:.2f}") #IMPORTANTE: Antes de poner .2f para troncar poner:
GB_consumits = 92.1
GB_restants = GB_pla_dades - GB_consumits
print(f"Els GB consumits són: {GB_restants:.2f}")

