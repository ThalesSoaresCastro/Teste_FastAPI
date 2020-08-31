from API.algorithms_code import algorithms_element_unique as algorithms

#import algorithms_element_unique as algorithms

"""
    Problema do conjunto e seus elementos únicos

    Por definição, um conjunto não pode ter elementos repetidos.
    Faça um programa capas de ler um número inteiro N (1 <=N<=1000) e N inteiros K (-1000 <= K <= 1000)

    A saída deverá ser um conjunto formado pelos K inteiros. Os elementos deverão ser exibidos em ordem crescente.

    Testes:
    1 - Exemplo 1.
    2 - Exemplo 2.
    3 - Exemplo 3.
    4 - N > 1000.
    5 - N < 1.
    6 - k > 1000.
    7 - k < -1000.
    8 - Quantidade de elementos da lista diferente do valor de N.
    9 - N não é inteiro.
    10 - Algum elemento da lista não é inteiro. 
"""
def test_algorithms_exe1():
    l = [10,10,9,9,8,8,7,7,6,6]
    result_l = [6,7,8,9,10]
    size_l = 10
    assert result_l == algorithms.unique_elements(l, size_l)

def test_algorithms_exe2():
    l=[-1, -1, -1, -1, -1]
    result_l = [-1]
    size_l=5
    assert result_l == algorithms.unique_elements(l, size_l)

def test_algorithms_exe3():
    l = [-123, 123, 999, 1000, -1000]
    result_l = [-1000, -123, 123, 999, 1000]
    size_l = 5
    assert result_l == algorithms.unique_elements(l, size_l)

#tratamento de erros...
def test_algorithms_error_tamanho_N_maior():
    l = [-123, 123, 999, 1000]
    result_l = "Tamanho de N inválido."
    size_l= 1001
    assert result_l == algorithms.unique_elements(l, size_l)

def test_algorithms_error_tamanho_N_menor():
    l = [-123, 123, 999, 1000]
    result_l = "Tamanho de N inválido."
    size_l= -4
    assert result_l == algorithms.unique_elements(l, size_l)


def test_algorithms_error_elemento_K_maior():
    l = [-123, 123, 999, 10000]
    result_l = "Os elementos devem ser maior ou igual à -1000 e menor ou igual à 1000."
    size_l= 4
    assert result_l == algorithms.unique_elements(l, size_l)


def test_algorithms_error_elemento_K_menor():
    l = [-123, 123, 999, -10000]
    result_l = "Os elementos devem ser maior ou igual à -1000 e menor ou igual à 1000."
    size_l= 4
    assert result_l == algorithms.unique_elements(l, size_l)

def test_algorithms_error_qte_lista_diferente_size():
    l = [-123, 123, 999, 1000]
    result_l = "Tamanho de N inválido."
    size_l= 10
    assert result_l == algorithms.unique_elements(l, size_l)

def test_algorithms_N_naoehInteiro():
    l = [-123, 123, 999, 1000]
    result_l = "Os valores devem ser todos inteiros."
    size_l= 3.4
    assert result_l == algorithms.unique_elements(l, size_l)

def test_algorithms_K_naoehInteiro():
    l = [-123, 123, 999, 4.5]
    result_l = "Os valores devem ser todos inteiros."
    size_l= 4
    assert result_l == algorithms.unique_elements(l, size_l)
