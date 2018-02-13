from collections import Counter
import re
import operator
import argparse


def load_data(file_path):
    with open(file_path, 'r') as txt_file:
        return txt_file.read()


def get_most_frequent_words(users_text, total_words=10):
    words = re.findall('\w+', users_text)
    counter = Counter(words)
    return counter.most_common(total_words)


def print_result(input_data):
    for block in input_data:
        print('Word: "{0}"'.format(block[0]), 'Repeat time:', block[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to file', required=True)
    args = parser.parse_args()
    text = load_data(args.path)
    final_result = get_most_frequent_words(text)
print_result(final_result)
