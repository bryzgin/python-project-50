import json
import os


def generate_diff(file_path1, file_path2):
    abs_path1 = os.path.abspath(file_path1)
    abs_path2 = os.path.abspath(file_path2)
    
    with open(abs_path1, "r") as f1:
        data1 = json.load(f1)
    
    with open(abs_path2, "r") as f2:
        data2 = json.load(f2)
    
    print("Файл 1 распарсен:", data1)
    print("Файл 2 распарсен:", data2)
    
    return ""