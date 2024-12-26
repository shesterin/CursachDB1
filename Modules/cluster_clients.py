from sklearn.mixture import GaussianMixture
import pandas as pd
import sqlite3

def load_data_from_db(db_path='database.db'):
    # Подключение к базе данных и загрузка данных
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM clients"  # Предполагается, что таблица называется 'clients'
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def cluster_clients(db_path):
    gmm = GaussianMixture(n_components=3, random_state=42)
    gmm.fit(db_path)
    return gmm.predict(db_path)


