from .calculos import mdc, soma_digitos
from .erros import EntradaInvalida, OperacaoInvalida


def converter(texto):
    try:
        return int(texto)
    except ValueError as erro:
        raise EntradaInvalida() from erro


def processar(linha):
    partes = linha.split()
    if not partes or partes[0] not in ('M', 'S'):
        raise OperacaoInvalida()
    if partes[0] == 'M':
        if len(partes) != 3:
            raise EntradaInvalida()
        a, b = converter(partes[1]), converter(partes[2])
        if not (1 <= a <= 10**9 and 1 <= b <= 10**9):
            raise EntradaInvalida()
        return f'MDC = {mdc(a, b)}'
    if len(partes) != 2:
        raise EntradaInvalida()
    numero = converter(partes[1])
    if not 0 <= numero <= 10**18:
        raise EntradaInvalida()
    return f'SOMA = {soma_digitos(numero)}'
