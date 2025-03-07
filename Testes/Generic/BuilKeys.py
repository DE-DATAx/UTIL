"""
Gera varias chaves com valores default:
qtd: int = 1,
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

k = gen.build_keys(qtd=5)

print(k)







