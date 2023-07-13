"""
    Escribir una función que dada una cadena de caracteres, devuelva:
        a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
        devolver 'USB'.
        b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
        'república argentina' debe devolver 'República Argentina'.
        c) Las palabras que comiencen con la letra 'A'. Por ejemplo, si recibe 'Antes de ayer'
        debe devolver 'Antes ayer'
"""


def primer_letra_cada_palabra(palabra):

    longitud = len(palabra)
    palabra = palabra.title()
    
    print(palabra)

    for i in range(longitud):

        if (palabra[i]>='A' and palabra[i]<='Z'):
            print(palabra[i],end="")

    print()

# primer_letra_cada_palabra("universal serial bus")
# primer_letra_cada_palabra("disney plus")
# primer_letra_cada_palabra("Organizacion mundial de la Salud")


def primer_letra_cada_palabra_mayuscula(palabra):

    print(palabra.title())


# primer_letra_cada_palabra_mayuscula("hola mundo")
# primer_letra_cada_palabra_mayuscula("la concha de tu madre")



def palabras_comienzan_con_a(texto):

    lista_texto = texto.split()
    longitud = len(lista_texto)
    print(texto)

    for i in range(longitud):

        if (lista_texto[i][0]=='A' or lista_texto[i][0]=='a'):
            print(lista_texto[i],end=" ")
    print()

palabras_comienzan_con_a("Antes de ayer")
palabras_comienzan_con_a("Amanecer en la puerta de tu amada mujer Antonella")