"""
Gera um HASH CODE baseado em uma palavra
word: str
pattern: str = "md5"

padoes permitidos:
["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
default=MD5
"""
from Utils import Generic as G

word = "PALAVRA TESTE"

gen = G.Generic()

__hash = gen.hash(word=word, pattern="md5")

print(__hash)

