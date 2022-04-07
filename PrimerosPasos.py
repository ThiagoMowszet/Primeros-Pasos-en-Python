# Mis primeros pasos en Python.

# Dia 1 | 04/4/2022

'''

Trabajo con las variables + la funcion Type() y len() para saber
que tipo de datos son nuestras variables y su longitud.

'''

variableNumerica = 25042001
variableCadenaDeTexto = 'El numero de arriba es mi nacimiento'
variableConComa = 2.2
variableVoF = True
variableVoF2 = False 

print(type(variableNumerica))
print(type(variableCadenaDeTexto))
print(type(variableConComa))
print(type(variableVoF))
print(type(variableVoF2))

print(len(variableCadenaDeTexto))



'''
Trabajo con la indexacion, slicing.


'''

a = 'Thiago'

# Quiero acceder a la letra 'g'

print(a[4])

# Accedo a todas las letras

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])


# Slicing de 'h, i, a'

print(a[1:4])


# Slicing de 'T, i, g'

print(a[0:6:2])




'''

Metodos 

'''

# Capitalize 

b = 'thiago eS EL MEJor'

x = b.capitalize()

print(x)



'''

Trabajo inputs del usuario.
*Recordar siempre que la funcion input siempre retorna un str*
Por eso debe ir antes del input lo que querramos, ejemplo int(input("?")) o float(input("?")).

'''


mensaje = int(input("Seleccione un numero: "))
mensaje2 = input("Escriba su inicial del apellido: ")



'''

Trabajo con Operadores: suma, resta, multiplicacion, division, 
division entera, exponente y modulo.

Orden de importancia
PEMDAS (Parentesis, Exponentes, Multiplicacion, Division, Suma, Resta).

'''

#Suma
v = 234 + 4 
print(v)

#Resta
k = 234 - 4
print(k)

#Multiplicacion
l = 3 * 3
print(l)

#Division
y = 15 / 5
print(y)

#Division Entera
i = 234 // 4
print(i)

#Exponente
r = 3**3
print(r)

#Modulo
uu = 98 % 9
print(uu)


# DIA 2 | 07/04/2022

'''

Operadores Logicos y Relacionales

Prioridad = (+ a -)

Not 

and 

or

'''

a = 3543
b = 324
c = 2325

if a > b and a > c:
    print("A es mayor")
elif b > a and b > c:
    print("B es mayor")
else:
    print("C es mayor")


ere = 234 
eree = 234

if ere == eree or eree == ere: 
    print("son iguales")



""" 

Listas

Pueden ser modificadas

"""


lista = ['a', 'b', 'c', 'd', 'f']

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])


# Como agregar un elemento a la lista? 

lista.append(5) # lista = ['a', 'b', 'c', 'd', 'f', 5]

print(lista)


# Como agregar un elemento en un indice en especifico?

lista.insert(5, 'g')  # lista = ['a', 'b', 'c', 'd', 'f', 'g', 5]
print(lista)


# Como remover un elemento?

lista.remove(5)
print(lista) # lista = ['a', 'b', 'c', 'd', 'f', 'g']


# Como encontrar un elemento especifico? 

print('g' in lista)


# Como hacer para que nos retorne el primer elemento del indice

print(lista.index('c'))



# Como cambiar un elemento (Esto es posible gracias a que las listas son mutables. es decir, sus elementos pueden ser modificados.)

lista[4] = 'e'
lista[5] = 'f'
print(lista) # ['a', 'b', 'c', 'd', 'e', 'f']