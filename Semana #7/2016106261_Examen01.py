'''

Examen I de Introducción a la programación
Estudiante: José Carlos Montoya Pichardo
Carné: 2016106261

'''

# =========================Función sumatoria_pares=============================
'''

Esta función permite sumar los números que se encuentran dentro de un rango
definido, basado en su valor par o impar.
Entradas: Números enteros y positivos. Además de un booleano que determina
si se trabaja con pares o impares.
Salida: Sumatoria de los números definidos.
Limitaciones: No se puede utilizar datos de valor flotante o cadena de texto.

'''


# Sumatoria para valor de verdad True
def funcion_pares(inicio, final):
    '''

    Se realiza la sumatoria utilizando solamente los números pares que se
    encuentran dentro del rango definido.

    '''
    if inicio > final:
        return 0
    else:
        pares = inicio % 2
        if pares == 0:
            return inicio + funcion_pares(inicio + 2, final)
        else:
            return funcion_pares(inicio + 1, final)


# Sumatoria para valor de verdad False
def funcion_impares(inicio, final):
    '''

    Se realiza la sumatoria utilizando solamente los números impares que se
    encuentran dentro del rango definido.

    '''
    if inicio > final:
        return 0
    else:
        impar = inicio % 2
        if impar == 0:
            return funcion_impares(inicio + 1, final)
        else:
            return inicio + funcion_impares(inicio + 2, final)


# Decisión basada en valor de verdad
def funcion_sumatoriaaux(inicio, final, pares):
    '''

    El valor de verdad de pares determina la función a utilizar para terminar
    el proceso solicitado.

    '''
    if pares == True:
        return funcion_pares(inicio, final)
    else:
        return funcion_impares(inicio, final)


# Validación de argumentos
def sumatoria_pares(inicio, final, pares):
    '''

    Se comprueba que inicio y final sean argumentos positivos y enteros, que
    inicio sea menor a final y que pares tenga valor booleano.

    '''
    if type(inicio) == int and type(final) == int:
        if inicio < 0 or final < 0:
            return "Error02"
        else:
            if inicio > final:
                return "Error02"
            else:
                if pares == True or pares == False:
                    return funcion_sumatoriaaux(inicio, final, pares)
                else:
                    return "Error03"
    else:
        return "Error01"


# Ejecución inicial
sumatoria_pares(inicio, final, pares)
# =============================================================================

# ===========================Función quita_ceros===============================
'''

Esta función permite remover los ceros adicionales de los números dados.
Entradas: Números enteros y positivos, de al menos 6 digitos.
Salida: Un número de 6 digitos que no contiene ceros.
Limitaciones: No se puede utilizar datos de valor flotante o cadena de texto.
Además, los números de entrada deben ser de 6 digitos o más.

'''


# Eliminación de ceros y composición del nuevo número
def funcion_nozero(numero, potencia):
    '''

    Se compone un nuevo número, basado en el número de entrada, que no contiene
    ceros para ser retornado para su valoración.

    '''
    if numero == 0:
        return 0
    else:
        lastdigit = numero % 10
        if lastdigit == 0:
            return funcion_nozero(numero // 10, potencia)
        else:
            return lastdigit * (10 ** potencia) + funcion_nozero(numero // 10,
                                                                 potencia + 1)


# Validación del nuevo número (sin ceros)
def funcion_digiseis(numero):
    '''

    Se cuenta la cantidad de dígitos del nuevo número formado. Para ello, antes
    se debe obtener ese número mediante el llamado a funcion_nozero(argumento)

    '''
    digitos = funcion_nozero(numero, 0)
    if digitos < 100000:
        return "Error03"
    else:
        return digitos


# Validación de argumentos
def quita_ceros(numero):
    '''

    Se comprueba que numero sea un número entero positivo y entero, de al menos
    6 digitos.

    '''
    if type(numero) == int:
        if numero == 0:
            return "Error03"
        elif numero > 99999:
            return funcion_digiseis(numero)
        else:
            '''

            Se acordó este error al inicio del examen, sin embargo el ejemplo
            muestra "Error03"

            '''
            return "Error02"
    else:
        return "Error01"


# Ejecución inicial
'''

Si los números comienzan con 0, se trata de un octal, lo cual muestra error
al ejecutar.

'''
quita_ceros(numero)
# =============================================================================

# ===========================Función palindromo================================
'''

Esta función valora si un número posee propiedad de palindromo.
Entradas: Números enteros y positivos.
Salida: Un valor de verdad (True para palindromo, False para no palindromo)
Limitaciones: No se puede utilizar datos de valor flotante o cadena de texto.
Los números deben ser naturales incluyendo 0.

'''


# Función que retorna la cantidad de digitos de un número
def cuentadigitos(numero):
    '''

    Se cuentan los digitos de un número mediante división entera

    '''
    if numero == 0:
        return 0
    else:
        return 1 + cuentadigitos(numero // 10)


#  Recomponer el número
def palindromo_final(numero, potencia):
    '''

    Se recompone el número utilizando operaciones de base 10.

    '''
    if numero == 0:
        return 0
    else:
        lastdigit = numero % 10
        return lastdigit * (10 ** potencia) + palindromo_final(numero // 10,
                                                             potencia - 1)


# Se comprueba la existencia del palindromo
def palindromoaux(numero):
    '''

    Se compara al nuevo número con el número original. Esto devuelve un valor
    de verdad

    '''
    potencia = cuentadigitos(numero) - 1
    nuevonum = palindromo_final(numero, potencia)
    if nuevonum == numero:
        return True
    else:
        return False


# Validación de argumentos
def palindromo(numero):
    '''

    Se comprueba que número sea un número entero positivo

    '''
    if type(numero) == int:
        if numero < 0:
            return "Error01"
        elif numero == 0:
            return True
        else:
            return palindromoaux(numero)
    else:
        return "Error01"


# Ejecución inicial
palindromo(numero)
# =============================================================================

# =========================Modificación de código==============================
'''

Esta función devuelve el valor del digito que se encuentra en una posición
determinada
Entradas: Números enteros y positivos.
Salida: Número que representa al digito de la posición señalada
Limitaciones: No se puede utilizar datos de valor flotante o cadena de texto.
La posición debe ser menor a la cantidad de digitos de un número, comenzando a
contar desde 0, derecha a izquierda

'''


# Función que retorna la cantidad de digitos de un número
def cuentadigitos2(numero):
    '''

    Se cuentan los digitos de un número mediante división entera

    '''
    if numero == 0:
        return 0
    else:
        return 1 + cuentadigitos2(numero // 10)


# Descomposición y retorno
def retornardigitoaux(posicion, numero):
    '''

    Se descompone el número original hasta obtener el valor del digito señalado
    por el usuario (posicion)

    '''
    if posicion == 0:
        return numero % 10
    else:
        return retornardigitoaux(posicion - 1, numero // 10)


# Valoración de argumentos
def retornardigito(posicion, numero):
    '''

    Se valida que los argumentos sean números enteros y positivos. Además,
    posicion debe ser menor a la cantidad retornada por cuentadigitos2.

    '''
    if type(posicion) != int or type(numero) != int:
        return "No son números enteros"
    elif posicion > cuentadigitos2(numero):
        return "La posición no existe en el número"
    else:
        return retornardigitoaux(posicion, numero)


# Ejecución inicial
retornardigito(posicion, numero)
# =============================================================================