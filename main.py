import os
from Modules.generate_dataset import generate_dataset_csv
from Modules.cluster_clients import cluster_clients
from Modules.visualize_clusters import visualize_clusters


def main():
    # Генерация датасета
    folder_path, dataset = generate_dataset_csv()

    # Кластеризация клиентов
    labels = cluster_clients(dataset)

    # Визуализация кластеров
    visualize_clusters(dataset, labels, folder_path)


if __name__ == "__main__":
    main()
