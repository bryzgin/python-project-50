import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    
    parser.add_argument(
        "-f", "--format",
        metavar="FORMAT",
        default="stylish",
        help="set format of output"
    )
    
    return parser.parse_args()