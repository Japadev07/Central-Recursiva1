"""As duas operações recursivas."""


def mdc(a: int, b: int) -> int:
    """Calcula o MDC com o algoritmo de Euclides."""
    if b == 0:
        return abs(a)
    return mdc(b, a % b)


def soma_digitos(numero: int) -> int:
    """Soma os dígitos de um inteiro por recursão."""
    numero = abs(numero)
    if numero < 10:
        return numero
    return numero % 10 + soma_digitos(numero // 10)
