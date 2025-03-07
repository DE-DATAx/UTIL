#import DE_LibCipher as LE
from Utils import RSA_Cipher


rsa = RSA_Cipher()

rsa.getChavePrivada(value_bytes=2048)
rsa.getChavePublica()
filepath = "/Testes/Cipher/files"

rsa.setFileKey(filename=f"{filepath}/private.pem", key=rsa.PRIVATE_KEY)
rsa.setFileKey(filename=f"{filepath}/public.pem", key=rsa.PUBLIC_KEY)

