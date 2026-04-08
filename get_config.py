import os

def get_config(app_const, dir_name, file_name):
    BASE_PATH = app_const['BASE_PATH']
    file_path = BASE_PATH + dir_name + file_name
    
    if not os.path.exists(file_path):
        print(f"Config file not found at {file_path}.")
        raise FileNotFoundError(f"Config file not found: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            news_config = f.read()
    except Exception as e:
        print(f"Failed to read config file at {file_path}: {e}")
        raise RuntimeError(f"Failed to read config file: {e}")
    
    success_msg = f"Successfully retrieved config from {file_path}."
    print(success_msg)
    return {"data": news_config, "message": success_msg}
    
    
if __name__ == "__main__":
    get_config()