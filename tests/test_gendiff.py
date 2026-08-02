import os

from gendiff import generate_diff


def get_fixture_path(file_name):
    return os.path.abspath(os.path.join("tests", "test_data", file_name))


def test_generate_diff_json():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    expected_file = get_fixture_path("expected_flat.txt")
    
    with open(expected_file, "r", encoding="utf-8") as f:
        expected_output = f.read()
    
    assert generate_diff(file1, file2) == expected_output