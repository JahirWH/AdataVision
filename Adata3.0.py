import tkinter as tk
from tkinter import ttk, messagebox
import os
from Adata3_0 import inicio_sesion, menu, VerInventario, ProductoNuevo, ModificarProducto, BuscarPorNombre, clearConsole

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AdataVision - Gestor de Contraseñas")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Estilo
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TLabel', font=('Arial', 10), background='#f0f0f0')
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Pantalla de inicio de sesión
        self.show_login_screen()
    
    def show_login_screen(self):
        # Limpiar frame actual
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Título
        ttk.Label(self.main_frame, text="Inicio de Sesión", style='Header.TLabel').pack(pady=20)
        
        # Formulario de inicio de sesión
        login_frame = ttk.Frame(self.main_frame)
        login_frame.pack(pady=20)
        
        ttk.Label(login_frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.username_entry = ttk.Entry(login_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(login_frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.password_entry = ttk.Entry(login_frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Iniciar Sesión", command=self.login).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Enfocar el campo de usuario
        self.username_entry.focus()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña")
            return
        
        # Aquí deberías implementar la lógica de autenticación
        # Por ahora, asumimos que el login es exitoso
        self.show_main_menu()
    
    def show_main_menu(self):
        # Limpiar frame actual
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Título
        ttk.Label(self.main_frame, text="Menú Principal", style='Header.TLabel').pack(pady=20)
        
        # Botones del menú
        menu_frame = ttk.Frame(self.main_frame)
        menu_frame.pack(pady=20)
        
        ttk.Button(menu_frame, text="1. Ver Contraseñas", 
                  command=self.show_passwords, width=30).pack(pady=5)
        ttk.Button(menu_frame, text="2. Agregar Nueva Contraseña", 
                  command=self.add_password, width=30).pack(pady=5)
        ttk.Button(menu_frame, text="3. Modificar Contraseña", 
                  command=self.modify_password, width=30).pack(pady=5)
        ttk.Button(menu_frame, text="4. Buscar Contraseña", 
                  command=self.search_password, width=30).pack(pady=5)
        ttk.Button(menu_frame, text="5. Cerrar Sesión", 
                  command=self.show_login_screen, width=30).pack(pady=20)
    
    def show_passwords(self):
        # Aquí deberías implementar la lógica para mostrar las contraseñas
        messagebox.showinfo("Información", "Mostrando todas las contraseñas...")
        # Ejemplo: VerInventario()
    
    def add_password(self):
        # Aquí deberías implementar la lógica para agregar una nueva contraseña
        messagebox.showinfo("Información", "Agregando nueva contraseña...")
        # Ejemplo: ProductoNuevo()
    
    def modify_password(self):
        # Aquí deberías implementar la lógica para modificar una contraseña
        messagebox.showinfo("Información", "Modificando contraseña...")
        # Ejemplo: ModificarProducto()
    
    def search_password(self):
        # Aquí deberías implementar la lógica para buscar una contraseña
        messagebox.showinfo("Información", "Buscando contraseña...")
        # Ejemplo: BuscarPorNombre()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()import os
import sys 
import csv
import getpass
import random 
import polars as pl
from random import choice
from datetime import date
from datetime import datetime
from cryptography.fernet import Fernet
from colorama import init,Fore,Back,Style
from time import sleep
import os.path as path
import time
import bcrypt
import base64
import hashlib


init()                         
                          

today = str(date.today())
time_tiempo = 6.2

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 80))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
        sleep(0.01)
        loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)


def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)


print(' ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ ')
print(' ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗')
print(' ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║')
print(' ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║')
print(' ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝')
print(' ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ')




def show():

                clearConsole()
                print("███╗░░░███╗██╗░░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗")
                print("████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝")
                print("██╔████╔██║░╚████╔╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░")
                print("██║╚██╔╝██║░░╚██╔╝░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░")
                print("██║░╚═╝░██║░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗")
                print("╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝")
                inicio_sesion()
                archivo_estado()


#Problema de logica al hacer un bucle de desincryptacion

password = input("Introduce tu Usuario : ")
secreto = password


