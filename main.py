import sys
from central_recursiva.erros import EntradaInvalida, OperacaoInvalida
from central_recursiva.processamento import processar


def main():
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return
    try:
        quantidade = int(linhas[0].strip())
    except ValueError:
        print('ERRO: EntradaInvalida')
        return
    if not 1 <= quantidade <= 100:
        print('ERRO: EntradaInvalida')
        return
    resultados = []
    for indice in range(quantidade):
        linha = linhas[indice + 1] if indice + 1 < len(linhas) else ''
        try:
            resultado = processar(linha)
        except OperacaoInvalida:
            resultado = 'ERRO: OperacaoInvalida'
        except EntradaInvalida:
            resultado = 'ERRO: EntradaInvalida'
        finally:
            resultados.append(resultado)
    print('\n'.join(resultados))


if __name__ == '__main__':
    main()
