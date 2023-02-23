#Zad1
lista = [x for x in range(1, 11)]
print(lista)

lista, lista2 = lista[:5], lista[5:]
print(lista)
print(lista2)

#Zad2
lista = lista + lista2
lista.insert(0, 0)
lista2 = lista.copy()
lista2.sort(reverse=True)
print(lista)
print(lista2)

#Zad3
imie = "Szymon".casefold()
nazwisko = "Śliwa".casefold()

lista3 = [list(imie), list(nazwisko)]
print(lista3)
for element in lista3: element[0] = element[0].capitalize()
print(lista3)

#Zad4

def foo(zdanie):
    return zdanie.replace(".", "").replace(",", "").split()

print(foo("Jakieś dowolnie długie zdanie..."))