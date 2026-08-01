import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows deifference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    return parser.parse_args()