###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

n1,n2 = float(input("Introdueix dos nombres: "))

if n1 > n2:
    print(f"El num més gran és {n1}")
else:
    print(f"El num més gran és {n2}")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
n1,n2 = float(input("Introdueix dos nombres: "))
op = input("Introdueix l'operació (+,-,/,*): ")

if op == '+':
    resposta = n1+n2
    print(f"El resultat és: {resposta}")
elif op == '-':
    resposta = n1-n2
    print(f"El resultat és: {resposta}")
elif op == '/':
    if n2 == 0:
        print(f"¡No es pot dividr un num entre 0!")
    resposta = n1/n2
    print(f"El resultat és: {resposta}")
    
elif op == '*':
    resposta = n1*n2
    print(f"El resultat és: {resposta}")
    

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int (input("Introdueix un any: "))

if any%4 == 0:
    if any%100 == 0:
        if any%400 == 0:
            print("L'any és de trespàs!")
        else:
            print("L'any NO és de trespàs!")
    else:
        print("L'any és de trespàs!")
else:
    print("L'any NO és de trespàs!")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edat = int (input("Introdueix l'edat: "))
if edat >= 0 and edat <=2:
    print("Nadó")
elif edat >= 3 and edat <=12:
    print("Infant")
elif edat >= 13 and edat <= 17:
    print("Adolescent")
elif edat >=18 and edat<=64:
    print("Adult")
elif edat >= 65:
    print("Persona Gran")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

nivell_senyal = int(input("Escriu el nivell de senyal rebut en dBm: "))
if nivell_senyal >= -50:
    print("Excel·lent")
elif nivell_senyal >= -67 and nivell_senyal < -50:
    print("Bona")
elif nivell_senyal >= -75 and nivell_senyal < -67:
    print("Feble") 
elif nivell_senyal < -75 :
    print("Molt Feble")   
    

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

pot_optica = int (input("Introdueix la potència òptica rebuda en Dbm: "))

if pot_optica >= -27 and pot_optica <= -8:
    print("Acceptable")
elif pot_optica < -27:
    print("Massa Baix")
elif pot_optica > -8:
    print("Massa Alt")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float (input("Introdueix el consum de dades en GB: "))
pla = 20
if consum > 20:
    addicionals = consum - 20
    print(f"Has consumit {addicionals:.2f} GB addicionals!")
elif consum < 0:
    print("No és possible consumir un num negatiu de dades! :^(")
else:
    print("El consum és dins del límit")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los_ences = input("L'indicador LOS està encès? (sí/no): ").strip().lower() == "sí"
internet_ences = input("L'indicador d'Internet està encès? (sí/no): ").strip().lower() == "sí"

if los_ences:
    print("Cal revisar el cable de fibra.")
elif not internet_ences:
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")


# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = float(input("Introdueix el percentatge de bateria (0-100%): "))

if bateria < 0 or bateria > 100:
    print("Error: El valor de la bateria ha d'estar entre el 0 % i el 100 %.")
elif bateria < 20:
    print("Nivell de bateria: Crític")
elif bateria <= 49:
    print("Nivell de bateria: Baix")
else:
    print("Nivell de bateria: Suficient")


# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts (0-100%): "))

if latencia < 0 or perdua < 0 or perdua > 100:
    print("Error: Valors introduïts fora de rang o invàlids.")
elif latencia <= 30 and perdua <= 1:
    print("Qualitat de la connexió: Excel·lent")
elif latencia <= 80 and perdua <= 3:
    print("Qualitat de la connexió: Bona")
elif latencia <= 150 and perdua <= 5:
    print("Qualitat de la connexió: Acceptable")
else:
    print("Qualitat de la connexió: Deficient")


# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = input("Introdueix el tipus de pla (bàsic/plus): ").strip().lower()
consum = float(input("Introdueix el consum mensual en GB: "))

if consum < 0 or pla not in ["bàsic", "basic", "plus"]:
    print("Error: Consum negatiu o tipus de pla desconegut.")
else:
    if pla in ["bàsic", "basic"]:
        base = 10.0
        limit = 10.0
        preu_extra = 1.50
    else:
        base = 20.0
        limit = 30.0
        preu_extra = 0.75

    exces = max(0.0, consum - limit)
    cost_total = base + (exces * preu_extra)
    print(f"El cost total del pla és de {cost_total:.2f} €.")


# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte_actiu = input("El compte està actiu? (sí/no): ").strip().lower() == "sí"

if not compte_actiu:
    print("Accés denegat: El compte està desactivat.")
else:
    contrasenya_ok = input("La contrasenya és correcta? (sí/no): ").strip().lower() == "sí"
    if not contrasenya_ok:
        print("Accés denegat: La contrasenya és incorrecta.")
    else:
        codi_ok = input("El codi de doble verificació és correcte? (sí/no): ").strip().lower() == "sí"
        if not codi_ok:
            print("Accés denegat: El codi de doble verificació ha fallat.")
        else:
            print("Accés permès: Benvingut!")


# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router_ences = input("El router està encès? (sí/no): ").strip().lower() == "sí"

if not router_ences:
    print("Cal encendre el router.")
else:
    los_ences = input("L'indicador LOS està encès? (sí/no): ").strip().lower() == "sí"
    if los_ences:
        print("Cal revisar el cable de fibra.")
    else:
        internet_ences = input("L'indicador d'Internet està encès? (sí/no): ").strip().lower() == "sí"
        if not internet_ences:
            print("Cal contactar amb el proveïdor.")
        else:
            print("La connexió funciona correctament.")


# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

servei_critic = input("Afecta un servei crític? (sí/no): ").strip().lower() == "sí"
usuaris = int(input("Introdueix el nombre d'usuaris afectats: "))
alternativa = input("Hi ha una alternativa de connexió disponible? (sí/no): ").strip().lower() == "sí"

if usuaris < 0:
    print("Error: El nombre d'usuaris afectats no pot ser negatiu.")
else:
    sense_alternativa = not alternativa

    if (servei_critic and sense_alternativa) or (usuaris >= 50 and sense_alternativa):
        print("Prioritat: Crítica")
    elif usuaris >= 10 or servei_critic:
        print("Prioritat: Alta")
    else:
        print("Prioritat: Baixa")