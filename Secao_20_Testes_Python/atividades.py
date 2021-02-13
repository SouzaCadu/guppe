

def comer(comida, saudavel):
    if saudavel:
        final = "porque é saudável."
    else:
        final = "porque só se vive uma vez."
    return f"Estou comendo {comida} {final}"


def dormir(num_horas):
    if num_horas < 8:
        return "Estou cansando, porque dormi pouco."
    return "Estou atraso para o trabalho, dormi demais."


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False
