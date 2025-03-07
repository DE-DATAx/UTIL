from crypto.Cipher import PKCS1_OAEP
from crypto.PublicKey import RSA

# Carregar a chave privada do arquivo
with open("chave_privada.pem", "rb") as f:
    chave_privada = RSA.import_key(f.read())

mensagem_criptografada="5f831b6e4723ee2af603098f62c4d580e932dafb7a6b84d29a7d2e5aaca4c6b91d0f77328f455a4ac5e04fe31090fae07a17d8098847a89ed822f68881a640b6917647574d4b5f30713629910d124055c8afde97f5a81f118b43cd312476cbe3f05aee501a3c5f91024fd1344d426f3b7c64ea37e3b26c49d41fd19aba50ce14171bee73a6440fc1c2d0e2df82a73897720b858d16eaae74e3c0126968039e3588c2c40bb7aeb9aae832a0263638c5e8bd277e2d80cfcb2c7ec68131dc9e7971c4049cd899adb7386bdcadbe4608c59c9014bb4671ec6bf96c208f57560bf8b74ae72512d830fb821c5997046b46a0951eb12a1fa96d14051d8bc07b68d6928a"

# Criar um objeto de descriptografia
decifra = PKCS1_OAEP.new(chave_privada)

# Descriptografar a mensagem
mensagem_original = decifra.decrypt(bytes.fromhex(mensagem_criptografada))

print("Mensagem descriptografada:", mensagem_original.decode())
