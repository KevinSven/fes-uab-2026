###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
i = 0
for num in range(2,21,2):
    print(num)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
suma = 0
for numero in numeros:
    suma+=numero
mitjana = suma/len(numeros)
print(f"La mitjana és: {mitjana}")


# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
max = numeros[0]
for numero in numeros:
    if numero > max:
        max = numero
print(max)
    
# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
nova_llista = [] 
for paraula in paraules:
    if len(paraula) > 5:
        nova_llista.append(paraula)
print(nova_llista)
        
# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
#paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]

lletra = input("Introdueix una lletra: ").lower()
comptador = 0

for paraula in paraules:
    if paraula.lower().startswith(lletra):
        comptador += 1

print(f"Hi ha {comptador} paraules que comencen per '{lletra}'.")
# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
# tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]

suma = 0
for tensio in tensions:
    suma += tensio

mitjana = suma / len(tensions)
print(f"La tensió mitjana és: {mitjana} V")
# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
V = 12
resistencies = [100, 220, 470, 1000]

for R in resistencies:
    I = V / R
    print(f"Resistència de {R} Ω -> Corrent: {I:.4f} A")
# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
nivells_soroll = [-92, -85, -78, -95, -81, -88]
llindar = -80
comptador = 0

for nivell in nivells_soroll:
    if nivell > llindar:
        comptador += 1

print(f"Nombre de mostres que superen els -80 dBm: {comptador}")
# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts     = [1, 0, 0, 1, 0, 1, 1, 0]

bits_diferents = 0
for i in range(len(bits_transmesos)):
    if bits_transmesos[i] != bits_rebuts[i]:
        bits_diferents += 1

taxa_error = bits_diferents / len(bits_transmesos)
print(f"Nombre de bits diferents: {bits_diferents}")
print(f"Taxa d'error (BER): {taxa_error}")
# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segon
frequencies = [50, 100, 500, 1000]

for f in frequencies:
    T = 1 / f
    print(f"Freqüència: {f} Hz -> Període: {T} s")