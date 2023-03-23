import datetime


class InformacaodoSistema:

    def __init__(self):
        pass

    @staticmethod
    def retornar_hora():
        now = datetime.datetime.now()
        resposta = f'Sao {now.hour} horas e {now.minute} minutos.'
        return resposta

    @staticmethod
    def retornar_nome():
        nome = 'Alice'
        resposta = f'Meu nome é {nome}, como posso ajudar?'
        return resposta

    @staticmethod
    def retornar_saudacao():
        resposta = f'Olá! Como posso ajudar?'
        return resposta

