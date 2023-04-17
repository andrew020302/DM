import networkx as nx
import numpy as np


n = 5
# Функція, яка перевіряє, чи є графи G1 та G2 ізоморфними
def is_isomorphic(G1, G2):
    return nx.is_isomorphic(G1, G2)

# Ввід графів користувачем
print("Введіть матрицю суміжності графу G1:")
G1 = nx.from_numpy_array(np.array([input().split() for i in range(n)], dtype=int))

print("Введіть матрицю суміжності графу G2:")
G2 = nx.from_numpy_array(np.array([input().split() for i in range(n)], dtype=int))

# Перевірка ізоморфізму графів
if is_isomorphic(G1, G2):
    print("Графи G1 та G2 є ізоморфними")
else:
    print("Графи G1 та G2 не є ізоморфними")
