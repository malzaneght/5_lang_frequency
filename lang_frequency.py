from collections import Counter
import re
import operator
import argparse

QUANTITY_WORDS = 10


def load_data(file_path):
    with open(file_path, 'r') as txt_file:
        return txt_file.read()


def get_most_frequent_words(users_text):
    pattern = re.compile('[\w\d_]+')
    parsed_text = pattern.findall(users_text)
    counter = Counter(parsed_text)
    return counter.most_common(QUANTITY_WORDS)


def print_result(input_data):
    for item in input_data:
        print('Word: "{}"'.format(item[0]), 'Repeat time:', item[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to file', required=True)
    args = parser.parse_args()
    text = load_data(args.path)
    result = get_most_frequent_words(text)
print_result(result)
