from Utils import Generic as G

gen = G.Generic()

string = 'Palavra de teste para pesquisa'
patterns = "de"


x = gen.findchar(string=string, pattern=patterns, ocorrencia=1)

print(x)