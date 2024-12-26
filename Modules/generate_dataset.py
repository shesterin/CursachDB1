import pandas as pd
import numpy as np
import csv, sqlite3
import os
from datetime import datetime

def generate_dataset_csv(num_samples=100):
    # Генерация случайных данных
    data = {
        'ClientID': range(1, num_samples + 1),
        'CreditScore': np.random.randint(300, 850, size=num_samples),
        'DebtToIncomeRatio': np.random.uniform(0, 1, size=num_samples),
        'LoanAmount': np.random.randint(1000, 50000, size=num_samples)
    }
    df = pd.DataFrame(data)

    # Создание папки с временным штампом
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_path = f'Results/{timestamp}'
    os.makedirs(folder_path, exist_ok=True)

    # Сохранение датасета в CSV
    csv_file_path = f'{folder_path}/dataset.csv'
    df.to_csv(csv_file_path, index=False)

    # Подключение к базе данных SQLite
    conn = sqlite3.connect(f'{folder_path}/database.db')
    df.to_sql('Dataset', conn, if_exists='replace', index=False)
    conn.close()

    return folder_path, df
