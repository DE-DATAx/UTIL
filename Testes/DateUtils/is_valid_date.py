from Utils import DateUtils as DT, Generic as G
import datetime as dt

du = DT.DateUtils()
g = G.Generic()

data = dt.datetime.now().strftime(du.DATETIME_FORMAT_PYTHON)
x = du.is_valid_date(data, du.DATETIME_FORMAT_PYTHON)
print(f"""A data "{data}", é {g.iif(x, "Verdadeira", "Falsa")}""")

data = "2025-02-29"
x = du.is_valid_date(data, du.DATE_FORMAT_PYTHON)
print(f"""A data "{data}", é {g.iif(x, "Verdadeira", "Falsa")}""")

data = "2024-02-29"
x = du.is_valid_date(data, du.DATE_FORMAT_PYTHON)
print(f"""A data "{data}", é {g.iif(x, "Verdadeira", "Falsa")}""")