def validate():
        
        if not password.isalpha() or len(password) > 6:
            clearConsole()
            time.sleep(1)
            clearConsole()
            print(Fore.RED + "Error: Si introduces un usuario incorrecto no podras desencryptar ." + Fore.RESET)
            time.sleep(3)
            return None
                    
        elif password =="exit" or password == "salir":
            print("saliendo....")
            estado_salida()
            sys.exit(0)
            
                    #error=="Generado"
            

            

def inicio_sesion():
        let = open('date.txt', 'r')
        ver=let.read()
        print('Ultima modificacion  : '+ Fore.GREEN + ver +Style.RESET_ALL)
        tem = open('temp.txt','r')
        ver=tem.read()
        print('Contrasena temporal  : '+ Fore.BLUE + Style.BRIGHT+ver+Style.RESET_ALL)


def archivo_estado():
        abrir = open('estado.txt', 'r')
        a = abrir.read()
        if a == 'encrypted':
            print("Estado del archivo: "+Fore.GREEN + a + Fore.RESET )
        elif a == 'decrypted':
             print("Estado del archivo: "+Fore.RED + a + Fore.RESET )

def actualizacion_sesion():

    today = str(date.today())
    hora_actual = str(datetime.now())

    archivo_estado = open("date.txt", "w")
    archivo_estado.write(hora_actual)
    archivo_estado.close()



def Generate_pas():
    longitud = input("¿De cuántos dígitos quieres las contraseñas?: ").strip()
    
    if not longitud.isdigit():
        print(Fore.RED + "⚠️ Ingresa solo números." + Fore.RESET)
        return
    longitud = int(longitud)

    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    print(Fore.GREEN + "\nContraseñas generadas:" + Fore.RESET)
    contrasenas = []

    for _ in range(2):
        p = ''.join([choice(valores) for _ in range(longitud)])
        contrasenas.append(p)
        print(Fore.CYAN + Style.BRIGHT + p + Style.RESET_ALL)

    # Guarda la última contraseña generada en temp.txt
    with open('temp.txt', 'w') as lee:
        lee.write(contrasenas[-1])



def Eliminacion():
    os.remove("Inventario.csv")
    print(Fore.RED+"Archivo eliminado"+Fore.RESET)
    validate()
#encryptacion automatica al cerrar el programa

def estado_key():
    #Convercion al leer el estado solo validacion, no agrega o modifica el estado
    le = open('estado.txt')
    estado=le.read()
    if estado =="encrypted":
        print("archivo ya esta encryptado!!! ")
        #validate()
    elif estado== "decrypted":
        encrypted_with_key()
        return
    else: 
        print("Error en algo") 

    #generar un archivo extra donde diga si el archivo esta encryptado si lo esta no no encryptara dos veces
def estado():
    try:
        with open('estado.txt', "r") as le:
            estado = le.read().strip()

        if estado == "encrypted":
            print("Archivo ya está encriptado!!!")
        elif estado == "decrypted":
            encrypted()  # Asegúrate de que la función encrypted() está definida
        else:
            print("Error: Estado desconocido.")

    except FileNotFoundError:
        print("Error: El archivo 'estado.txt' no existe.")

def estado_salida():
    try:
        with open('estado.txt', "r") as les:
            estado_salir = les.read().strip()

        if estado_salir == "decrypted":
            encrypted()
    except FileNotFoundError:
        print("Error: No se encontró 'estado.txt'.")



def estado_dos():
    #Verificacion de desencryptacion
    leer = open('estado.txt','r')
    estado=leer.read()
    if estado =="decrypted":
        print(Fore.RED+"No se puede desencryptar el archivo, el archivo ya se encuentra desencrytado"+Fore.RESET)
        return
    elif estado== "encrypted":
        decrypted()
    else: 
        print("Error en algo") 


def actualizacion_estado():
    archivo_estado = open("estado.txt", "w")
    archivo_estado.write("encrypted")
    archivo_estado.close()

def actualizacion_estado_dos():
    archivo_estado = open("estado.txt", "w")
    archivo_estado.write("decrypted")
    archivo_estado.close()

