import os

from gendiff.parser import parse


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def get_file_data(file_path):
    abs_path = os.path.abspath(file_path)
    project_root = os.path.abspath(os.getcwd())
    
    try:
        common_path = os.path.commonpath([project_root, abs_path])        
        if common_path != project_root:
            raise PermissionError("Access denied: File is outside the project directory.")
    except ValueError:
        raise PermissionError("Access denied: Invalid file path.")
    
    _, extension = os.path.splitext(abs_path)
    format_name = extension.strip(".").lower()
    
    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    return parse(content, format_name)


def generate_diff(file_path1, file_path2):
    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)

    all_keys = sorted(data1.keys() | data2.keys())
    
    lines = ["{"]
    
    for key in all_keys:
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {to_str(data1[key])}")            
        elif key not in data1 and key in data2:
            lines.append(f"  + {key}: {to_str(data2[key])}")            
        elif data1[key] != data2[key]:
            lines.append(f"  - {key}: {to_str(data1[key])}")
            lines.append(f"  + {key}: {to_str(data2[key])}")
        else:
            lines.append(f"    {key}: {to_str(data1[key])}")
    
    lines.append("}")
    
    return "\n".join(lines)