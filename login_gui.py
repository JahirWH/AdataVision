import tkinter as tk
from tkinter import ttk, messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Configurar el estilo
        self.setup_styles()
        
        # Crear la interfaz
        self.create_widgets()
    
    def setup_styles(self):
        """Configura los estilos de la aplicación"""
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10))
    
    def create_widgets(self):
        """Crea los widgets de la interfaz"""
        # Frame principal para centrar el contenido
        main_frame = ttk.Frame(self.root, padding="40 20")
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="Inicio de Sesión", 
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=(0, 30))
        
        # Frame para el formulario
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill=tk.X, pady=10)
        
        # Etiqueta y campo de usuario
        ttk.Label(form_frame, text="Usuario:").pack(anchor='w', pady=(0, 5))
        self.username_entry = ttk.Entry(form_frame, width=30)
        self.username_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Etiqueta y campo de contraseña
        ttk.Label(form_frame, text="Contraseña:").pack(anchor='w', pady=(0, 5))
        self.password_entry = ttk.Entry(form_frame, width=30, show="*")
        self.password_entry.pack(fill=tk.X, pady=(0, 25))
        
        # Botón de inicio de sesión
        login_button = ttk.Button(
            form_frame, 
            text="Iniciar Sesión", 
            command=self.verify_login,
            width=20
        )
        login_button.pack(pady=5)
        
        # Botón de salir
        exit_button = ttk.Button(
            form_frame, 
            text="Salir", 
            command=self.root.quit,
            width=20
        )
        exit_button.pack(pady=5)
        
        # Enfocar el campo de usuario al iniciar
        self.username_entry.focus()
        
        # Configurar la tecla Enter para iniciar sesión
        self.root.bind('<Return>', lambda e: self.verify_login())
    
    def verify_login(self):
        """Verifica las credenciales del usuario"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña")
            return
        
        # Aquí iría la lógica de verificación real
        # Por ahora, solo mostramos un mensaje de éxito
        messagebox.showinfo("Éxito", f"Bienvenido, {username}")
        
        # Aquí podrías abrir la ventana principal de la aplicación
        # self.open_main_application()

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
