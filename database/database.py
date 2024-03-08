import csv
from zipfile import ZipFile, ZIP_DEFLATED
import os
import sqlite3
import json


database_name = "dataset_db.db"


def create_database():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS datasets (
        id TEXT PRIMARY KEY,
        data TEXT,
        info TEXT
    )''')
    conn.commit()
    conn.close()


def add_dataset(dataset_id, data, info):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    data_json = json.dumps(data)
    info_json = json.dumps(info)
    cursor.execute('INSERT INTO datasets (id, data, info) VALUES (?, ?, ?)',
                   (dataset_id, data_json, info_json))
    conn.commit()
    conn.close()


def read_dataset(dataset_id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT data, info FROM datasets WHERE id = ?', (dataset_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        data, info = result
        return {"data": json.loads(data), "info": json.loads(info)}
    else:
        return None


def list_dataset_ids():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM datasets')
    dataset_ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return dataset_ids


def transform_data_to_csv_format(data):
    transformed_data = ["time,IR,MIC"]
    for i, time_point in enumerate(data['time']):
        row = f"{time_point},{data['IR'][i]},{data['MIC'][i]}"
        transformed_data.append(row)
    return transformed_data


def save_datasets_as_csv(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('SELECT id, data FROM datasets')
    for dataset_id, data_json in cursor.fetchall():
        csv_file_path = os.path.join(output_folder, f"{dataset_id}.csv")
        if os.path.exists(csv_file_path):
            return
        else:
            data = json.loads(data_json)
            data = transform_data_to_csv_format(data)
            with open(csv_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for line in data:
                    writer.writerow(line.split(','))
    conn.close()



def save_info_as_csv(output_file_path):
    file_path = os.path.join(output_file_path, "results.csv")
    all_info_data = []
    headers = []

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('SELECT info FROM datasets')
    for info_json in cursor.fetchall():
        info = json.loads(info_json[0])
        if not headers:
            headers = list(info.keys())
        all_info_data.append([info.get(header) for header in headers])
    conn.close()
    print()
    os.makedirs(output_file_path, exist_ok=True)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)  # Write the column headers
        writer.writerows(all_info_data)  # Write the rows of data

def create_zip_from_folder(folder_path, zip_file_path):
    with ZipFile(zip_file_path, 'w', ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


def delete_all_data():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM datasets')
    conn.commit()
    conn.close()
    return {"message": "All datasets have been deleted successfully"}


def delete_dataset_id(dataset_id: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM datasets WHERE id = ?', (dataset_id,))
    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    if rows_affected > 0:
        return {"message": "Dataset deleted successfully"}
