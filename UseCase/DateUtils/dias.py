from Utils import DateUtils as DU
import datetime as dt

now = dt.datetime.now()

du = DU.DateUtils()

primeirodiaano = du.getPrimeiroDiaAno(now)
print("primeiro dia do ano: ",primeirodiaano)

ultimodia = du.getUltimoDiaAno(now)
print("ultimo dia do ano: ",ultimodia)

primeirodiasemestre = du.getPrimeiroDiaSemestre(now)
print("primeiro dia do semestre: ",primeirodiasemestre)

ultimodiasemestre = du.getUltimoDiaSemestre(now)
print("ultimo dia do semestre: ",ultimodiasemestre)

primeirodiames = du.getPrimeiroDiaMes(now)
print("primeiro dia do mes: ", primeirodiames)

ultimodiames = du.getUltimoDiaMes(now)
print("ultimo dia do mes: ", ultimodiames)

primeirodiaquinzena = du.getPrimeiroDiaQuinzena(now)
print("primeiro dia da quizena: ", primeirodiaquinzena)

ultimodiaquinzena = du.getUltimoDiaQuinzena(now)
print("Ultimo dia da quizena: ", ultimodiaquinzena)

primeirahoradia = du.getPrimeiraHoraDia(now)
print("primeira hora do dia: ", primeirahoradia)

ultimahoradia = du.getUltimaHoraDia(now)
print("ultima hora do dia: ", ultimahoradia)