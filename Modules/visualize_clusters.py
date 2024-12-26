import matplotlib.pyplot as plt
import seaborn as sns


def visualize_clusters(data, labels, folder_path):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data['CreditScore'], y=data['LoanAmount'], hue=labels, palette='viridis')
    plt.title('Кластеризация клиентов по кредитной истории')
    plt.xlabel('Кредитный рейтинг')
    plt.ylabel('Сумма кредита')
    plt.legend(title='Кластер')

    # Сохранение визуализации
    plt.savefig(f'{folder_path}/clusters_visualization.png')

    # Открытие изображения в отдельном окне
    plt.show()  # {{ edit_1 }}
    plt.close()
