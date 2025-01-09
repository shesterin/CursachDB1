import pandas as pd
import numpy as np
import sqlite3
import os
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

def generate_dataset_csv(num_samples=200):
    # Генерация случайных данных
    data = {
        'ClientID': range(1, num_samples + 1),
        'CreditScore': np.random.randint(300, 850, size=num_samples),
        'DebtToIncomeRatio': np.random.uniform(0, 1, size=num_samples),
        'LoanAmount': np.random.randint(1000, 50000, size=num_samples)
    }
    df = pd.DataFrame(data)

    # Создание папки с временным штампом
    timestamp = datetime.now().strftime("%Y/%m/%d/%H_%M_%S")
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


class TestGenerateDatasetCSV(unittest.TestCase):

    @patch('os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    @patch('sqlite3.connect')
    def test_generate_dataset_csv(self, mock_connect, mock_to_csv, mock_makedirs):
        # Настройка
        mock_connect.return_value = MagicMock()

        # Вызов функции
        folder_path, df = generate_dataset_csv(10)

        # Проверка создания папки
        self.assertTrue(mock_makedirs.called)

        # Проверка сохранения CSV
        self.assertTrue(mock_to_csv.called)

        # Проверка подключения к базе данных
        mock_connect.assert_called_once_with(f'{folder_path}/database.db')

        # Проверка, что данные сохранены в базу данных
        mock_connect.return_value.__enter__.return_value.to_sql.assert_called_once_with('Dataset',
                                                                                        mock_connect.return_value.__enter__(),
                                                                                        if_exists='replace',
                                                                                        index=False)

        # Проверка структуры данных
        self.assertEqual(len(df), 10)
        self.assertIn('ClientID', df.columns)
        self.assertIn('CreditScore', df.columns)
        self.assertIn('DebtToIncomeRatio', df.columns)
        self.assertIn('LoanAmount', df.columns)


if __name__ == '__main__':
    unittest.main()