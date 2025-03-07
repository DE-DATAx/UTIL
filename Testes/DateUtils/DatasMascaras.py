from Utils import DateUtils as DU

du = DU.DateUtils()

print("Formato da data no SQL: ", du.DATE_FORMAT_SQL)
print("Formato da data e hora no SQL (milisegundos): ", du.MILLISECONDS_FORMAT_SQL)
print("Formato da data e hora no SQL: ", du.DATETIME_FORMAT_SQL)
print("Formato da hora no SQL: ", du.TIME_FORMAT_SQL)
print("-"*100)
print("Formato da data no PYTHON: ", du.DATE_FORMAT_PYTHON)
print("Formato da data e hora no PYTHON (milisegundos): ", du.MILLISECONDS_FORMAT_PYTHON)
print("Formato da data e hora no PYTHON: ", du.DATETIME_FORMAT_PYTHON)
print("Formato da hora no PYTHON: ", du.TIME_FORMAT_PYTHON)