def genera_clave():
                    print("Desea generar una nueva contraseña y usuario: ")
                    save=input("Y/N :")
                    if save== 'Y' or save== 'y':
                        secreto = input('Tu usuario de maximo 6 letras: ')  # Puede ser cualquier identificador único
                        identificador = input('Clave de maximo 6 numeros: ') 
                         # Usa el nombre de usuario del sistema
# Validar usuario (solo letras y máximo 6 caracteres)
                        if not secreto.isalpha() or len(secreto) > 6:
                            print(Fore.RED + "Error: Debes ingresar un máximo de 6 letras." + Fore.RESET)
                            return
                        if not identificador.isdigit() or len(identificador) > 6:
                            print(Fore.RED + "Error: Debes ingresar un máximo de 6 dígitos." + Fore.RESET)
                            return
                        clave_base = secreto + identificador  
    # Crear un hash SHA256 de la clave base
                        clave_hash = hashlib.sha256(clave_base.encode()).digest()
                        clave_final = base64.urlsafe_b64encode(clave_hash[:32])
                        print(Fore.RED+"La nueva clave de encryptacion es \n"+Fore.RESET)
                        print("Clave generada:", clave_final.decode())
                        time.sleep(4)
                        clearConsole()
                        print("El usuario y clave se guardaran en : clave.txt")
                        time.sleep(2)
                        clearConsole()
                        with open('clave.txt', 'wb') as archivo:
                            archivo.write(f"Usuario: {secreto}:password:{identificador}\n".encode())  # Separar usuario y clave   
                            archivo.close()                    
                        print(Fore.BLUE+"La clave se a guardado con exito"+Fore.RESET)
                        time.sleep(2)
                        print("Desea encryptar el archivo ahora con las nuevas claves:")
                        da = input("Y/N :")
                        if da == "Y" or da == "y":
                            le = open('estado.txt',"r",)
                            estado=le.read()

                            if estado =="encrypted":
                                print("Primero desencrypte el archivo!!! ")
                                return
                            #validate()
                            elif estado== "decrypted":
                                archivo =open('Inventario.csv','rb')
                                datos = archivo.read()
                                f = Fernet(clave_final)
                                datos_cifrados = f.encrypt(datos)
                                encrypted_file= open('Inventario.csv', 'wb') 
                                encrypted_file.write(datos_cifrados)
                                print(Fore.RED+"El archivo se encrypto con exito"+Fore.RESET)
                                actualizacion_estado()
                        else:
                            print("SALIENDO...")
                            time.sleep(1)
                            return

                    else:
                        print("SALIENDO...")

        #Elecion si quiero que se desencrypte con llave interna o externa

# def encrypted_with_key():
#     identificador = input('Usurio maximo 4 letras o num :')  # Usa el nombre de usuario del sistema
#     clave_base = secreto + identificador  
#     # Crear un hash SHA256 de la clave base
#     clave_hash = hashlib.sha256(clave_base.encode()).digest()
#     # Tomar los primeros 32 bytes y codificarlos en base64 para Fernet
#     clave_final = base64.urlsafe_b64encode(clave_hash[:32])
#     # Mostrar la clave generada
#     print("Clave generada:", clave_final.decode())
#     archivo =open('Inventario.csv','rb')
#     datos = archivo.read()
#     f = Fernet(clave_final)
#     datos_cifrados = f.encrypt(datos)
#     encrypted_file= open('Inventario.csv', 'wb') 
#     encrypted_file.write(datos_cifrados)
#     print(Fore.RED+"El archivo se encrypto con exito"+Fore.RESET)
#     actualizacion_estado()


