# Es importante saber que PYTHON tiene distintos tipos de operadores, existen operadores SIMPLES, ARITMETICOS
# y de COMPARACION. veremos algunos de ellos en esta clase.

int = 3
int2 = 3
print(int + int2) 

print(4 + 5) # Suma
print(4 - 5) # Resta
print(4 * 5) # Multiplicacion
print(4 / 5) # Division
print(4 % 5) # Modulo (La operacion que se lleva acabo es una division, pero nos muestra lo que resta )
print(4 // 5) # Floor Division (Division que aproxima el resultado a un entero)
print(4 ** 5) # Exponente (Calcula el exponente )

# Con cadenas de texto solo se puede usar el '+' como es comun, para concatenar
print("Hello" + " Friend") 
# De igual manera no podemos mezclar tipos de datos en una concatenacion, en dado caso deberemos usar funciones
# del sistema que nos permitan cambiar el tipo de dato para la correcta operacion. 
print("Hello " + "Friend " + str(5))
# Pero si podemos multiplicar una palabra. 
print(" Hello Friend " * 5) 

# Operadores comparativos 

print(5 <= 4)
print(5 >= 4)
print(5 < 4)
print(5 > 4)
print(5 == 4)
print(5 != 4)

# Como dato extra, tomemos en cuenta que al momento de hacer operaciones comparativas en 
# algun String, lo que hara es una comparacion ALFABETICA x ASCII.

print("Hola" <= "Aquel")
print("Hola" >= "Odin")
print("Hola" == "Loki")
print("Holas" != "Thor")

# Operadores Logicos

