from Utils import RSA_Cipher

rsa = RSA_Cipher()

__path = "../files"
__word = "Palavra curta para criptografia o seu teste"
print("Palavra a ser criptografada: ", __word)

rsa.setInit(path=__path, word=__word)

__cipher = rsa.CIPHER(word=__word)
print("Criptofragrando: ", __cipher)
__deCipher = rsa.CIPHER(word=__cipher, action="D")
print("Descriptografando: ", __deCipher.decode())