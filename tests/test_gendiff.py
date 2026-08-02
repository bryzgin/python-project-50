import os

import pytest

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


def test_generate_diff_yaml():
    file1 = get_fixture_path("file1.yml")
    file2 = get_fixture_path("file2.yaml")
    expected_file = get_fixture_path("expected_flat.txt")

    with open(expected_file, "r", encoding="utf-8") as f:
        expected_output = f.read()

    assert generate_diff(file1, file2) == expected_output


def test_generate_diff_security_path_traversal():
    bad_path1 = "../../../../etc/passwd"
    bad_path2 = "tests/test_data/file2.json"

    with pytest.raises(PermissionError):
        generate_diff(bad_path1, bad_path2)


def test_generate_diff_file_not_found():
    missing_path1 = "tests/test_data/non_existent_file.json"
    missing_path2 = "tests/test_data/file2.json"

    with pytest.raises(FileNotFoundError):
        generate_diff(missing_path1, missing_path2)
