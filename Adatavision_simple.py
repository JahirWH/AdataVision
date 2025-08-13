import sys
import os
import csv
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from PySide6.QtCore import Qt

# Constantes
HEADERS = ['Código', 'Servicio', 'Email', 'Password', 'Usuario', 'Referencia', 'Fecha']
CSV_HEADERS = ['codigo', 'service', 'email', 'password', 'username', 'web', 'fecha']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Contraseñas - Versión Simple")
        self.setMinimumSize(800, 600)
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        # Widget central
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)

        # Tabla de datos
        self.table = QTableWidget()
        self.table.setColumnCount(len(HEADERS))
        self.table.setHorizontalHeaderLabels(HEADERS)
        layout.addWidget(self.table, stretch=2)

        # Panel de botones
        button_panel = QWidget()
        button_layout = QVBoxLayout(button_panel)
        
        # Botones
        refresh_btn = QPushButton("Actualizar")
        refresh_btn.clicked.connect(self.load_data)
        button_layout.addWidget(refresh_btn)

        button_layout.addStretch()
        layout.addWidget(button_panel)

    def load_data(self):
        """Carga los datos del archivo CSV."""
        try:
            # Verificar si el archivo existe
            if not os.path.exists('Inventario.csv'):
                with open('Inventario.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(CSV_HEADERS)
                return

            # Leer datos
            with open('Inventario.csv', 'r', newline='') as f:
                reader = csv.DictReader(f)
                data = list(reader)

            # Actualizar tabla
            self.table.setRowCount(len(data))
            for row, item in enumerate(data):
                for col, header in enumerate(CSV_HEADERS):
                    cell = QTableWidgetItem(item[header])
                    cell.setFlags(cell.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Hacer la celda no editable
                    self.table.setItem(row, col, cell)

            self.table.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al cargar datos: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
