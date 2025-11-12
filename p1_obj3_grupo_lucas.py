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
    return cifrar_cesar(msj, -int(clave))

def cifrar_atbash(msj):
    res = ""
    for c in msj:
        if 'A' <= c <= 'Z':
            res += chr(122 - (ord(c) - 65))
        elif 'a' <= c <= 'z':
            res += chr(90 - (ord(c) - 97))
        elif '0' <= c <= '9':
            res += chr(57 - (ord(c) - 48))
        else:
            res += c
    return res

def descifrar_atbash(msj):
    return cifrar_atbash(msj)

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
    ventana_bienvenida()

main()
