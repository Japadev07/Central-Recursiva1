import sys


class OperacaoInvalida(Exception):
    pass


class EntradaInvalida(Exception):
    pass


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def soma_digitos(numero):
    if numero < 10:
        return numero
    return numero % 10 + soma_digitos(numero // 10)


def converter(texto):
    try:
        return int(texto)
    except ValueError as erro:
        raise EntradaInvalida() from erro


def processar(linha):
    partes = linha.split()

    if not partes or partes[0] not in ("M", "S"):
        raise OperacaoInvalida()

    if partes[0] == "M":
        if len(partes) != 3:
            raise EntradaInvalida()

        a = converter(partes[1])
        b = converter(partes[2])

        if a <= 0 or b <= 0:
            raise EntradaInvalida()

        return f"MDC = {mdc(a, b)}"

    if len(partes) != 2:
        raise EntradaInvalida()

    numero = converter(partes[1])

    if numero < 0:
        raise EntradaInvalida()

    return f"SOMA = {soma_digitos(numero)}"


def main():
    linhas = sys.stdin.read().splitlines()

    if not linhas:
        return

    try:
        quantidade = int(linhas[0].strip())
    except ValueError:
        print("ERRO: EntradaInvalida")
        return

    if not 1 <= quantidade <= 100:
        print("ERRO: EntradaInvalida")
        return

    resultados = []

    for indice in range(quantidade):
        linha = linhas[indice + 1] if indice + 1 < len(linhas) else ""

        try:
            resultado = processar(linha)
        except OperacaoInvalida:
            resultado = "ERRO: OperacaoInvalida"
        except EntradaInvalida:
            resultado = "ERRO: EntradaInvalida"
        finally:
            resultados.append(resultado)

    print("\n".join(resultados))


if __name__ == "__main__":
    main()
