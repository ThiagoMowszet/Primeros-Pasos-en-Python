# Mis primeros pasos en Python.

# Dia 1 = 4/4/2022

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



'''

Operadores Logicos

Prioridad:
not, and y or

'''
