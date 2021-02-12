"""
Delta data hora

delta = data_final - data_inicial

import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2021, 8, 6, 0)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento), repr(tempo_para_evento), tempo_para_evento)

print(f"Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 360} horas para o evento.")

data_compra = datetime.datetime.now()

regra_boleto = datetime.timedelta(days=5)

vencimento_boleto = data_compra + regra_boleto

print(vencimento_boleto)

"""
