import base64
import csv
import hashlib
import json
from datetime import datetime
from cryptography.fernet import Fernet
from typing import Optional, Dict, List, Tuple

class SecureDataManager:
    SIGNATURE = b'ADATAVISION_ENCRYPTED_v1:'  # Firma para detectar archivos encriptados
    
    def __init__(self):
        self.virtual_data: List[Dict] = []  # Datos en memoria
        self.is_modified: bool = False
        self.encryption_key: Optional[bytes] = None
        self.last_modified: str = datetime.now().strftime("%Y-%m-%d")
        self.file_status: str = "unknown"
        
    def generate_key(self, username: str, password: str) -> bytes:
        """Genera una clave de encriptación basada en usuario y contraseña"""
        clave_base = username + password
        clave_hash = hashlib.sha256(clave_base.encode()).digest()
        return base64.urlsafe_b64encode(clave_hash[:32])
    
    def is_file_encrypted(self, file_path: str) -> bool:
        """Detecta si un archivo está encriptado verificando la firma"""
        try:
            with open(file_path, 'rb') as file:
                header = file.read(len(self.SIGNATURE))
                return header == self.SIGNATURE
        except FileNotFoundError:
            return False
        except Exception:
            return False
    
    def load_data(self, file_path: str, encryption_key: Optional[bytes] = None) -> bool:
        """Carga datos del archivo a memoria"""
        try:
            is_encrypted = self.is_file_encrypted(file_path)
            
            with open(file_path, 'rb') as file:
                content = file.read()
                
                if is_encrypted:
                    if not encryption_key:
                        raise ValueError("Se requiere clave para desencriptar")
                    
                    # Remover la firma
                    content = content[len(self.SIGNATURE):]
                    
                    f = Fernet(encryption_key)
                    decrypted_data = f.decrypt(content)
                    self.virtual_data = json.loads(decrypted_data.decode())
                    self.encryption_key = encryption_key
                    self.file_status = "decrypted"
                else:
                    # Archivo no encriptado
                    self.virtual_data = json.loads(content.decode())
                    self.file_status = "decrypted"
                
                self.is_modified = False
                return True
                
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")
            return False
    
    def save_data(self, file_path: str, encrypt: bool = False) -> Tuple[bool, str]:
        """Guarda los datos en un nuevo archivo"""
        if not self.is_modified and not encrypt:
            return True, file_path
            
        try:
            # Crear nombre para nuevo archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_file_path = f"{file_path}.{timestamp}"
            
            # Convertir datos a JSON
            data_json = json.dumps(self.virtual_data, ensure_ascii=False)
            
            if encrypt:
                if not self.encryption_key:
                    raise ValueError("Se requiere clave para encriptar")
                
                # Encriptar datos
                f = Fernet(self.encryption_key)
                encrypted_data = f.encrypt(data_json.encode())
                
                # Agregar firma
                final_data = self.SIGNATURE + encrypted_data
                
                with open(new_file_path, 'wb') as file:
                    file.write(final_data)
                
                self.file_status = "encrypted"
            else:
                # Guardar sin encriptar
                with open(new_file_path, 'w', encoding='utf-8') as file:
                    file.write(data_json)
                
                self.file_status = "decrypted"
            
            self.is_modified = False
            self.last_modified = datetime.now().strftime("%Y-%m-%d")
            return True, new_file_path
            
        except Exception as e:
            print(f"Error al guardar datos: {str(e)}")
            return False, ""
    
    def modify_data(self, index: int, new_data: Dict) -> bool:
        """Modifica un registro en memoria"""
        if 0 <= index < len(self.virtual_data):
            self.virtual_data[index] = new_data
            self.is_modified = True
            return True
        return False
    
    def add_data(self, new_data: Dict) -> bool:
        """Agrega un nuevo registro a los datos en memoria"""
        try:
            self.virtual_data.append(new_data)
            self.is_modified = True
            return True
        except Exception:
            return False
    
    def get_data(self) -> List[Dict]:
        """Obtiene una copia de los datos en memoria"""
        return self.virtual_data.copy()
    
    def search_data(self, criteria: Dict) -> List[Dict]:
        """Busca registros que coincidan con los criterios"""
        results = []
        for item in self.virtual_data:
            matches = True
            for key, value in criteria.items():
                if key not in item or item[key] != value:
                    matches = False
                    break
            if matches:
                results.append(item.copy())
        return results
    
    def get_status(self) -> Dict:
        """Retorna el estado actual del gestor de datos"""
        return {
            "file_status": self.file_status,
            "is_modified": self.is_modified,
            "last_modified": self.last_modified,
            "records_count": len(self.virtual_data)
        }