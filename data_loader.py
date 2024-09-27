import pandas as pd
import numpy as np
import os

def load_network_data(file_path):
   
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"Error: An error occurred while parsing the file {file_path}: {e}")
        return pd.DataFrame()

def load_log_data(file_path):

    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
        logs = [log.strip() for log in logs]
        return logs
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error: An error occurred while loading the file {file_path}: {e}")
        return []

def load_data(file_path, data_type):

    if data_type == 'network':
        return load_network_data(file_path)
    elif data_type == 'log':
        return load_log_data(file_path)
    else:
        print(f"Error: Unsupported data type {data_type}.")
        return pd.DataFrame() if data_type == 'network' else []

def save_data(data, file_path, data_type):

    if data_type == 'network':
        data.to_csv(file_path, index=False)
    elif data_type == 'log':
        with open(file_path, 'w') as file:
            for log in data:
                file.write(log + '\n')
    else:
        print(f"Error: Unsupported data type {data_type}.")

def check_file_exists(file_path):
  
    return os.path.exists(file_path)

def check_file_empty(file_path):

    return os.path.getsize(file_path) == 0