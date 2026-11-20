###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom,salutacio='Hola'):
    print(f"{salutacio} {nom}!")
saludar_a('Kevin')
# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    if numero%2==0:
        return True
    else:
        return False
print(es_parell(5)) #False
# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    for numero in numeros: #numero coge el valor de cada posición de la lista en cada vuelta
        suma += numero
    return suma/len(numeros)        
print(mitjana([4,7,10]))
# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):#*args permite poner la cantidad de numeros que quieras dentro del paréntesis
    suma = 0
    for numero in args:
        suma += numero
    return suma
print(sumar_tot(2,3,5,6,4,3,3,5,8))
# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for i in range(0,limit):
        print(f"{numero}x{i} = {numero*i}")
taula_multiplicar(7)
# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):#**kwargs significa keyword arguments --> acepta argumentos que vienen con nombres
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(edat = 19, nom = 'Kevin', grau="Enginyeria de Telecomunicació")
# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no està definit per a nombres negatius.")
    resultat = 1
    comptador = 1
    while comptador <= n:
        resultat *= comptador
        comptador += 1
    
    return resultat

print(factorial(5)) 

def maxim_llista(numeros):
    if not numeros:
        return None  # O pots llançar un ValueError si la llista està buida
    valor_max = numeros[0]
    for num in numeros:
        if num > valor_max:
            valor_max = num
    return valor_max

print(maxim_llista([12, 82, 74, 64, 73, 8]))  # 82
# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    lletres = 'aeiou'
    comptador = 0
    for caracter in text.lower():
        if caracter in lletres:
            comptador+= 1
    print(comptador)
comptar_vocals('elefante')

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    valor_max = numeros[0]
    valor_min = numeros[0]
    for num in numeros:
        if num > valor_max:
            valor_max = num
        elif num < valor_min:
            valor_min = num
    print(valor_max)
    print(valor_min)
minim_i_maxim([12,2,23,4,1,-4])
# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari
def es_palindrom(text):
    invertida = text[::-1]
    if text == invertida:
        return True
    else:
        return False
print(es_palindrom('ana'))