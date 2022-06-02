# Utilizando a biblioteca numpy para resolver o Desafio 1 - Algoritmo Peak Finding

import numpy as np

a = np.array([[1, 2, 3, 0, 0],
             [2, 3, 1, 0, 0],
             [3, 2, 1, 0, 0],
             [1, 2, 3, 1, 5]])

print("Listas: ")
print(a)

req_index = np.argmax(a, axis=1)
print("\nMaiores indices de cada lista: ")
print(req_index)