def encrypted():
    
        identificador = input(Fore.BLUE + "Crea clave numérica de máximo 6 dígitos: " + Fore.RESET)

        if not identificador.isdigit() or len(identificador) > 6:
            print(Fore.RED + "Error: La clave debe contener solo números y un máximo de 6 dígitos." + Fore.RESET)
            return

        clave_base = secreto + identificador  

    # Crear un hash SHA256 de la clave base
        clave_hash = hashlib.sha256(clave_base.encode()).digest()

    # Tomar los primeros 32 bytes y codificarlos en base64 para Fernet
        clave_final = base64.urlsafe_b64encode(clave_hash[:32])

    # Mostrar la clave generada
        print("Clave generada:", clave_final.decode())

        archivo =open('Inventario.csv','rb')
        datos = archivo.read()
   
        fernet = Fernet(clave_final)     
        file=open('Inventario.csv', 'rb') 
        original = file.read() 

        encrypted = fernet.encrypt(original) 

        file=open('Inventario.csv', 'rb') 
        original = file.read()


        encrypted_file= open('Inventario.csv', 'wb') 
        encrypted_file.write(encrypted)

        actualizacion_estado()
        # print(Fore.RED+"archivo encryptado "+Fore.RESET)
        print(Fore.BLUE + Style.BRIGHT+"Archivo encryptado con exito!"+Style.RESET_ALL)


        # identificador = input("Ingresa tu consetrasena para desencriptar: ")
        if secreto is None :
            print(Fore.RED + "No se ingresó una clave válida." + Fore.RESET)
            return

        
#desencrptacion automatica al introducior la contraseña correcta


    #return
def decrypted():
        key = secreto
        identificador = input(Fore.GREEN + 'Ingresa los dígitos numéricos para desencriptar: ' + Fore.RESET)

        if not identificador.isdigit() or len(identificador) > 6:
            print(Fore.RED + "Error: Debes ingresar máximo 6 dígitos numéricos." + Fore.RESET)
            return
    
        clave_base = key + identificador  

        clave_hash = hashlib.sha256(clave_base.encode()).digest()
        clave_final = base64.urlsafe_b64encode(clave_hash[:32])
        try:
        # Leer archivo y desencriptar
            with open('Inventario.csv', 'rb') as archivo:
                datos_cifrados = archivo.read()
        
                f = Fernet(clave_final)
                datos_descifrados = f.decrypt(datos_cifrados)

            with open('Inventario.csv', 'wb') as archivo:
                 archivo.write(datos_descifrados)

            actualizacion_estado_dos()
            time.sleep(0.5)
            print(Fore.GREEN + "El archivo se desencriptó con éxito" + Fore.RESET)
            return identificador  # Retorna el identificador si es necesario
    
        except Exception as e:
            print("┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐   ┬┌┐┌┌─┐┌─┐┬─┐┬─┐┌─┐┌─┐┌┬┐")  
            print("├─┘├─┤└─┐└─┐││││ │├┬┘ ││   │││││  │ │├┬┘├┬┘├┤ │   │ ")  
            print("┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘   ┴┘└┘└─┘└─┘┴└─┴└─└─┘└─┘ ┴ ")
            time.sleep(1)
            print(Fore.RED + "Error: No se pudo desencriptar el archivo. ¿Ingresaste los números correctos?" + Fore.RESET)

  # Obtener el identificador desde decrypted

    # Crear un hash SHA256 y codificarlo para Fernet

 


# def decrypted_key():

  
    
#     identificador = input('Crea Usuario :  ')

#     if not identificador.isdigit() or len(identificador) != 6:
#         print(Fore.RED + "Error: Debes ingresar maximo 6 dígitos." + Fore.RESET)
#         return

#     clave_base = secreto + identificador  

#     # Crear un hash SHA256 y codificarlo para Fernet
#     clave_hash = hashlib.sha256(clave_base.encode()).digest()
#     clave_final = base64.urlsafe_b64encode(clave_hash[:32])

#     try:
#         # Leer archivo y desencriptar
#         with open('Inventario.csv', 'rb') as archivo:
#             datos_cifrados = archivo.read()
        
#         f = Fernet(clave_final)
#         datos_descifrados = f.decrypt(datos_cifrados)

#         with open('Inventario.csv', 'wb') as archivo:
#             archivo.write(datos_descifrados)

#         print(Fore.GREEN + "El archivo se desencriptó con éxito" + Fore.RESET)
    
#     except Exception as e:
#         print(Fore.RED + "Error: No se pudo desencriptar el archivo. ¿Ingresaste los números correctos?" + Fore.RESET)


