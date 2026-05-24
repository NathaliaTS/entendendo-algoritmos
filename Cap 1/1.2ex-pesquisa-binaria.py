"""
  Esse algoritmo calcula o número máximo de etapas necessárias para encontrar um item em uma lista usando a pesquisa binária. 
  A pesquisa binária é um algoritmo eficiente para encontrar um item em uma lista ordenada, 
  e o número máximo de etapas é dado pela fórmula log2(n), onde n é o tamanho da lista. 
  O resultado é arredondado para o número inteiro mais próximo.

  Exercicios":
  1.1 - Número máximo de etapas para encontrar um item em uma lista de 128 elementos. -> 7 etapas
  1.2 - Número máximo de etapas para encontrar um item em uma lista de 236 elementos. -> 8 etapas
"""

import math

tamanho_lista = input("Digite o tamanho da lista: ")
tamanho_lista = int(tamanho_lista)

max_etapas = round(math.log(tamanho_lista, 2))

print("O número máximo de etapas para encontrar um item é: ", max_etapas)
