import sys
import os
import csv
import time
import base64
import hashlib
from datetime import date, datetime
from random import choice

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLineEdit, QLabel, 
                              QTableWidget, QTableWidgetItem, QMessageBox, 
                              QTabWidget, QGridLayout, QComboBox, QDialog,
                              QFileDialog, QProgressBar, QFrame, QStackedWidget,
                              QScrollArea, QSplashScreen)
from PySide6.QtCore import Qt, QTimer, Signal, Slot, QSize, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QPixmap, QColor, QPalette, QIcon, QKeySequence
from cryptography.fernet import Fernet
import polars as pl

# Constantes globales
TODAY = str(date.today())
HEADERS = ['Código', 'Servicio', 'Email', 'Password', 'Usuario', 'Referencia', 'Fecha']
CSV_HEADERS = ['codigo', 'service', 'email', 'password', 'username', 'web', 'fecha']

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
   
        
   
class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.username = ""
        
        # Layout principal
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(main_layout)
        
        # Panel izquierdo (formulario)
        left_panel = QWidget()
        left_panel.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                border-radius: 4px;
            }
        """)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(20, 20, 20, 20)
        left_layout.setSpacing(15)
        
        # Título del formulario
        form_title = QLabel("Usuario login")
        form_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
        """)
        form_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        left_layout.addWidget(form_title)
        
        # Campo de usuario
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Máximo 6 letras")
        self.user_input.setMaxLength(6)
        self.user_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #404040;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QLineEdit:focus {
                border: 1px solid #666666;
            }
        """)
        left_layout.addWidget(self.user_input)
        
        # Botones
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.login_button = QPushButton("Ingresar")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #404040;
                color: #ffffff;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        self.login_button.clicked.connect(self.accept_login)
        
        self.exit_button = QPushButton("Salir")
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #404040;
                color: #ffffff;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        self.exit_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.exit_button)
        left_layout.addLayout(button_layout)
        
        # Panel derecho (descripción)
        right_panel = QWidget()
        right_panel.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                border-radius: 4px;
            }
        """)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(20, 20, 20, 20)
        
        # Título y descripción en un solo párrafo
        description_text = """
        <p style='color: white; font-size: 14px; margin: 0;'>
        <b>ADATAVISION</b><br>
        Sistema de encriptación que combina usuario y contraseña para crear una clave única. 
        Los datos se encriptan automáticamente y solo podrán ser desencriptados con las credenciales originales.
        </p>
        """
        
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(description_label)
        
        # Agregar imagen
        image_label = QLabel()
        pixmap = QPixmap("cyberpunk.png")
        scaled_pixmap = pixmap.scaled(200, 140, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(image_label)
        
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)
        
        # Establecer tamaño fijo
        self.setFixedSize(700, 400)
    
    def accept_login(self):
        username = self.user_input.text()
        # password = self.password_input.text()
        
        if not username.isalpha() or len(username) > 6:
            QMessageBox.warning(self, "Error", "El usuario debe contener solo letras (máximo 6)")
            return
            
        # if not password:
        #     QMessageBox.warning(self, "Error", "Por favor ingrese su contraseña")
        #     return
            
        self.username = username
        self.accept()





class PasswordDialog(QDialog):
    def __init__(self, mode, parent=None):
        super().__init__(parent)
        self.mode = mode  # 'encrypt' o 'decrypt'
        
        if mode == 'encrypt':
            self.setWindowTitle("Encriptar Archivo")
            title_text = "Encriptación"
            button_text = "Encriptar"
        else:
            self.setWindowTitle("Desencriptar Archivo")
            title_text = "Desencriptación"
            button_text = "Desencriptar"
        
        self.setFixedSize(350, 150)
        
        # Layout principal
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Título
        title_label = QLabel(title_text)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Campo para la clave numérica
        key_layout = QHBoxLayout()
        key_label = QLabel("Clave numérica:")
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Máximo 6 dígitos")
        self.key_input.setMaxLength(6)
        self.key_input.setEchoMode(QLineEdit.EchoMode.Password)
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        # Botones
        button_layout = QHBoxLayout()
        self.process_button = QPushButton(button_text)
        self.process_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        self.process_button.clicked.connect(self.accept_password)
        
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.process_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
    
    def accept_password(self):
        password = self.key_input.text()
        if not password.isdigit() or len(password) > 6:
            QMessageBox.warning(self, "Error", "La clave debe contener solo números (máximo 6)")
            return
        self.password = password
        self.accept()

class PasswordGeneratorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Generador de Contraseñas")
        self.setFixedSize(600, 500)  # Aumentado el tamaño
        
        # Layout principal
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Título
        title_label = QLabel("Generador de Contraseñas")
        title_label.setStyleSheet("""
            font-size: 24px; 
            font-weight: bold;
            color: #00ff9f;
            margin-bottom: 20px;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Longitud de la contraseña
        length_layout = QHBoxLayout()
        length_label = QLabel("Longitud:")
        length_label.setStyleSheet("font-size: 16px;")
        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("Cantidad de caracteres")
        self.length_input.setText("12")
        self.length_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_input)
        layout.addLayout(length_layout)
        
        # Opciones de caracteres
        options_layout = QGridLayout()
        options_layout.setSpacing(15)
        
        self.include_lowercase = QComboBox()
        self.include_lowercase.addItems(["Incluir minúsculas", "No incluir minúsculas"])
        self.include_lowercase.setStyleSheet("""
            QComboBox {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        options_layout.addWidget(QLabel("Minúsculas:"), 0, 0)
        options_layout.addWidget(self.include_lowercase, 0, 1)
        
        self.include_uppercase = QComboBox()
        self.include_uppercase.addItems(["Incluir mayúsculas", "No incluir mayúsculas"])
        self.include_uppercase.setStyleSheet("""
            QComboBox {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        options_layout.addWidget(QLabel("Mayúsculas:"), 1, 0)
        options_layout.addWidget(self.include_uppercase, 1, 1)
        
        self.include_numbers = QComboBox()
        self.include_numbers.addItems(["Incluir números", "No incluir números"])
        self.include_numbers.setStyleSheet("""
            QComboBox {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        options_layout.addWidget(QLabel("Números:"), 2, 0)
        options_layout.addWidget(self.include_numbers, 2, 1)
        
        self.include_symbols = QComboBox()
        self.include_symbols.addItems(["Incluir símbolos", "No incluir símbolos"])
        self.include_symbols.setStyleSheet("""
            QComboBox {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        options_layout.addWidget(QLabel("Símbolos:"), 3, 0)
        options_layout.addWidget(self.include_symbols, 3, 1)
        
        layout.addLayout(options_layout)
        
        # Botón para generar
        self.generate_button = QPushButton("Generar Contraseñas")
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 5px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                min-width: 250px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        self.generate_button.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Área de resultados
        result_label = QLabel("Contraseñas Generadas:")
        result_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(result_label)
        
        self.results_area = QTableWidget(2, 2)
        self.results_area.setHorizontalHeaderLabels(["Contraseña", "Acciones"])
        self.results_area.horizontalHeader().setStretchLastSection(True)
        self.results_area.verticalHeader().setVisible(False)
        self.results_area.setStyleSheet("""
            QTableWidget {
                font-size: 14px;
                min-height: 150px;
            }
            QTableWidget::item {
                padding: 10px;
            }
        """)
        layout.addWidget(self.results_area)
        
        # Botón para cerrar
        self.close_button = QPushButton("Cerrar")
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        self.close_button.clicked.connect(self.accept)
        layout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.generated_passwords = []
    
    def generate_passwords(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                QMessageBox.warning(self, "Error", "La longitud debe ser un número positivo")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "La longitud debe ser un número entero")
            return
        
        use_lowercase = self.include_lowercase.currentText().startswith("Incluir")
        use_uppercase = self.include_uppercase.currentText().startswith("Incluir")
        use_numbers = self.include_numbers.currentText().startswith("Incluir")
        use_symbols = self.include_symbols.currentText().startswith("Incluir")
        
        if not any([use_lowercase, use_uppercase, use_numbers, use_symbols]):
            QMessageBox.warning(self, "Error", "Debe seleccionar al menos un tipo de caracteres")
            return
        
        chars = ""
        if use_lowercase:
            chars += "abcdefghijklmnopqrstuvwxyz"
        if use_uppercase:
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if use_numbers:
            chars += "0123456789"
        if use_symbols:
            chars += "<=>@#%&+!?*()[]{}^~-_.:,;"
        
        self.generated_passwords = []
        for _ in range(2):
            password = ''.join([choice(chars) for _ in range(length)])
            self.generated_passwords.append(password)
        
        self.update_results_table()
        
        # Guardar la última contraseña en temp.txt
        with open('temp.txt', 'w') as file:
            file.write(self.generated_passwords[-1])
    
    def update_results_table(self):
        self.results_area.setRowCount(len(self.generated_passwords))
        
        for i, password in enumerate(self.generated_passwords):
            # Contraseña
            password_item = QTableWidgetItem(password)
            password_item.setFlags(password_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.results_area.setItem(i, 0, password_item)
            
            # Botón para copiar
            copy_button = QPushButton("Copiar")
            copy_button.clicked.connect(lambda _, p=password: QApplication.clipboard().setText(p))
            self.results_area.setCellWidget(i, 1, copy_button)
        
        self.results_area.resizeColumnsToContents()

class KeyGeneratorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Generador de Claves")
        self.setFixedSize(500, 400)  # Aumentado el tamaño
        
        # Layout principal
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Título
        title_label = QLabel("Generador de Claves de Encriptación")
        title_label.setStyleSheet("""
            font-size: 24px; 
            font-weight: bold;
            color: #00ff9f;
            margin-bottom: 20px;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Campo de usuario
        user_layout = QHBoxLayout()
        user_label = QLabel("Usuario:")
        user_label.setStyleSheet("font-size: 16px;")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Máximo 6 letras")
        self.user_input.setMaxLength(6)
        self.user_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        user_layout.addWidget(user_label)
        user_layout.addWidget(self.user_input)
        layout.addLayout(user_layout)
        
        # Campo de clave numérica
        key_layout = QHBoxLayout()
        key_label = QLabel("Clave numérica:")
        key_label.setStyleSheet("font-size: 16px;")
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Máximo 6 dígitos")
        self.key_input.setMaxLength(6)
        self.key_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                min-width: 200px;
            }
        """)
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        # Área para mostrar la clave generada
        self.key_display = QLineEdit()
        self.key_display.setReadOnly(True)
        self.key_display.setPlaceholderText("La clave generada se mostrará aquí")
        self.key_display.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a2e;
                padding: 10px;
                font-size: 14px;
                min-height: 40px;
            }
        """)
        layout.addWidget(self.key_display)
        
        # Botones
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.generate_button = QPushButton("Generar Clave")
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 5px;
                padding: 12px;
                font-size: 14px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        self.generate_button.clicked.connect(self.generate_key)
        
        self.save_button = QPushButton("Guardar")
        self.save_button.setEnabled(False)
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71;
                color: white;
                border-radius: 5px;
                padding: 12px;
                font-size: 14px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            QPushButton:disabled {
                background-color: #95A5A6;
            }
        """)
        self.save_button.clicked.connect(self.save_key)
        
        self.encrypt_button = QPushButton("Encriptar Ahora")
        self.encrypt_button.setEnabled(False)
        self.encrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border-radius: 5px;
                padding: 12px;
                font-size: 14px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
            QPushButton:disabled {
                background-color: #95A5A6;
            }
        """)
        self.encrypt_button.clicked.connect(self.encrypt_now)
        
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.encrypt_button)
        layout.addLayout(button_layout)
        
        # Botón para cerrar
        self.close_button = QPushButton("Cerrar")
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #95A5A6;
                color: white;
                border-radius: 5px;
                padding: 12px;
                font-size: 14px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #7F8C8D;
            }
        """)
        self.close_button.clicked.connect(self.reject)
        layout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.generated_key = None
    
    def generate_key(self):
        username = self.user_input.text()
        if not username.isalpha() or len(username) > 6:
            QMessageBox.warning(self, "Error", "El usuario debe contener solo letras (máximo 6)")
            return
        
        key = self.key_input.text()
        if not key.isdigit() or len(key) > 6:
            QMessageBox.warning(self, "Error", "La clave debe contener solo números (máximo 6)")
            return
        
        clave_base = username + key
        clave_hash = hashlib.sha256(clave_base.encode()).digest()
        clave_final = base64.urlsafe_b64encode(clave_hash[:32])
        
        self.generated_key = clave_final
        self.key_display.setText(clave_final.decode())
        
        self.save_button.setEnabled(True)
        self.encrypt_button.setEnabled(True)
    
    def save_key(self):
        if not self.generated_key:
            return
        
        username = self.user_input.text()
        key = self.key_input.text()
        
        with open('clave.txt', 'wb') as archivo:
            archivo.write(f"Usuario: {username}:password:{key}\n".encode())
        
        QMessageBox.information(self, "Éxito", "La clave se ha guardado con éxito en clave.txt")
    
    def encrypt_now(self):
        if not self.generated_key:
            return
        
        try:
            with open('estado.txt', "r") as le:
                estado = le.read().strip()
            if estado == "encrypted":
                QMessageBox.warning(self, "Error", "El archivo ya está encriptado")
                return
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No se encontró el archivo estado.txt")
            return
        
        try:
            with open('Inventario.csv', 'rb') as archivo:
                datos = archivo.read()
                f = Fernet(self.generated_key)
                datos_cifrados = f.encrypt(datos)
            
            with open('Inventario.csv', 'wb') as encrypted_file:
                encrypted_file.write(datos_cifrados)
            
            # Actualizar el estado
            with open('estado.txt', 'w') as archivo_estado:
                archivo_estado.write("encrypted")
            
            QMessageBox.information(self, "Éxito", "El archivo se encriptó con éxito")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo encriptar el archivo: {str(e)}")

class EncryptedFileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Archivo Encriptado")
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
            QDialog {
                background-color: #1a1a1a;
            }
            QLabel {
                color: #ffffff;
                font-size: 16px;
            }
            QPushButton {
                background-color: #404040;
                color: #ffffff;
                border-radius: 4px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: normal;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Icono de candado
        lock_label = QLabel("🔒")
        lock_label.setStyleSheet("""
            font-size: 48px;
            color: #ffffff;
        """)
        lock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lock_label)
        
        # Título
        title_label = QLabel("ARCHIVO ENCRIPTADO")
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            margin: 10px 0;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Mensaje
        message_label = QLabel("Para acceder al contenido, primero debe desencriptar el archivo.")
        message_label.setWordWrap(True)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message_label)
        
        # Botón
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        ok_button = QPushButton("Entendido")
        ok_button.clicked.connect(self.accept)
        button_layout.addWidget(ok_button)
        
        button_layout.addStretch()
        layout.addLayout(button_layout)

class AdatavisionMainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.last_used_password = None  # Variable para guardar la última contraseña usada
        self.initUI()
        
        # Cargar información inicial
        self.load_last_modified()
        self.load_temp_password()
        self.check_file_status()
    
    def initUI(self):
        self.setWindowTitle("Adatavision - Gestor de Contraseñas")
        self.setMinimumSize(1000, 600)
        
        # Establecer el estilo minimalista para la ventana principal
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QPushButton {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #404040;
                border-radius: 4px;
                padding: 8px 15px;
                font-weight: normal;
                min-width: 150px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #404040;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #404040;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #666666;
            }
            QTableWidget {
                background-color: #2d2d2d;
                color: #ffffff;
                gridline-color: #404040;
                border: 1px solid #404040;
                border-radius: 4px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #404040;
                color: #ffffff;
            }
            QTableWidget::item:hover {
                background-color: #333333;
                cursor: pointer;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #404040;
                padding: 5px;
            }
            QMenuBar {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QMenuBar::item {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QMenuBar::item:selected {
                background-color: #404040;
                color: #ffffff;
            }
            QMenu {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #404040;
            }
            QMenu::item:selected {
                background-color: #404040;
                color: #ffffff;
            }
            QStatusBar {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
        """)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Panel izquierdo (tabla y búsqueda)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Barra de estado con estilo minimalista
        self.status_bar = self.statusBar()
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #2d2d2d;
                color: #ffffff;
                border-top: 1px solid #404040;
            }
        """)
        self.status_bar.showMessage(f"Usuario: {self.username} | Bienvenido a Adatavision")
        
        # Área de información con estilo minimalista
        info_frame = QFrame()
        info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        info_frame.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
            }
        """)
        
        info_layout = QHBoxLayout(info_frame)
        info_layout.setSpacing(20)
        
        # Modificación
        self.modification_label = QLabel("Última modificación: Cargando...")
        self.modification_label.setStyleSheet("color: #ffffff; font-weight: bold;")
        info_layout.addWidget(self.modification_label)
        
        # Contraseña temporal
        self.temp_password_label = QLabel("Contraseña temporal: Cargando...")
        self.temp_password_label.setStyleSheet("""
            color: #ffffff; 
            font-weight: bold;
            padding: 5px;
            border: 1px solid #404040;
            border-radius: 3px;
        """)
        self.temp_password_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.temp_password_label.mousePressEvent = self.copy_temp_password
        info_layout.addWidget(self.temp_password_label)
        
        # Estado del archivo
        self.file_status_label = QLabel("Estado del archivo: Cargando...")
        self.file_status_label.setStyleSheet("color: #ffffff; font-weight: bold;")
        info_layout.addWidget(self.file_status_label)
        
        left_layout.addWidget(info_frame)
        
        # Campo de búsqueda
        search_layout = QHBoxLayout()
        search_label = QLabel("Buscar:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Introduce texto para buscar...")
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_items)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        left_layout.addLayout(search_layout)
        
        # Tabla de datos
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(7)
        self.data_table.setHorizontalHeaderLabels(HEADERS)
        self.data_table.horizontalHeader().setStretchLastSection(True)
        self.data_table.cellClicked.connect(self.copy_cell_content)
        left_layout.addWidget(self.data_table)
        
        # Panel derecho (botones)
        right_panel = QWidget()
        right_panel.setFixedWidth(200)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Botones principales
        self.refresh_button = QPushButton("Actualizar")
        self.refresh_button.clicked.connect(self.load_inventory)
        right_layout.addWidget(self.refresh_button)
        
        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.show_add_dialog)
        right_layout.addWidget(self.add_button)
        
        # Botones de herramientas
        self.encrypt_button = QPushButton("Encriptar")
        self.encrypt_button.clicked.connect(self.encrypt_file)
        right_layout.addWidget(self.encrypt_button)
        
        self.decrypt_button = QPushButton("Desencriptar")
        self.decrypt_button.clicked.connect(self.decrypt_file)
        right_layout.addWidget(self.decrypt_button)
        
        self.generate_password_button = QPushButton("Generar Contraseñas")
        self.generate_password_button.clicked.connect(self.generate_passwords)
        right_layout.addWidget(self.generate_password_button)
        
        self.generate_key_button = QPushButton("Generar Claves")
        self.generate_key_button.clicked.connect(self.generate_keys)
        right_layout.addWidget(self.generate_key_button)
        
        # Agregar los paneles al layout principal
        main_layout.addWidget(left_panel, stretch=7)
        main_layout.addWidget(right_panel, stretch=1)
        
        # Barra de menú
        self.create_menu_bar()
        
        # Accesos rápidos de teclado
        self.setup_shortcuts()
    
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu("Archivo")
        
        refresh_action = file_menu.addAction("Actualizar")
        refresh_action.triggered.connect(self.load_inventory)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Salir")
        exit_action.triggered.connect(self.close)
        
        # Menú Herramientas
        tools_menu = menubar.addMenu("Herramientas")
        
        encrypt_action = tools_menu.addAction("Encriptar")
        encrypt_action.triggered.connect(self.encrypt_file)
        
        decrypt_action = tools_menu.addAction("Desencriptar")
        decrypt_action.triggered.connect(self.decrypt_file)
        
        tools_menu.addSeparator()
        
        gen_pass_action = tools_menu.addAction("Generar Contraseñas")
        gen_pass_action.triggered.connect(self.generate_passwords)
        
        gen_key_action = tools_menu.addAction("Generar Claves")
        gen_key_action.triggered.connect(self.generate_keys)
        
        # Menú Ayuda
        help_menu = menubar.addMenu("Ayuda")
        
        about_action = help_menu.addAction("Acerca de")
        about_action.triggered.connect(self.show_about)
    
    def setup_shortcuts(self):
        # Accesos rápidos de teclado
        self.refresh_shortcut = QKeySequence("F5")
        self.refresh_button.setShortcut(self.refresh_shortcut)
        
        self.search_shortcut = QKeySequence("Ctrl+F")
        self.search_button.setShortcut(self.search_shortcut)
        
        self.add_shortcut = QKeySequence("Ctrl+N")
        self.add_button.setShortcut(self.add_shortcut)
    
    def load_last_modified(self):
        try:
            with open('date.txt', 'r') as file:
                last_modified = file.read()
                self.modification_label.setText(f"Última modificación: {last_modified}")
        except FileNotFoundError:
            with open('date.txt', 'w') as file:
                now = str(datetime.now())
                file.write(now)
                self.modification_label.setText(f"Última modificación: {now}")
    
    def load_temp_password(self):
        try:
            with open('temp.txt', 'r') as file:
                temp_password = file.read()
                self.temp_password_label.setText(f"Contraseña temporal: {temp_password}")
        except FileNotFoundError:
            with open('temp.txt', 'w') as file:
                file.write("No hay contraseña temporal")
                self.temp_password_label.setText("Contraseña temporal: No hay contraseña temporal")
    
    def check_file_status(self):
        try:
            with open('estado.txt', 'r') as file:
                status = file.read().strip()
                if status == "encrypted":
                    self.file_status_label.setText("Estado del archivo: Encriptado")
                    self.file_status_label.setStyleSheet("color: #27AE60; font-weight: bold;")
                elif status == "decrypted":
                    self.file_status_label.setText("Estado del archivo: Desencriptado")
                    self.file_status_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
                else:
                    self.file_status_label.setText("Estado del archivo: Desconocido")
        except FileNotFoundError:
            with open('estado.txt', 'w') as file:
                file.write("decrypted")
                self.file_status_label.setText("Estado del archivo: Desencriptado")
                self.file_status_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
    
    def load_inventory(self):
        try:
            # Verificar si el archivo está encriptado
            with open('estado.txt', 'r') as file:
                status = file.read().strip()
                if status == "encrypted":
                    dialog = EncryptedFileDialog(self)
                    dialog.exec()
                    self.data_table.setRowCount(0)
                    return
            
            # Cargar datos con polars
            df = pl.read_csv('Inventario.csv')
            
            # Llenar la tabla
            self.data_table.setRowCount(len(df))
            
            for i, row in enumerate(df.iter_rows(named=True)):
                for j, col in enumerate(CSV_HEADERS):
                    item = QTableWidgetItem(str(row[col]))
                    # Hacer que las celdas no sean editables pero sean seleccionables
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable)
                    self.data_table.setItem(i, j, item)
            
            self.data_table.resizeColumnsToContents()
            self.status_bar.showMessage("Inventario cargado correctamente", 3000)
        
        except FileNotFoundError:
            # Crear el archivo si no existe
            with open('Inventario.csv', 'w') as file:
                file.write(','.join(CSV_HEADERS) + '\n')
            self.data_table.setRowCount(0)
            self.status_bar.showMessage("Se creó un nuevo archivo de inventario vacío", 3000)
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar el inventario: {str(e)}")
    
    def show_add_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Nuevo Elemento")
        dialog.setFixedSize(400, 300)
        
        layout = QVBoxLayout(dialog)
        
        form_layout = QGridLayout()
        
        # Campos para agregar
        service_label = QLabel("Servicio:")
        self.service_input = QLineEdit()
        form_layout.addWidget(service_label, 0, 0)
        form_layout.addWidget(self.service_input, 0, 1)
        
        email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        form_layout.addWidget(email_label, 1, 0)
        form_layout.addWidget(self.email_input, 1, 1)
        
        password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        form_layout.addWidget(password_label, 2, 0)
        form_layout.addWidget(self.password_input, 2, 1)
        
        username_label = QLabel("Usuario:")
        self.username_input = QLineEdit()
        form_layout.addWidget(username_label, 3, 0)
        form_layout.addWidget(self.username_input, 3, 1)
        
        ref_label = QLabel("Referencia:")
        self.ref_input = QLineEdit()
        form_layout.addWidget(ref_label, 4, 0)
        form_layout.addWidget(self.ref_input, 4, 1)
        
        layout.addLayout(form_layout)
        
        # Botones
        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Guardar")
        save_button.clicked.connect(lambda: self.add_new_item(dialog))
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton("Cancelar")
        cancel_button.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        dialog.exec()
    
    def add_new_item(self, dialog=None):
        # Verificar si el archivo está encriptado
        try:
            with open('estado.txt', 'r') as file:
                status = file.read().strip()
                if status == "encrypted":
                    encrypted_dialog = EncryptedFileDialog(self)
                    encrypted_dialog.exec()
                    return
        except FileNotFoundError:
            with open('estado.txt', 'w') as file:
                file.write("decrypted")
        
        # Obtener valores de los campos
        service = self.service_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        username = self.username_input.text().strip()
        reference = self.ref_input.text().strip()
        
        # Validar que no estén vacíos
        if not all([service, email, password, username, reference]):
            QMessageBox.warning(self, "Campos Vacíos", "Todos los campos son obligatorios")
            return
        
        # Generar código único
        from random import randint
        code = ''.join(str(randint(0, 9)) for _ in range(4))
        
        # Verificar si el código ya existe
        try:
            with open('Inventario.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['codigo'] == code:
                        QMessageBox.warning(self, "Código Duplicado", 
                                          "Se generó un código duplicado. Intente nuevamente.")
                        return
        except FileNotFoundError:
            pass
        
        # Agregar el nuevo elemento
        today = str(date.today())
        
        try:
            with open('Inventario.csv', 'a', newline='') as file:
                file.write(f"\n{code},{service},{email},{password},{username},{reference},{today}")
            
            # Actualizar la fecha de modificación
            with open('date.txt', 'w') as file:
                now = str(datetime.now())
                file.write(now)
            
            # Limpiar campos
            self.service_input.clear()
            self.email_input.clear()
            self.password_input.clear()
            self.username_input.clear()
            self.ref_input.clear()
            
            # Recargar inventario
            self.load_inventory()
            self.load_last_modified()
            
            QMessageBox.information(self, "Éxito", "Elemento agregado correctamente")
            
            if dialog:
                dialog.accept()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo agregar el elemento: {str(e)}")
    
    def search_items(self):
        # Verificar si el archivo está encriptado
        try:
            with open('estado.txt', 'r') as file:
                status = file.read().strip()
                if status == "encrypted":
                    encrypted_dialog = EncryptedFileDialog(self)
                    encrypted_dialog.exec()
                    self.data_table.setRowCount(0)
                    return
        except FileNotFoundError:
            with open('estado.txt', 'w') as file:
                file.write("decrypted")
        
        search_text = self.search_input.text().strip().lower()
        
        if not search_text:
            QMessageBox.warning(self, "Campo Vacío", "Ingrese un texto para buscar")
            return
        
        try:
            df = pl.read_csv('Inventario.csv')
            
            # Filtrar resultados
            filtered_df = df.filter(
                pl.col("codigo").cast(pl.Utf8).str.contains(search_text, literal=True) |
                pl.col("service").str.contains(search_text, literal=True) |
                pl.col("email").str.contains(search_text, literal=True) |
                pl.col("password").str.contains(search_text, literal=True) |
                pl.col("username").str.contains(search_text, literal=True) |
                pl.col("web").str.contains(search_text, literal=True)
            )
            
            # Mostrar resultados
            self.data_table.setRowCount(len(filtered_df))
            
            for i, row in enumerate(filtered_df.iter_rows(named=True)):
                for j, col in enumerate(CSV_HEADERS):
                    item = QTableWidgetItem(str(row[col]))
                    # Hacer que las celdas no sean editables pero sean seleccionables
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable)
                    self.data_table.setItem(i, j, item)
            
            self.data_table.resizeColumnsToContents()
            
            self.status_bar.showMessage(f"Se encontraron {len(filtered_df)} resultados", 3000)
        
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No se encontró el archivo de inventario")
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo realizar la búsqueda: {str(e)}")
    
    def encrypt_file(self):
        # Verificar si el archivo ya está encriptado
        try:
            with open('estado.txt', 'r') as file:
                status = file.read().strip()
                if status == "encrypted":
                    QMessageBox.warning(self, "Archivo Encriptado", 
                                      "El archivo ya está encriptado.")
                    return
        except FileNotFoundError:
            with open('estado.txt', 'w') as file:
                file.write("decrypted")
        
        # Mostrar diálogo para ingresar contraseña
        dialog = PasswordDialog('encrypt', self)
        if dialog.exec():
            password = dialog.password
            
            # Generar clave a partir del usuario y contraseña
            clave_base = self.username + password
            clave_hash = hashlib.sha256(clave_base.encode()).digest()
            clave_final = base64.urlsafe_b64encode(clave_hash[:32])
            
            try:
                with open('Inventario.csv', 'rb') as archivo:
                    datos = archivo.read()
                    f = Fernet(clave_final)
                    datos_cifrados = f.encrypt(datos)
                
                with open('Inventario.csv', 'wb') as encrypted_file:
                    encrypted_file.write(datos_cifrados)
                
                # Actualizar el estado
                with open('estado.txt', 'w') as archivo_estado:
                    archivo_estado.write("encrypted")
                
                self.check_file_status()
                self.data_table.setRowCount(0)
                
                QMessageBox.information(self, "Éxito", "El archivo se encriptó con éxito")
            
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo encriptar el archivo: {str(e)}")
    
    def decrypt_file(self):
        # Verificar si el archivo ya está desencriptado
        try:
            with open('estado.txt', 'r') as file:
                status = file.read().strip()
                if status == "decrypted":
                    QMessageBox.warning(self, "Archivo Desencriptado", 
                                      "El archivo ya está desencriptado.")
                    return
        except FileNotFoundError:
            with open('estado.txt', 'w') as file:
                file.write("encrypted")
        
        # Mostrar diálogo para ingresar contraseña
        dialog = PasswordDialog('decrypt', self)
        if dialog.exec():
            password = dialog.password
            
            # Guardar la contraseña para uso posterior
            self.last_used_password = password
            
            # Generar clave a partir del usuario y contraseña
            clave_base = self.username + password
            clave_hash = hashlib.sha256(clave_base.encode()).digest()
            clave_final = base64.urlsafe_b64encode(clave_hash[:32])
            
            try:
                with open('Inventario.csv', 'rb') as archivo:
                    datos_cifrados = archivo.read()
                    f = Fernet(clave_final)
                    datos_descifrados = f.decrypt(datos_cifrados)
                
                with open('Inventario.csv', 'wb') as decrypted_file:
                    decrypted_file.write(datos_descifrados)
                
                # Actualizar el estado
                with open('estado.txt', 'w') as archivo_estado:
                    archivo_estado.write("decrypted")
                
                self.check_file_status()
                self.load_inventory()
                
                QMessageBox.information(self, "Éxito", "El archivo se desencriptó con éxito")
            
            except Exception as e:
                QMessageBox.critical(self, "Error", "No se pudo desencriptar el archivo. Verifique la contraseña.")
    
    def generate_passwords(self):
        dialog = PasswordGeneratorDialog(self)
        if dialog.exec():
            self.load_temp_password()
    
    def generate_keys(self):
        dialog = KeyGeneratorDialog(self)
        dialog.exec()
        self.check_file_status()
    
    def show_about(self):
        about_text = """
        <h2>Adatavision</h2>
        <p>Gestor de Contraseñas Seguro</p>
        <p>Versión: 2.0</p>
        <p>Esta aplicación permite almacenar y gestionar contraseñas de forma segura.</p>
        <p>Desarrollado con PySide6.</p>
        """
        QMessageBox.about(self, "Acerca de Adatavision", about_text)
    
    def closeEvent(self, event):
        try:
            # Verificar el estado actual del archivo
            with open('estado.txt', 'r') as file:
                current_status = file.read().strip()
            
            # Si está desencriptado y tenemos las credenciales, intentar encriptar
            if current_status == "decrypted" and self.last_used_password is not None:
                # Generar clave de encriptación con las credenciales guardadas
                clave_base = self.username + self.last_used_password
                clave_hash = hashlib.sha256(clave_base.encode()).digest()
                clave_final = base64.urlsafe_b64encode(clave_hash[:32])
                
                try:
                    # Encriptar el archivo
                    with open('Inventario.csv', 'rb') as archivo:
                        datos = archivo.read()
                        f = Fernet(clave_final)
                        datos_cifrados = f.encrypt(datos)
                    
                    with open('Inventario.csv', 'wb') as encrypted_file:
                        encrypted_file.write(datos_cifrados)
                    
                    # Actualizar el estado
                    with open('estado.txt', 'w') as archivo_estado:
                        archivo_estado.write("encrypted")
                    
                    QMessageBox.information(self, "Éxito", "Archivo encriptado automáticamente al cerrar")
                except Exception as e:
                    QMessageBox.warning(self, "Error", 
                                      f"No se pudo encriptar el archivo automáticamente: {str(e)}")
            elif current_status == "decrypted":
                QMessageBox.warning(self, "Advertencia", 
                                  "El archivo está desencriptado pero no hay credenciales guardadas para encriptar automáticamente")
            elif current_status != "encrypted":
                QMessageBox.warning(self, "Inconsistencia", 
                                  "El estado del archivo es inconsistente. Por favor, verifique manualmente.")
        
        except FileNotFoundError:
            QMessageBox.warning(self, "Advertencia", 
                              "No se pudo verificar el estado del archivo")
        
        event.accept()

    def copy_temp_password(self, event):
        try:
            with open('temp.txt', 'r') as file:
                temp_password = file.read().strip()
                if temp_password != "No hay contraseña temporal":
                    QApplication.clipboard().setText(temp_password)
                    self.status_bar.showMessage("Contraseña temporal copiada al portapapeles", 2000)
                else:
                    self.status_bar.showMessage("No hay contraseña temporal para copiar", 2000)
        except FileNotFoundError:
            self.status_bar.showMessage("No hay contraseña temporal para copiar", 2000)

    def copy_cell_content(self, row, column):
        item = self.data_table.item(row, column)
        if item is not None:
            content = item.text()
            QApplication.clipboard().setText(content)
            self.status_bar.showMessage(f"Contenido copiado: {content}", 2000)

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Mostrar splash screen
    splash = SplashScreen()
    splash.show()
    
    # Procesar eventos para mostrar el splash
    app.processEvents()
    
    # Mostrar diálogo de login
    login_dialog = LoginDialog()
    if login_dialog.exec():
        username = login_dialog.username
        main_window = AdatavisionMainWindow(username)
        main_window.show()
        main_window.load_inventory()
        return app.exec()
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())