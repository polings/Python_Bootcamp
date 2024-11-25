import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("num_lines", help="Number of lines", type=int)
    return parser.parse_args()


def main():
    args = get_args()
    for num in range(args.num_lines):
        try:
            x = input()
        except EOFError:
            break
        if (x.startswith("00000")) and (x[5] != "0") and (len(x) == 32):
            print(x)


if __name__ == "__main__":
    main()
