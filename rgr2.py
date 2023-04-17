import networkx as nx
import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

def create_weight_matrix(n):
    weight_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            message = f"Введіть вагу ребра ({i+1}, {j+1}): "
            weight = simpledialog.askfloat("Введення ваги", message)
            row.append(weight)
        weight_matrix.append(row)
    return np.array(weight_matrix)

def process_input():
    n = int(size_input.get())
    input_matrix = create_weight_matrix(n)

    row_ind, col_ind = linear_sum_assignment(-input_matrix)

    G = nx.Graph()
    num_rows = input_matrix.shape[0]
    G.add_nodes_from(range(1, num_rows + 1))

    for i in range(num_rows):
        for j in range(num_rows):
            if input_matrix[i, j] != 0:
                G.add_edge(i + 1, j + 1, weight=input_matrix[i, j])

    max_matching_edges = []
    for i in range(len(row_ind)):
        if input_matrix[row_ind[i], col_ind[i]] != 0:
            max_matching_edges.append((row_ind[i] + 1, col_ind[i] + 1))

    max_matching_text.delete("1.0", tk.END)
    max_matching_text.insert(tk.END, ", ".join([f"{u}-{v}" for u, v in max_matching_edges]))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, edgelist=max_matching_edges, node_size=600, with_labels=True, font_size=16, width=2, edge_color='b')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, font_size=16)
    plt.show()


window = tk.Tk()

window.title("Max Matching")

size_label = tk.Label(window, text="Введіть розмірність матриці:")
size_label.grid(row=0, column=0)
size_input = tk.Entry(window, width=5)
size_input.grid(row=0, column=1)

process_button = tk.Button(window, text="Обчислити", command=process_input)
process_button.grid(row=0, column=2)

max_matching_label = tk.Label(window, text="Максимальне паросполучення:")
max_matching_label.grid(row=1, column=0)
max_matching_text = tk.Text(window, width=30, height=10)
max_matching_text.grid(row=1, column=1)
window.mainloop()