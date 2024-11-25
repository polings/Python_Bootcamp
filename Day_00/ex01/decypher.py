import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("phrase", help="Phrase to decypher")
    return parser.parse_args()


def main():
    args = get_args()
    for arg in args.phrase.split():
        print(arg[0], end="")


if __name__ == "__main__":
    main()
