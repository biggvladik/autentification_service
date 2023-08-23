import bcrypt

salt = b'$2b$12$eOm2n5VT3aOPhVN8m5a0.O'
def hash_password(password:str)-> str:
    return bcrypt.hashpw(password.encode(),salt).decode()

