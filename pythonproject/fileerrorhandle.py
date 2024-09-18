import pandas as pd

def append_to_csv(file_name, data_frame):
    try:
        data_frame.to_csv(file_name, mode='a', header=not pd.io.common.file_exists(file_name), index=False)
    except Exception as e:
        print(f"An error occurred while updating {file_name}: {e}")

def read_from_csv(file_name):
    try:
        data_frame = pd.read_csv(file_name)
        return data_frame
    except (FileNotFoundError, pd.errors.EmptyDataError):
        raise ValueError(f"{file_name} not found or empty")
          
        