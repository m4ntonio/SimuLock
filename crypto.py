from pathlib import Path
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

def derivar_chave(senha: bytes, salt: bytes):
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(senha)

def encrypt_file(file_path: Path, senha: bytes):
    salt = os.urandom(16)
    nonce = os.urandom(12)

    chave = derivar_chave(senha, salt)
    aesgcm = AESGCM(chave)

    data = file_path.read_bytes()
    encrypted = aesgcm.encrypt(nonce, data, None)

    new_file = file_path.with_suffix(file_path.suffix + ".locked")
    new_file.write_bytes(salt + nonce + encrypted)

    file_path.unlink()

def decrypt_file(file_path: Path, senha: bytes):
    data = file_path.read_bytes()

    salt = data[:16]
    nonce = data[16:28]
    encrypted = data[28:]

    chave = derivar_chave(senha, salt)
    aesgcm = AESGCM(chave)

    decrypted = aesgcm.decrypt(nonce, encrypted, None)

    original = Path(str(file_path).replace(".locked", ""))
    original.write_bytes(decrypted)

    file_path.unlink()