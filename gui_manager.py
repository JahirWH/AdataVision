import tkinter as tk
from tkinter import ttk, messagebox
import os
import importlib.util
import sys

# Cargar el módulo con nombre que contiene puntos
spec = importlib.util.spec_from_file_location("adata_module", "Adata3.0.py")
adata_module = importlib.util.module_from_spec(spec)
sys.modules["adata_module"] = adata_module
spec.loader.exec_module(adata_module)

# Importar las funciones necesarias
inicio_sesion = adata_module.inicio_sesion
menu = adata_module.menu
VerInventario = adata_module.VerInventario
ProductoNuevo = adata_module.ProductoNuevo
ModificarProducto = adata_module.ModificarProducto
BuscarPorNombre = adata_module.BuscarPorNombre
clearConsole = adata_module.clearConsole

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
    root.mainloop()
