import argparse
from main import triangle

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Enter three sides length value")
    parser.add_argument('sides', metavar="s1 s2 s3", type=int, nargs="*", help='enter the length value for the first side')
    args = parser.parse_args()
    triangle(args.sides)