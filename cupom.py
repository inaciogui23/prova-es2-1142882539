MAXIMO = 29


def desconto_valido(percentual):
    if type(percentual) is not int:
        return False
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
