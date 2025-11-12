# lucas matias emanuel gomez
# legajo : 114103

from tkinter import *
from tkinter import messagebox

def cifrar_cesar(msj, clave):
    res = ""
    k = int(clave)
    for c in msj:
        if 'A' <= c <= 'Z':
            res += chr((ord(c) - 65 + k) % 26 + 65)
        elif 'a' <= c <= 'z':
            res += chr((ord(c) - 97 + k) % 26 + 97)
        elif '0' <= c <= '9':
            res += chr((ord(c) - 48 + k) % 10 + 48)
        else:
            res += c
    return res

def descifrar_cesar(msj, clave):
    """
    Descifra un mensaje cifrado con el método César.

    >>> descifrar_cesar("KROD PXQGR 456", 3)
    'HOLA MUNDO 123'
    >>> descifrar_cesar("A0", 1)
    'Z9'
    >>> descifrar_cesar("efgbcd", 4)
    'abcxyz'
    >>> descifrar_cesar("Ovsh890", 7)
    'Hola123'
    >>> descifrar_cesar("KROD", 3)
    'HOLA'
    >>> descifrar_cesar("mtqf rzsit", 5)
    'hola mundo'
    >>> descifrar_cesar("Bqttq345", 2)
    'Zorro123'
    >>> descifrar_cesar("Giwev#6469", 4)
    'Cesar#2025'
    >>> descifrar_cesar("Zidryx", 10)
    'Python'
    >>> descifrar_cesar("EFG bcd 123", 4)
    'ABC xyz 789'
    """
    return cifrar_cesar(msj, -int(clave))

def cifrar_atbash(mensaje):
    
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


def descifrar_atbash(mensaje):
    """
    >>> descifrar_atbash("SLOZ NFMWL")
    'HOLA MUNDO'
    >>> descifrar_atbash("zyxCBA")
    'abcXYZ'
    >>> descifrar_atbash("876")
    '123'
    >>> descifrar_atbash("A0")
    'Z9'
    >>> descifrar_atbash("Sloz876")
    'Hola123'
    >>> descifrar_atbash("Kbgslm")
    'Python'
    >>> descifrar_atbash("Ufmwznvmglh")
    'Fundamentos'
    >>> descifrar_atbash("Zgyzhs")
    'Atbash'
    >>> descifrar_atbash("XRUIZWL XVHZI")
    'CIFRADO CESAR'
    >>> descifrar_atbash("876zyxCBA!@#")
    '123abcXYZ!@#'
    """
    # Atbash es simétrico: cifrar = descifrar
    return cifrar_atbash(mensaje)

# INTERFAZ

def ventana_bienvenida():
    ven = Tk()
    ven.title("TP Grupal Parte 1 - Grupo: lucas")
    ven.geometry("480x240")
    ven.resizable(0,0)
    ven.config(bg="lightblue")

    Label(ven, text="Bienvenido a la aplicacion de mensajes secretos del grupo Lucas",
          bg="lightblue", font=("Arial", 11, "bold")).pack(pady=10)

    txt = ("Bienvenido a la aplicacion de mensajes secretos del grupo Lucas.\n"
           "Para continuar presione Continuar; de lo contrario cierre la ventana.")
    Label(ven, text=txt, bg="lightblue", wraplength=420, justify="left").pack(pady=8)

    Label(ven, text="Construida por:\nLucas Matias Emanuel Gomez",
          bg="lightblue", justify="left").pack(pady=8)

    Button(ven, text="Continuar", width=14, command=lambda: abrir_principal(ven)).pack(pady=4)
    Button(ven, text="Cerrar", width=14, command=ven.destroy).pack(pady=4)

    ven.mainloop()

def abrir_principal(ven_ant):
    ven_ant.destroy()

    ven = Tk()
    ven.title("Mensajes Secretos - Grupo Lucas")
    ven.geometry("520x330")
    ven.resizable(0,0)
    ven.config(bg="lightyellow")

    Label(ven, text="Ingrese el mensaje:", bg="lightyellow").grid(row=0, column=0, padx=10, pady=10, sticky="w")

    txt_msj = Text(ven, width=55, height=5)
    txt_msj.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

    Label(ven, text="Clave (solo para Cesar):", bg="lightyellow").grid(row=2, column=0, padx=10, pady=5, sticky="w")

    ent_clave = Entry(ven, width=6)
    ent_clave.grid(row=2, column=1, pady=5, sticky="w")

    txt_out = Text(ven, width=55, height=5, state="disabled")
    txt_out.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def mostrar(t):
        txt_out.config(state="normal")
        txt_out.delete("1.0", END)
        txt_out.insert("1.0", t)
        txt_out.config(state="disabled")

    def tomar_mensaje():
        return txt_msj.get("1.0", "end-1c")

    def tomar_clave():
        return ent_clave.get()

    def btn_cifrar_cesar():
        try:
            k = int(tomar_clave())
            mostrar(cifrar_cesar(tomar_mensaje(), k))
        except:
            messagebox.showerror("", "Ingrese una clave numerica valida")

    def btn_descifrar_cesar():
        try:
            k = int(tomar_clave())
            mostrar(descifrar_cesar(tomar_mensaje(), k))
        except:
            messagebox.showerror("", "Ingrese una clave numerica valida")

    def btn_cifrar_atbash():
        mostrar(cifrar_atbash(tomar_mensaje()))

    def btn_descifrar_atbash():
        mostrar(descifrar_atbash(tomar_mensaje()))

    Button(ven, text="Cifrar Cesar", width=16, command=btn_cifrar_cesar).grid(row=3, column=0, padx=5, pady=6)
    Button(ven, text="Descifrar Cesar", width=16, command=btn_descifrar_cesar).grid(row=3, column=1, padx=5, pady=6)
    Button(ven, text="Cifrar Atbash", width=16, command=btn_cifrar_atbash).grid(row=3, column=2, padx=5, pady=6)
    Button(ven, text="Descifrar Atbash", width=16, command=btn_descifrar_atbash).grid(row=3, column=3, padx=5, pady=6)

    ven.mainloop()

def main():
    import doctest
    ventana_bienvenida()
    print(doctest.testmod())

main()
