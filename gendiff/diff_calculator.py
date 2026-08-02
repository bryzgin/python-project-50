import json
import os


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file_path1, file_path2):
    abs_path1 = os.path.abspath(file_path1)
    abs_path2 = os.path.abspath(file_path2)
    
    with open(abs_path1, "r") as f1:
        data1 = json.load(f1)
    
    with open(abs_path2, "r") as f2:
        data2 = json.load(f2)
    
    all_keys = sorted(list(data1.keys() | data2.keys()))
    
    lines = ["{"]
    
    for key in all_keys:
        if key in data1 and key in data2:
            lines.append(f" - {key}: {to_str(data1[key])}")        
        elif key not in data1 and key in data2:
            lines.append(f" - {key}: {to_str(data1[key])}")
            lines.append(f" + {key}: {to_str(data2[key])}")        
        else:
            lines.append(f"   {key}: {to_str(data1[key])}")
    
    lines.append("}")
    
    return "\n".join(lines)