import hashlib
import string
from random import choice
import random as rd
import re


class Generic:
    def __init__(self):
        #print('teste')
        pass

    @staticmethod
    def findchar(string: str, pattern: str, ocorrencia: int = None, inicio: int = 0, fim: int = 0, trim: bool = True):
        try:
            if trim:
                string = string.strip()
            if fim == 0:
                fim = len(string)
            if fim > inicio and (fim-inicio) > len(pattern):
                string = string[inicio:fim]
            if ocorrencia is not None:
                locate = re.findall(pattern, string)
                if ocorrencia is not None:
                    if ocorrencia > len(locate):
                        locate = locate[len(locate)-1]


        except Exception as error:
            locate = error
        finally:
            return locate


    @staticmethod
    def build_key(size: int = 24,
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
                  ) -> str:
        index = 1
        key = ""
        literal = ""
        if lower_case:
            literal = literal + string.ascii_lowercase
        if upper_case:
            literal = literal + string.ascii_uppercase
        if digits:
            literal = literal + string.digits
        if hex_digits:
            literal = literal + string.hexdigits
        if oct_digits:
            literal = literal + string.octdigits
        if special_chars:
            literal = literal + string.punctuation
        if printable_chars:
            literal = literal + string.printable
        if control_chars:
            literal = literal + string.whitespace
        try:
            for i in range(size):
                letra = choice(literal)
                if index == word_length and i < size - 1:
                    key += letra + sep
                    index = 1
                else:
                    key += letra
                    index += 1
        except Exception as error:
            key = f"Impossivel gerar uma chave. Erro: {error}"
        return key

    @staticmethod
    def build_keys(qtd: int = 1,
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
                   control_chars: bool = False) -> list:
        keys = []
        for index in range(qtd):
            k = Generic.build_key(size=size,
                              sep=sep,
                              word_length=word_length,
                              lower_case=lower_case,
                              upper_case=upper_case,
                              digits=digits,
                              hex_digits=hex_digits,
                              oct_digits=oct_digits,
                              special_chars=special_chars,
                              printable_chars=printable_chars,
                              control_chars=control_chars
                              )
            keys.append(k)
        return keys

    @staticmethod
    def hash(word: str, pattern: str = "md5"):
        pattern_list = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
        h, msg, error = None, None, None
        try:
            #value /= b'{word}'/
            if pattern == pattern_list[0]:
                h = hashlib.md5()
            elif pattern == pattern_list[1]:
                h = hashlib.sha1()
            elif pattern == pattern_list[2]:
                h = hashlib.sha224()
            elif pattern == pattern_list[3]:
                h = hashlib.sha256()
            elif pattern == pattern_list[4]:
                h = hashlib.sha384()
            elif pattern == pattern_list[5]:
                h = hashlib.sha512()
            h.update(word.encode())
            msg = h.hexdigest()
        except Exception as error:
            msg = f"""Erro ao tentar montar o HASH. Erro: {error}"""
        finally:
            return msg

    @staticmethod
    def ifnull(var, val):
        if (var is None or var == 'None'):
            value = val
        else:
            value = var
        return value

    @staticmethod
    def iif(condicao: bool, value_true, value_false):
        if condicao:
            value = value_true
        else:
            value = value_false
        return value

    @staticmethod
    def nvl(value, default):
        msg, result = None, None
        try:
            if (value is not None):
                result = value
            else:
                result = default
            return result
        except Exception as error:
            msg = error
            result = msg
        finally:
            return result

    @staticmethod
    def cores_ansi() -> dict:
        cores = {"Preto": ["\033[1;30m", "\033[1;40m"],
                 "Vermelho": ["\033[1;31m", "\033[1;41m"],
                 "Verde": ["\033[1;32m", "\033[1;42m"],
                 "Amarelo": ["\033[1;33m", "\033[1;43m"],
                 "Azul": ["\033[1;34m", "\033[1;44m"],
                 "Magenta": ["\033[1;35m", "\033[1;45m"],
                 "Cyan": ["\033[1;36m", "\033[1;46m"],
                 "Cinza Claro": ["\033[1;37m", "\033[1;47m"],
                 "Cinza Escuro": ["\033[1;90m", "\033[1;100m"],
                 "Vermelho Claro": ["\033[1;91m", "\033[1;101m"],
                 "Verde Claro": ["\033[1;92m", "\033[1;102m"],
                 "Amarelo Claro": ["\033[1;93m", "\033[1;103m"],
                 "Azul Claro": ["\033[1;94m", "\033[1;104m"],
                 "Magenta Claro": ["\033[1;95m", "\033[1;105m"],
                 "Cyan Claro": ["\033[1;96m", "\033[1;106m"],
                 "Branco": ["\033[1;97m", "\033[1;107m"],
                 "Negrito": ["\033[;1m", None],
                 "Inverte": ["\033[;7m", None],
                 "Reset (remove formatação)": ["\033[0;0m", None]}
        return cores

    @staticmethod
    def random_generator(size: int = 6, chars: str = string.ascii_uppercase + string.digits):
        value = ''.join(rd.choice(chars) for _ in range(size))
        return value

    def is_valid_int(self, value):
        msg, result = None, True
        try:
            int(value)
        except Exception as error:
            msg = error
            result = False
        finally:
            return result

    def is_valid_float(self, value):
        msg, result = None, True
        try:
            float(value)
        except Exception as error:
            msg = error
            result = False
        finally:
            return result

    def is_valid_type(self, value, type, default_value, format=None):
        msg, result = None, None
        try:
            if type.upper() == 'DATE':
                default_value = dt.datetime.strptime(value, format)
            elif type.upper() == 'INT':
                default_value = int(value)
            elif type.upper() == "FLOAT":
                default_value = float(value)
            else:
                raise Exception
            result = default_value
        except Exception as error:
            msg = error
            result = msg
        finally:
            return result

    def calcular_formula(self, formula: str, variaveis):
        msg, result = None, None
        try:
            result = eval(formula, {}, variaveis)
        except Exception as error:
            msg = error
            result = msg
        finally:
            return result
