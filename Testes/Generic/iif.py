from Utils import Generic as G

gen = G.Generic()

x = gen.iif((1==1), "a", "b")
print(x)

x = gen.iif(("a" in "a"), "x", "z")
print(x)

x = gen.iif((1!=1), "k", "j")
print(x)

x = gen.iif((10/2==1), "1", 10/2)
print(x)