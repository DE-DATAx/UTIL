from Utils import Generic as G

gen = G.Generic()

x = gen.cores_ansi()

print(f"""Este texto {x["Vermelho"][0]}sera impresso em vermelho, e {x["Amarelo"][0]}este outro em Amarelo""")