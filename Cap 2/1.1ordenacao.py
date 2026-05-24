'''
  Função para encontrar o menor elemento em um array e ordenar o array usando o método de ordenação por seleção.
  O método de ordenação por seleção funciona encontrando o menor elemento em uma parte não ordenada do array e trocando-o com o primeiro elemento dessa parte. 
  O processo é repetido para a parte restante do array até que todo o array esteja ordenado.
'''

def buscaMenor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacaoPorSelecao(arr):
  novo_arr = []
  for i in range(len(arr)):
    menor_indice = buscaMenor(arr)
    novo_arr.append(arr.pop(menor_indice))
  return novo_arr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))
