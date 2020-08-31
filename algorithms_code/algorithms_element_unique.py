"""
    Problema do conjunto e seus elementos únicos

    Por definição, um conjunto não pode ter elementos repetidos.
    Faça um programa capas de ler um número inteiro N (1 <=N<=1000) e N inteiros K (-1000 <= K <= 1000)

    A saída deverá ser um conjunto formado pelos K inteiros. Os elementos deverão ser exibidos em ordem crescente.
"""

def verifica_n_inteiro(l):
    for e in l:
        if not isinstance(e, int):
            return True
    return False

def unique_elements(l, l_size):
    
    if not isinstance(l_size, int) or verifica_n_inteiro(l):
        return "Os valores devem ser todos inteiros."    


    elif max(l) > 1000 or min(l) < -1000:
        return "Os elementos devem ser maior ou igual à -1000 e menor ou igual à 1000."
    
    elif l_size > 1000 or l_size<1 or len(l) != l_size:
        return "Tamanho de N inválido."
        
    else:
        new_list = []
        """
            For percorre a lista...
            para cada elemento verifica se não se encontra na nova lista...
            
            => caso positivo, o elemento é adicionado a lista..
            => caso negativo, não acontece nada...
        """
        [new_list.append(i) if i not in new_list else None for i in l]
        return sorted(new_list)
