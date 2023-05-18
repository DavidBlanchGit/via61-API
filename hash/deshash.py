import hashlib
import os

# Generar una sal aleatoria de 16 bytes
salt = os.urandom(16)

# Contraseña que se va a hashear y verificar
password = b"my_password"

# Concatenar la contraseña con la sal
salted_password = password + salt

# Generar el hash SHA512 de la contraseña con la sal
hashed_password = hashlib.sha512(salted_password).hexdigest()

# Imprimir el hash generado
print("Hash generado: ", hashed_password)

# Simulación de almacenamiento en la base de datos (en realidad se debería guardar el hash y la sal)
stored_hash = hashed_password
stored_salt = salt

# Contraseña ingresada por el usuario
user_password = b"CXZzCxz"

# Concatenar la contraseña ingresada por el usuario con la sal almacenada en la base de datos
salted_user_password = user_password + stored_salt

# Generar el hash SHA512 de la contraseña ingresada por el usuario con la sal almacenada en la base de datos
hashed_user_password = hashlib.sha512(salted_user_password).hexdigest()

# Comparar el hash generado con el hash almacenado en la base de datos
if hashed_user_password == stored_hash:
    print("Contraseña válida")
else:
    print("Contraseña inválida")