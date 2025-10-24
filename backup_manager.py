import os
import shutil
from datetime import datetime
from typing import Optional

class BackupManager:
    def __init__(self, backup_dir: str = ".backups"):
        self.backup_dir = backup_dir
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
    def create_backup(self, file_path: str) -> Optional[str]:
        """Crea una copia de seguridad del archivo"""
        try:
            if not os.path.exists(file_path):
                return None
                
            # Crear nombre para el backup
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.basename(file_path)
            backup_path = os.path.join(
                self.backup_dir, 
                f"{filename}.{timestamp}.backup"
            )
            
            # Crear el backup
            shutil.copy2(file_path, backup_path)
            return backup_path
            
        except Exception as e:
            print(f"Error al crear backup: {str(e)}")
            return None
            
    def restore_backup(self, backup_path: str, target_path: str) -> bool:
        """Restaura un archivo desde su backup"""
        try:
            if not os.path.exists(backup_path):
                return False
                
            shutil.copy2(backup_path, target_path)
            return True
            
        except Exception as e:
            print(f"Error al restaurar backup: {str(e)}")
            return False
            
    def list_backups(self, original_file: str) -> list:
        """Lista todos los backups disponibles para un archivo"""
        try:
            filename = os.path.basename(original_file)
            backups = []
            
            for file in os.listdir(self.backup_dir):
                if file.startswith(filename) and file.endswith(".backup"):
                    backup_path = os.path.join(self.backup_dir, file)
                    backups.append({
                        "path": backup_path,
                        "date": datetime.fromtimestamp(
                            os.path.getmtime(backup_path)
                        ).strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
            return sorted(backups, key=lambda x: x["date"], reverse=True)
            
        except Exception as e:
            print(f"Error al listar backups: {str(e)}")
            return []