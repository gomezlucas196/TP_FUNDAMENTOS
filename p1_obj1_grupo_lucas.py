def cifrar_cesar(mensaje, clave):
    #Esta funcion recibe un mensaje y una clave(Que sirve para encripto cesar) 
    #y retorna el mismo mensaje pero encriptado en cesar! cada letra segun su orden del
    #abecedario se le suman las posiciones indicadas AUTOR: Lucas Gomez
    """
    >>> cifrar_cesar("HOLA MUNDO 123", 3)
    'KROD PXQGR 456'
    >>> cifrar_cesar("Z9", 1)
    'A0'
    >>> cifrar_cesar("abcxyz", 4)
    'efgbcd'
    >>> cifrar_cesar("Hola123", 7)
    'Ovsh890'
    >>> cifrar_cesar("HOLA", 3)
    'KROD'
    >>> cifrar_cesar("hola mundo", 5)
    'mtqf rzsit'
    >>> cifrar_cesar("Zorro123", 2)
    'Bqttq345'
    >>> cifrar_cesar("Cesar#2025", 4)
    'Giwev#6469'
    >>> cifrar_cesar("Python", 10)
    'Zidryx'
    >>> cifrar_cesar("ABC xyz 789", 4)
    'EFG bcd 123'
    """
    resultado = ""
    for caracter in mensaje:
        if 'A' <= caracter <= 'Z':
            resultado += chr((ord(caracter) - ord('A') + clave) % 26 + ord('A'))
        elif 'a' <= caracter <= 'z':
            resultado += chr((ord(caracter) - ord('a') + clave) % 26 + ord('a'))
        elif '0' <= caracter <= '9':
            resultado += chr((ord(caracter) - ord('0') + clave) % 10 + ord('0'))
        else:
            resultado += caracter
    return resultado

def main():
    import doctest
    print(doctest.testmod())
main()