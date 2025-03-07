import os

class SO:
    def __init__(self):
        ...

    @staticmethod
    def ping(hostname):
        # hostname = "google.com"  # example
        response = os.system("ping -n 1 " + hostname + " >> trash_ping.log")
        # and then check the response...
        if response == 0:
            result = f"""{hostname} Sucesso!"""
        else:
            result = f"""{hostname} Não encontrado!"""
        return result

    @staticmethod
    def getPID():
        return os.getpid()

    @staticmethod
    def killPID(pid):
        result = True
        try:
            os.kill(pid, signal.SIGKILL)
        except Exception as error:
            result = False
        finally:
            return result