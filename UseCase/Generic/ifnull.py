from Utils import Generic as G

gen = G.Generic()

x = gen.ifnull(None, "21341")
print(x)

x = gen.ifnull('None', "1111")
print(x)

x = gen.ifnull('abc', "21341")
print(x)

x = gen.ifnull('blablabla', "21341")
print(x)