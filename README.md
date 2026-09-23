# Central Recursiva

## Integrantes

- Everton Felipe Cirqueira da Silva
## Descrição

Programa Python que calcula o MDC de dois inteiros positivos e a soma dos dígitos de um inteiro não negativo, conforme o problema CentralRecursivaRobusta.

## Execução

Com Python 3 instalado, na pasta do projeto execute `python main.py < entrada.txt` (no Windows, também pode usar `py main.py < entrada.txt`). O arquivo `entrada.txt` começa com Q e contém Q operações nas linhas seguintes. Para submeter no beecrowd, copie todo o conteúdo de `submissao_beecrowd.py` e selecione Python 3.

## Módulos

- `main.py`: lê Q operações, trata erros com `try`, `except` e `finally` e imprime os resultados.
- `central_recursiva/__init__.py`: identifica o pacote Python.
- `central_recursiva/calculos.py`: funções recursivas.
- `central_recursiva/processamento.py`: valida os dados e seleciona a operação.
- `central_recursiva/erros.py`: exceções personalizadas.
- `submissao_beecrowd.py`: versão de arquivo único para o avaliador.

## Algoritmos recursivos

O MDC usa o algoritmo de Euclides: `mdc(a, b)` chama `mdc(b, a % b)` até `b == 0`. A soma dos dígitos separa o último dígito com `% 10`, remove-o com `// 10` e repete até restar um único dígito.

## Exceções personalizadas

`OperacaoInvalida` representa um código diferente de M e S. `EntradaInvalida` representa números não inteiros, quantidade incorreta de argumentos ou valores fora dos limites. Ambas herdam de `Exception`.
