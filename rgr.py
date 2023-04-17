import networkx as nx
import matplotlib.pyplot as plt
import random
import tkinter as tk
import tkinter.messagebox as messagebox


def show_error_message(message):
    messagebox.showerror("Помилка", message)


def create_graph():
    plt.clf() # очищення попереднього графа

    G = nx.Graph()
    # отримання кількості вершин та ребер з полів введення
    try:
        n = int(entry_vertex.get())
        m = int(entry_edge.get())
    except ValueError:
        show_error_message("Неправильний формат введених даних")
        return

    # перевірка коректності введених даних
    if n <= 0 or m <= 0:
        show_error_message("Кількість вершин та ребер повинні бути більше 0")
        return
    if m > n * (n - 1) / 2:
        show_error_message("{} - максимальна кількість ребер для вибраної кількості вершин".format(n * (n - 1) / 2))
        return

    G.add_nodes_from(range(1, n + 1))

    edges_added = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if edges_added >= m:
                break
            G.add_edge(i, j)
            edges_added += 1
        if edges_added >= m:
            break

    print(G.edges())

    matching = nx.max_weight_matching(G)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edges(G, pos, edgelist=matching, edge_color='r')
    plt.show()  # відображаємо граф за допомогою функції show() бібліотеки matplotlib


# створення вікна
root = tk.Tk()
root.title("Створення графа")

# створення поля для введення числа вершин
label_vertex = tk.Label(root, text="Введіть кількість вершин графа:")
label_vertex.pack()
entry_vertex = tk.Entry(root)
entry_vertex.pack()

# створення поля для введення числа ребер
label_edge = tk.Label(root, text="Введіть кількість ребер графа:")
label_edge.pack()
entry_edge = tk.Entry(root)
entry_edge.pack()


def is_valid_probability(entry):
    try:
        value = float(entry)
        if value >= 0 and value <= 1:
            return True
        else:
            return False
    except ValueError:
        return False

# створення кнопки для підтвердження введення
button = tk.Button(root, text="Підтвердити", command=create_graph)
button.pack()

# запуск головного циклу вікна
root.geometry("300x150")
root.mainloop()
