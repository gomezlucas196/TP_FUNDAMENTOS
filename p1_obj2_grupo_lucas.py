def cifrar_atbash(mensaje):
    #Funcion que recibe un mensaje y lo retorna encriptado en codigo atbash (da vuelta el abecedario)
    #AUTOR: Lucas Gomez
    """
    >>> cifrar_atbash("HOLA MUNDO")
    'SLOZ NFMWL'
    >>> cifrar_atbash("abcXYZ")
    'zyxCBA'
    >>> cifrar_atbash("123")
    '876'
    >>> cifrar_atbash("Z9")
    'A0'
    >>> cifrar_atbash("Hola123")
    'Sloz876'
    >>> cifrar_atbash("Python")
    'Kbgslm'
    >>> cifrar_atbash("Fundamentos")
    'Ufmwznvmglh'
    >>> cifrar_atbash("Atbash")
    'Zgyzhs'
    >>> cifrar_atbash("CIFRADO CESAR")
    'XRUIZWL XVHZI'
    >>> cifrar_atbash("123abcXYZ!@#")
    '876zyxCBA!@#'
    """
    resultado = ""
    for c in mensaje:
        if 'A' <= c <= 'Z':
            resultado += chr(ord('Z') - (ord(c) - ord('A')))
        elif 'a' <= c <= 'z':
            resultado += chr(ord('z') - (ord(c) - ord('a')))
        elif '0' <= c <= '9':
            resultado += chr(ord('9') - (ord(c) - ord('0')))
        else:
            resultado += c
    return resultado


def main():
    import doctest
    print(doctest.testmod())


main()
