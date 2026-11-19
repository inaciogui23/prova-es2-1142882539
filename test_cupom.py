from cupom import desconto_valido


def test_aceita_percentual_exatamente_no_limite():
    percentual = 29

    resultado = desconto_valido(percentual)

    assert resultado is True


def test_rejeita_percentual_um_acima_do_limite():
    percentual = 30

    resultado = desconto_valido(percentual)

    assert resultado is False


def test_rejeita_percentual_zero():
    percentual = 0

    resultado = desconto_valido(percentual)

    assert resultado is False


def test_rejeita_percentual_fracionario_dentro_da_faixa():
    percentual = 28.5

    resultado = desconto_valido(percentual)

    assert resultado is False
