import tkinter as tk
from tkinter import scrolledtext
from Modules.generate_dataset import generate_dataset_csv
from Modules.cluster_clients import cluster_clients
from Modules.visualize_clusters import visualize_clusters


def run_program():
    # Генерация датасета
    folder_path, dataset = generate_dataset_csv()
    output_text.insert(tk.END, "Датасет сгенерирован.\n")

    # Кластеризация клиентов
    labels = cluster_clients(dataset)
    output_text.insert(tk.END, "Клиенты кластеризованы.\n")

    # Визуализация кластеров
    visualize_clusters(dataset, labels, folder_path)
    output_text.insert(tk.END, "Кластеры визуализированы.\n")


def main():
    # Создание основного окна
    window = tk.Tk()
    window.title("Кластеризация клиентов")

    # Создание кнопки для запуска программы
    run_button = tk.Button(window, text="Запустить", command=run_program)
    run_button.pack(pady=10)

    # Создание текстового поля для вывода результатов
    global output_text
    output_text = scrolledtext.ScrolledText(window, width=50, height=20)
    output_text.pack(pady=10)

    # Запуск основного цикла
    window.mainloop()


if __name__ == "__main__":
    main()
