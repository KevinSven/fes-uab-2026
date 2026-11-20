# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
tupla =('Barcelona', 'Madrid', 'Córdoba', 'París', 'Matalascañas')
print(tupla[1])
print(tupla[3])
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
tupla2 = (2,8,3,7,1,6,4,2,1,3,7,3)
comptador = 0
for num in tupla2:
    if num == 3: 
        comptador += 1
print(comptador)
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def tupla_ordenada(tupla):
    tupla_nova = tuple(sorted(tupla))
    return tupla_nova

print(tupla_ordenada((9,8,3,2,4,6,6)))