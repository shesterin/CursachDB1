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
    df.to_csv(f'{folder_path}/dataset.csv', index=False)

    #con = sqlite3.connect(f'{timestamp}dataset.db')
    #cur = con.cursor()
    #cur.execute("""CREATE TABLE clients(
    #     ClientID INTEGER NOT NULL,
    #     CreditScore INTEGER NOT NULL,
    #     DebtToIncomeRatio INTEGER NOT NULL,
    #     LoanAmount INTEGER NOT NULL
    # );""")

    #with open(f'{folder_path}/dataset.csv', 'r', encoding="utf8") as f:
    #    dr = csv.DictReader(f, delimiter=",")
    #    to_db = [(i['ClientID'], i['CreditScore'], i['DebtToIncomeRatio'], i['LoanAmount']) for i in dr]

    #cur.executemany("INSERT INTO BD (ClientID, CreditScore, DebtToIncomeRatio, LoanAmount) VALUES (?, ?, ?);", to_db)
    #con.commit()
    #con.close()

    return folder_path, df


