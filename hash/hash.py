import hashlib
import os

# Generar una sal aleatoria de 16 bytes
salt = os.urandom(16)

# Contraseña que se va a hashear
password = b"my_password"

# Concatenar la contraseña con la sal
salted_password = password + salt

# Generar el hash SHA512 de la contraseña con la sal
hashed_password = hashlib.sha256(salted_password).hexdigest()
hashed_password_2 = hashlib.sha384(salted_password).hexdigest()
hashed_password_unsalt = hashlib.sha384(password).hexdigest()

# Imprimir el resultado
print(hashed_password)
print(hashed_password_2)