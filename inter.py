import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import csv
import os
from datetime import datetime
from cryptography.fernet import Fernet
import base64
import hashlib

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AdataVision - Gestor de Contraseñas")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Configuración de estilos
        self.setup_styles()
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Mostrar pantalla de inicio de sesión
        self.show_login_screen()
    
    def setup_styles(self):
        """Configura los estilos de la aplicación"""
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TLabel', font=('Arial', 10), background='#f0f0f0')
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Title.TLabel', font=('Arial', 20, 'bold'), background='#f0f0f0')
    
    def clear_frame(self):
        """Limpia el frame principal"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Muestra la pantalla de inicio de sesión"""
        self.clear_frame()
        
        # Título
        ttk.Label(
            self.main_frame, 
            text="Inicio de Sesión", 
            style='Title.TLabel'
        ).pack(pady=20)
        
        # Frame del formulario
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(pady=20, padx=50, fill=tk.X)
        
        # Campo de usuario
        ttk.Label(form_frame, text="Usuario:").pack(anchor='w', pady=(10, 5))
        self.username_entry = ttk.Entry(form_frame, width=40)
        self.username_entry.pack(fill=tk.X, pady=5)
        
        # Campo de contraseña
        ttk.Label(form_frame, text="Contraseña:").pack(anchor='w', pady=(10, 5))
        self.password_entry = ttk.Entry(form_frame, width=40, show="*")
        self.password_entry.pack(fill=tk.X, pady=5)
        
        # Frame de botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(
            button_frame, 
            text="Iniciar Sesión", 
            command=self.login,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Salir", 
            command=self.root.quit,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        # Enfocar el campo de usuario
        self.username_entry.focus()
    
    def login(self):
        """Maneja el inicio de sesión"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña")
            return
        
        # Aquí iría la lógica de autenticación
        # Por ahora, simplemente mostramos el menú principal
        self.show_main_menu()
    
    def show_main_menu(self):
        """Muestra el menú principal"""
        self.clear_frame()
        
        # Título
        ttk.Label(
            self.main_frame, 
            text="Menú Principal", 
            style='Title.TLabel'
        ).pack(pady=20)
        
        # Frame de botones
        menu_frame = ttk.Frame(self.main_frame)
        menu_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        # Configuración de la cuadrícula
        menu_frame.columnconfigure(0, weight=1)
        menu_frame.columnconfigure(1, weight=1)
        
        # Botones del menú
        buttons = [
            ("Ver Contraseñas", self.show_passwords, 0, 0),
            ("Agregar Contraseña", self.add_password, 0, 1),
            ("Modificar Contraseña", self.modify_password, 1, 0),
            ("Buscar Contraseña", self.search_password, 1, 1),
            ("Generar Contraseña", self.generate_password, 2, 0),
            ("Cerrar Sesión", self.show_login_screen, 2, 1)
        ]
        
        for text, command, row, col in buttons:
            btn = ttk.Button(
                menu_frame, 
                text=text, 
                command=command,
                style='TButton',
                width=25
            )
            btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
    
    def show_passwords(self):
        """Muestra todas las contraseñas guardadas"""
        self.clear_frame()
        
        # Título y botón de regreso
        ttk.Label(
            self.main_frame, 
            text="Tus Contraseñas", 
            style='Title.TLabel'
        ).pack(pady=(0, 20))
        
        # Área de texto para mostrar las contraseñas
        text_area = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Arial', 10)
        )
        text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Botón de regreso
        ttk.Button(
            self.main_frame,
            text="Regresar al Menú",
            command=self.show_main_menu
        ).pack(pady=10)
        
        # Aquí iría la lógica para cargar y mostrar las contraseñas
        text_area.insert(tk.INSERT, "Aquí se mostrarán tus contraseñas guardadas.\n\n")
        text_area.insert(tk.INSERT, "Esta es una versión de demostración. En una versión completa, ")
        text_area.insert(tk.INSERT, "aquí se cargarían y mostrarían tus contraseñas de manera segura.")
        text_area.config(state=tk.DISABLED)
    
    def add_password(self):
        """Muestra el formulario para agregar una nueva contraseña"""
        self.clear_frame()
        
        # Título
        ttk.Label(
            self.main_frame, 
            text="Agregar Nueva Contraseña", 
            style='Title.TLabel'
        ).pack(pady=20)
        
        # Frame del formulario
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(pady=10, padx=50, fill=tk.X)
        
        # Campos del formulario
        fields = [
            ("Servicio:", "entry_service"),
            ("Usuario/Email:", "entry_username"),
            ("Contraseña:", "entry_password"),
            ("URL/Web:", "entry_url"),
            ("Notas:", "entry_notes")
        ]
        
        self.entries = {}
        
        for i, (label_text, entry_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky='w', pady=5, padx=5)
            entry = ttk.Entry(form_frame, width=50)
            entry.grid(row=i, column=1, sticky='ew', pady=5, padx=5)
            self.entries[entry_name] = entry
        
        # Hacer que la columna 1 se expanda
        form_frame.columnconfigure(1, weight=1)
        
        # Frame de botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(
            button_frame, 
            text="Guardar", 
            command=self.save_password,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Cancelar", 
            command=self.show_main_menu,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
    
    def save_password(self):
        """Guarda la nueva contraseña"""
        # Aquí iría la lógica para guardar la contraseña
        messagebox.showinfo("Éxito", "Contraseña guardada correctamente.")
        self.show_main_menu()
    
    def modify_password(self):
        """Muestra la interfaz para modificar una contraseña existente"""
        self.clear_frame()
        
        ttk.Label(
            self.main_frame, 
            text="Modificar Contraseña", 
            style='Title.TLabel'
        ).pack(pady=20)
        
        # En una versión completa, aquí se mostraría una lista de contraseñas para seleccionar
        ttk.Label(
            self.main_frame,
            text="Selecciona la contraseña que deseas modificar:",
            font=('Arial', 10)
        ).pack(pady=10)
        
        # Lista de ejemplo (en una versión real, esto vendría de la base de datos)
        passwords = ["Google - usuario@ejemplo.com", "Facebook - usuario@ejemplo.com"]
        
        listbox = tk.Listbox(
            self.main_frame,
            height=5,
            width=60,
            font=('Arial', 10)
        )
        
        for password in passwords:
            listbox.insert(tk.END, password)
        
        listbox.pack(pady=10, padx=20, fill=tk.BOTH)
        
        # Frame de botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(
            button_frame, 
            text="Editar Seleccionado", 
            command=lambda: self.edit_selected_password(listbox.get(tk.ACTIVE)),
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Regresar", 
            command=self.show_main_menu,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
    
    def edit_selected_password(self, selected):
        """Muestra el formulario para editar una contraseña"""
        # En una versión completa, aquí se cargarían los datos de la contraseña seleccionada
        messagebox.showinfo("Editar", f"Editando: {selected}")
    
    def search_password(self):
        """Muestra la interfaz de búsqueda de contraseñas"""
        self.clear_frame()
        
        ttk.Label(
            self.main_frame, 
            text="Buscar Contraseña", 
            style='Title.TLabel'
        ).pack(pady=20)
        
        # Campo de búsqueda
        search_frame = ttk.Frame(self.main_frame)
        search_frame.pack(pady=10, padx=50, fill=tk.X)
        
        ttk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT, padx=5)
        
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        ttk.Button(
            search_frame, 
            text="Buscar", 
            command=self.perform_search,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        # Área de resultados
        self.results_text = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            width=80,
            height=15,
            font=('Arial', 10)
        )
        self.results_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Botón de regreso
        ttk.Button(
            self.main_frame,
            text="Regresar al Menú",
            command=self.show_main_menu
        ).pack(pady=10)
    
    def perform_search(self):
        """Realiza la búsqueda de contraseñas"""
        search_term = self.search_entry.get()
        
        if not search_term:
            messagebox.showwarning("Búsqueda vacía", "Por favor ingresa un término de búsqueda.")
            return
        
        # En una versión completa, aquí se buscarían las contraseñas que coincidan
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.INSERT, f"Resultados para: {search_term}\n\n")
        self.results_text.insert(tk.INSERT, "En una versión completa, aquí se mostrarían las contraseñas ")
        self.results_text.insert(tk.INSERT, f"que coincidan con el término: '{search_term}'")
        self.results_text.config(state=tk.DISABLED)
    
    def generate_password(self):
        """Genera una contraseña segura"""
        import random
        import string
        
        # Generar una contraseña aleatoria
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Mostrar la contraseña generada
        self.clear_frame()
        
        ttk.Label(
            self.main_frame, 
            text="Generar Contraseña Segura", 
            style='Title.TLabel'
        ).pack(pady=20)
        
        # Mostrar la contraseña generada
        password_frame = ttk.Frame(self.main_frame)
        password_frame.pack(pady=10, padx=50, fill=tk.X)
        
        ttk.Label(password_frame, text="Contraseña generada:", font=('Arial', 10, 'bold')).pack(anchor='w')
        
        password_display = ttk.Entry(
            password_frame, 
            font=('Courier', 12), 
            justify='center',
            width=30
        )
        password_display.pack(pady=10, fill=tk.X)
        password_display.insert(0, password)
        password_display.config(state='readonly')
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(
            button_frame, 
            text="Copiar al Portapapeles", 
            command=lambda: self.copy_to_clipboard(password),
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Generar Otra", 
            command=self.generate_password,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Regresar al Menú", 
            command=self.show_main_menu,
            style='TButton'
        ).pack(side=tk.LEFT, padx=5)
    
    def copy_to_clipboard(self, text):
        """Copia texto al portapapeles"""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Copiado", "La contraseña ha sido copiada al portapapeles.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
