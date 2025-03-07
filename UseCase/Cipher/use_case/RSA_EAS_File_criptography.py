import json
#from DE_LibCipher import Encrypt_AES, Encrypt_RSA
from Utils import  AES_Cipher, RSA_Cipher

eas = AES_Cipher()
rsa = RSA_Cipher()

rsa.getChavePrivada(2048)
rsa.getChavePublica()

# Lendo arquivo JSON a ser criptografado
fh = open("C:/cloud/OneDrive/Trabalho/Projetos/Python/DATAx/UTIL/UseCase/Cipher/files/base.json", "r")
buf = fh.read()
bufj = json.loads(buf)


encrypted_text = []

# Cipher
for key in bufj:
    base_text = json.dumps(bufj[key], indent=4)
    text = eas.encrypt(plaintext=base_text, rsa_public_key=rsa.PUBLIC_KEY)
    encrypted_text.append(text)
    print(text)

# DesCipher
for index in encrypted_text:
    result = eas.decrypt(encrypted_data=index, rsa_private_key=rsa.PRIVATE_KEY)
    print(result)

#encrypted_text = eas.encrypt(large_text, rsa.PUBLIC_KEY)
#print(encrypted_text)
