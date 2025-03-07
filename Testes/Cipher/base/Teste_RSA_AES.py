from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_large_text(plaintext, rsa_public_key):
    # Gerar uma chave AES aleatória (16 bytes)
    aes_key = get_random_bytes(16)

    # Criar cifra AES em modo CBC
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher_aes.iv  # Vetor de Inicialização

    # Adicionar padding ao texto para que seja múltiplo de 16
    ciphertext = cipher_aes.encrypt(pad(plaintext.encode(), AES.block_size))

    # Criptografar a chave AES com RSA
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # Retornar base64 para fácil armazenamento
    return base64.b64encode(encrypted_aes_key + iv + ciphertext).decode()

def decrypt_large_text(encrypted_data, rsa_private_key):
    # Converter de base64 para bytes
    encrypted_data = base64.b64decode(encrypted_data)

    # Extrair partes (chave AES criptografada + IV + texto criptografado)
    key_size = rsa_private_key.size_in_bytes()
    encrypted_aes_key = encrypted_data[:key_size]
    iv = encrypted_data[key_size:key_size + 16]
    ciphertext = encrypted_data[key_size + 16:]

    # Descriptografar a chave AES com RSA
    cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Descriptografar o texto com AES
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher_aes.decrypt(ciphertext), AES.block_size)

    return plaintext.decode()

# Gerar chaves RSA
rsa_key = RSA.generate(2048)
public_key = rsa_key.publickey()
private_key = rsa_key

# Texto grande para criptografar (> 4000 bytes)
large_text = "Este é um texto muito longo... " * 500  # Repetindo para ter mais de 4000 bytes

# Criptografar
encrypted_text = encrypt_large_text(large_text, public_key)
print("🔒 Texto criptografado:", encrypted_text[:100] + "...")  # Exibir só o começo

# Descriptografar
decrypted_text = decrypt_large_text(encrypted_text, private_key)
print("\n🔓 Texto descriptografado:", decrypted_text[:100] + "...")  # Exibir só o começo
