import hashlib

# Hash salado generado con la contraseña "contraseña123" y la salt "abc123xyz789wqz456"
hashed_password = "bbe799dad85954165f80eb38fe8f2cce2242c5909726d4122e73c086c13bafc4471098e3ef5e6b09060196be76538705139b903b938538526818686c01bd0564"

# Obtener la salt del hash
salt = bytes.fromhex(hashed_password[:32*2])  # La salt es de 16 bytes

# Obtener la contraseña original sin la salt
password = hashed_password[32*2:]

# Imprimir la salt y el hash
print(f"La salt es: {salt.hex()}")
print(f"El hash es: {password}")