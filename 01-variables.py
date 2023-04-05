'''
Debemos tomar en cuenta que con PYTHON no "debemos" de utilizar la notacion Camello el momento de crear
variables, es recomentado usar mejor solo MINUSCULAS & notacion SNAKE. 

mi_nueva_variable = ''

cuando necesitemos, por alguna razon utilizar el nombre de una varieable pero esta sea una palabra reservada
bastara con colocar un guin bajo en su inicio:

_if = ''

Tomemos en cuenta tambien que hola, Hola y HOLA, PYTHON las tomara como diferentes variables.
'''
mi_variable = "Esta es mi primer variable en PYTHON"
print(mi_variable)

var_string = "Hello Friend"
var_int = 56
var_bool = True
var_float = 3.1416

print(var_bool, var_float, var_int, var_string)

#Cambiamos de tipo de datos para ver como se hace. 

var_int_to_string = str (var_int)
var_float_to_string = str(var_float)


print(len(var_string)) #esta funcion sirve para contar los caracteres de un string.
