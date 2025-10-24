import base64

def is_file_encrypted(file_path: str) -> bool:
    """
    Detecta si un archivo está encriptado verificando su firma y estructura
    """
    SIGNATURE = b'ADATAVISION_ENCRYPTED_v1:'
    
    try:
        with open(file_path, 'rb') as file:
            # Leer la firma
            header = file.read(len(SIGNATURE))
            if header != SIGNATURE:
                return False
                
            # Leer el resto del contenido
            content = file.read()
            
            # Verificar que el contenido restante sea base64 válido
            try:
                # Intentar decodificar como base64 (formato usado por Fernet)
                padding_needed = 4 - (len(content) % 4)
                if padding_needed != 4:
                    content += b'=' * padding_needed
                base64.urlsafe_b64decode(content)
                return True
            except Exception:
                return False
                
    except FileNotFoundError:
        return False
    except Exception:
        return False

def verify_encryption_state(file_path: str) -> dict:
    """
    Verifica y retorna el estado actual del archivo
    """
    try:
        is_encrypted = is_file_encrypted(file_path)
        file_exists = True
        can_read = True
    except FileNotFoundError:
        is_encrypted = False
        file_exists = False
        can_read = False
    except PermissionError:
        is_encrypted = False
        file_exists = True
        can_read = False
    
    return {
        "exists": file_exists,
        "can_read": can_read,
        "is_encrypted": is_encrypted,
        "status": "encrypted" if is_encrypted else "decrypted" if (file_exists and can_read) else "unknown"
    }