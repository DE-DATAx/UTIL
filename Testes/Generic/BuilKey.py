"""
Gera uma chave com valores default:
size: int = 24,
sep: str = "-",
word_length: int = 4,
lower_case: bool = True,
upper_case: bool = True,
digits: bool = True,
hex_digits: bool = False,
oct_digits: bool = False,
special_chars: bool = False,
printable_chars: bool = False,
control_chars: bool = False
"""
from Utils import Generic as G

gen = G.Generic()

k = gen.build_key()

print(k)







