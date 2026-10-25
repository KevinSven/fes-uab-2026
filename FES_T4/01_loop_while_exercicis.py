###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

comptador = 10
while comptador >= 1:
    print(comptador)
    comptador -= 1


# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

numero = 1
suma_parells = 0

while numero <= 20:
    if numero % 2 == 0:
        suma_parells += numero
    numero += 1

print(f"La suma dels números parells entre 1 i 20 és: {suma_parells}")


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.

num_factorial = int(input("Introdueix un número enter positiu: "))
factorial = 1
i = 1

while i <= num_factorial:
    factorial *= i
    i += 1

print(f"El factorial de {num_factorial} és: {factorial}")


# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.

contrasenya = input("Introdueix una contrasenya (mínim 8 caràcters): ")

while len(contrasenya) < 8:
    print("La contrasenya és massa curta!")
    contrasenya = input("Introdueix una contrasenya (mínim 8 caràcters): ")

print("Contrasenya vàlida")


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

num_taula = int(input("Introdueix un número per veure la seva taula de multiplicar: "))
multiplicador = 1

while multiplicador <= 10:
    print(f"{num_taula} x {multiplicador} = {num_taula * multiplicador}")
    multiplicador += 1


# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.

n = int(input("Introdueix un número enter positiu N: "))
candidat = 2

print(f"Números primers fins a {n}:")
while candidat <= n:
    es_primer = True
    divisor = 2
    
    # Comprovem si el candidat té algun divisor a banda de 1 i ell mateix
    while divisor < candidat:
        if candidat % divisor == 0:
            es_primer = False
            break
        divisor += 1
        
    if es_primer:
        print(candidat)
        
    candidat += 1


# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.

suma_total = 0
num_introduit = int(input("Introdueix un número enter (0 per acabar): "))

while num_introduit != 0:
    suma_total += num_introduit
    num_introduit = int(input("Introdueix un altre número enter (0 per acabar): "))

print(f"La suma total és: {suma_total}")


# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.

num_xifres = int(input("Introdueix un número enter positiu: "))
temp = num_xifres
comptador_xifres = 0

# Manejem el cas especial de l'0
if temp == 0:
    comptador_xifres = 1
else:
    while temp > 0:
        temp //= 10  # Eliminem l'última xifra mitjançant divisió entera
        comptador_xifres += 1

print(f"El número {num_xifres} té {comptador_xifres} xifres.")


# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.

termes = int(input("Quants termes de Fibonacci vols veure? "))

a, b = 0, 1
comptador_fib = 0

while comptador_fib < termes:
    print(a)
    a, b = b, a + b
    comptador_fib += 1


# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while fins que l'encerti.

SECRET = 7
intent = int(input("Endevina el número secret: "))

while intent != SECRET:
    if intent < SECRET:
        print("El número secret és MÉS GRAN.")
    else:
        print("El número secret és MÉS PETIT.")
    intent = int(input("Torna a provar: "))

print("Felicitats! Has encertat el número secret.")