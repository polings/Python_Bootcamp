import sys
import re


def main():
    stdin = sys.stdin.read()
    if len(stdin) != 0:
        text = stdin.rstrip().split()
        if len(text) == 3 and len(text[0]) == 5 and len(text[1]) == 5 and len(text[2]) == 5:
            print(True if re.match('[*][^*]{3}[*]', text[0]) and re.match('[*]{2}[^*][*]{2}', text[1]) and re.match(
                '[*][^*][*][^*][*]', text[2]) else False)
        else:
            print('Error')
    else:
        print('Error')


if __name__ == "__main__":
    main()