def menu():

    #print("******MENU INVENTARIO******")
    print("1--- Ver   ","                   2--- Agregar " )
    print("3--- Modificar ","               4--- Buscar")
    print("5--- Encryptar      ","          6--- Desencryptar")
    print("7--- Generar password","         8--- Genera nuevas claves")
    print(Fore.RED+"eliminartodo"+Fore.RESET)



    option=input("Introduzca el número de la opción deseada: ")
    return option


    
def Existename(service):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(service==row['service']):
                return row
        return "No existe name"



def VerInventario():
    try:
        df_csv = pl.read_csv("Inventario.csv")
        
        if df_csv.is_empty():
            print(Fore.YELLOW + "El inventario está vacío o encryptado" + Fore.RESET)
            return
        
        print(Fore.CYAN + "📦 Inventario Actual 📦" + Fore.RESET)
        pl.Config.set_tbl_rows(70)  # Ajusta el límite de filas visibles a 100
        print(df_csv)

    except FileNotFoundError:
        print(Fore.RED + "Error: No se encontró 'Inventario.csv'." + Fore.RESET)
    except pl.exceptions.NoDataError:
        print(Fore.YELLOW + "El archivo está vacío" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}" + Fore.RESET)
   


def ProductoNuevo():
    try:
        with open('estado.txt', 'r') as ver:
            var = ver.read().strip()  # Eliminar espacios en blanco

        if var == 'encrypted':
            print(Fore.RED + "Primero debe desencriptar el archivo!!" + Fore.RESET)
            return

        from random import randint
        codigo = ''.join(str(randint(0, 9)) for _ in range(4))  # Código de 4 dígitos aleatorios
        
        if ExisteCodigo(codigo) != "No existe":
            print(Fore.RED + "Error: el código ya existe." + Fore.RESET)
            return

        ubicacion = input('Servicio: ').strip()
        descripcion = input('Email: ').strip()
        unidad = input('Password: ').strip()
        tipo = input('Usuario: ').strip()
        familia = input('Referencia: ').strip()
        fecha = str(date.today())

        # Verificar que todos los campos tengan datos
        if not all([ubicacion, descripcion, unidad, tipo, familia]):
            print(Fore.RED + "Error: No puedes dejar campos vacíos." + Fore.RESET)
            return

        with open('Inventario.csv', 'a') as file:
            file.write(f'\n{codigo},{ubicacion},{descripcion},{unidad},{tipo},{familia},{fecha}')
        
        print(Fore.GREEN + "Se agregó correctamente." + Fore.RESET)

    except FileNotFoundError:
        print(Fore.RED + "Error: No se encontró 'estado.txt'." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}" + Fore.RESET)


def ModificarProducto():
    if not os.path.exists('estado.txt'):
        print(Fore.RED + "Error: No se encontró el archivo de estado." + Fore.RESET)
        return

    with open('estado.txt', 'r') as f:
        var = f.read().strip()

    if var == 'encrypted':
        print(Fore.RED + "Primero debe desencriptar el archivo!!" + Fore.RESET)
        return

    service = input('Ingrese el servicio a modificar: ').strip()

    if Existename(service) == "No existe":  
        print(Fore.RED + "Error: El servicio no existe en el inventario." + Fore.RESET)
        return

    df = pl.read_csv('Inventario.csv')

    # Mostrar todos los servicios coincidentes
    ds = df.filter(pl.col("service").str.contains(service))
    print(Fore.YELLOW + "El servicio actual contiene: " + Fore.RESET)
    print(ds)

    codigo = input("Ingrese el código a modificar (deje en blanco para cancelar): ").strip()
    if not codigo:
        print(Fore.YELLOW + "Modificación cancelada." + Fore.RESET)
        return

    # Obtener datos actuales del código
    # dr = df.filter(pl.col("codigo") == codigo)
   # Asegúrate de convertir a texto el código
    dr = df.filter(pl.col("codigo").cast(pl.Utf8) == codigo)
    if dr.is_empty():
        print(Fore.RED + "Código no encontrado en el inventario." + Fore.RESET)
        return

    current_data = dr.row(0, named=True)


    # Mostrar valores actuales y permitir dejar en blanco para conservarlos
    print(Fore.CYAN + "\nDeje en blanco para mantener el valor actual:" + Fore.RESET)

    ubicacion = input(f'Servicio [{current_data["service"]}]: ').strip() or current_data["service"]
    descripcion = input(f'Email [{current_data["email"]}]: ').strip() or current_data["email"]
    unidad = input(f'Contraseña [{current_data["password"]}]: ').strip() or current_data["password"]
    tipo = input(f'Usuario [{current_data["username"]}]: ').strip() or current_data["username"]
    familia = input(f'Ref [{current_data["web"]}]: ').strip() or current_data["web"]
    fecha = today


    modificarBDD(codigo, ubicacion, descripcion, unidad, tipo, familia, fecha)


