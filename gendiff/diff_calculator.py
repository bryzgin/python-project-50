import os

from gendiff.parser import parse
from gendiff.tree_builder import build_diff_tree
from gendiff.formatters.stylish import render_stylish


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def safe_path(path):
    resolved = os.path.realpath(path)
    base_dir = os.path.realpath(os.getcwd())

    if resolved != base_dir and not resolved.startswith(base_dir + os.sep):
        raise PermissionError(f"Path {path} is outside the allowed directory.")
    return resolved


def get_file_data(file_path):
    abs_path = safe_path(file_path)

    if not os.path.isfile(abs_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    _, extension = os.path.splitext(abs_path)
    format_name = extension.strip(".").lower()

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    return parse(content, format_name)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)

    diff_tree = build_diff_tree(data1, data2)
    
    if format_name == "stylish":
        return render_stylish(diff_tree)
    
    raise ValueError(f"Unknown format: {format_name}")
