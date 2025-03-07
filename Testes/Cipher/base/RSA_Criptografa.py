from crypto.Cipher import PKCS1_OAEP
from crypto.PublicKey import RSA

# Carregar a chave pública do arquivo
with open("chave_publica.pem", "rb") as f:
    chave_publica = RSA.import_key(f.read())

# Criar um objeto de criptografia com RSA
cifra = PKCS1_OAEP.new(chave_publica)

# Mensagem a ser criptografada
mensagem = "Segredo super seguro!"
mensagem_criptografada = cifra.encrypt(mensagem.encode())
print(mensagem_criptografada)

print(f"{type(mensagem_criptografada)} - Mensagem criptografada:", mensagem_criptografada.hex())