def modificarBDD(codigo, ubicacion, descripcion, unidad, tipo, familia, fecha):
    result = []


    with open('Inventario.csv', newline='') as File:
        reader = csv.DictReader(File)
        for row in reader:
            # Compara como string para evitar errores de tipo
            if row['codigo'].strip() == str(codigo).strip():
                row['service'] = ubicacion
                row['email'] = descripcion
                row['password'] = unidad
                row['username'] = tipo
                row['web'] = familia
                row['fecha'] = fecha
            result.append(row)

    # Escribir el nuevo CSV
    with open('Inventario.csv', 'w', newline='') as File:
        fieldnames = ['codigo', 'service', 'email', 'password', 'username', 'web', 'fecha']
        writer = csv.DictWriter(File, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)
        # print("Resultado final para guardar:")
        # for r in result:
        #     print(r)
    
    actualizacion_sesion()
    print(Fore.GREEN + f"✅ Servicio '{ubicacion}' actualizado correctamente." + Fore.RESET)


def ExisteCodigo(codigo):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(codigo==row['codigo']):
                return row
        return "No existe"


def BuscarPorNombre():
    ver= open('estado.txt','r')
    var=ver.read()
    

    if var == 'encrypted':
        print(Fore.RED+"Primero debe desencriptar el archivo!!"+Fore.RESET)
    else:

        df=pl.read_csv('Inventario.csv')
        palabra=str(input('Ingrese el nombre a buscar: '))
        print(Fore.YELLOW+"Servicios con la palabra  "+Fore.RESET+ (palabra))
        print(df.filter(df['service'].str.contains(palabra)))
        #print(Fore.YELLOW+"Emails con la palabra  "+Fore.RESET+ (palabra))
        print(df.filter(df['email'].str.contains(palabra)))
        #print(Fore.YELLOW+"Usuarios con la palabra  "+Fore.RESET+ (palabra))
        print(df.filter(df['username'].str.contains(palabra)))
        #print(Fore.YELLOW+"webs con la palabra   "+Fore.RESET+ (palabra))
        print(df.filter(df['web'].str.contains(palabra)))
       

def pausa():
    input("\nPresiona Enter para continuar...")
#soluconar logica para encryptarb sin que se vuelva un bucle

def main():

    validate()
    while True:
        show()
        option=menu()
        if option == '1':
            VerInventario()
            pausa()
        elif option == '2':
            ProductoNuevo()
            pausa()
        elif option == '3':
            ModificarProducto()
            pausa()
        elif option == '4':
            BuscarPorNombre()
            pausa()
        elif option == '5':
            estado()

            pausa()
        elif option == '6':
            estado_dos()
            pausa()
        elif option == '7':
            Generate_pas()
            pausa()
        elif option == '8':
            genera_clave()
            pausa()
        # elif option == '9':
        #     decrypted_key()
        #     pausa()
        elif option == 'eliminartodo':
            Eliminacion()
            pausa()
        # elif option == '10':
        #     estado_key()
        #     pausa()
        elif option == 'exit' or 'salir':
            estado_salida()
            clearConsole()
            print(Fore.GREEN + "Revisando ..."+ Fore.RESET)
            time.sleep(1)
    
            clearConsole()
            print(Fore.GREEN + "SALIENDO....!" + Fore.RESET)
            break
        else:
            print('opcion invalida')
     
main()


