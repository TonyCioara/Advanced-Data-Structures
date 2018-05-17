import re
import sys
import time
from trie import Trie


def get_words(text_file):
    with open(text_file) as words_file:
        raw_data = words_file.read()
        raw_data = raw_data.replace('\n', ' ')
        raw_data = re.sub('[^a-zA-Z]+', ' ', raw_data)
        data_list = raw_data.split(" ")
        data_list.pop()
        return data_list


def benchmark(all_prefixes, auto_corrector):
    start_time = time.time()
    for prefix in all_prefixes:
        auto_corrector.find_words(prefix)
    end_time = time.time()
    run_time = end_time - start_time
    return run_time


def main():
    text_file = '/usr/share/dict/words'
    all_words = get_words(text_file)

    start_time = time.time()
    auto_corrector = AutoCorrector(all_words)

    end_time = time.time()
    run_time = end_time - start_time
    print("--------------")
    print('Built Trie in {} "seconds.'.format(run_time))

    all_prefixes = set([word[:len(word)//2] for word in all_words])
    run_time = benchmark(all_prefixes, auto_corrector)
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(run_time, len(all_prefixes), len(all_words)))


class AutoCorrector(object):

    def __init__(self, data_list):
        self.trie = Trie()
        self.populate_trie(data_list)

    def populate_trie(self, data_list):
        for word in data_list:
            self.trie.insert(word)

    def find_words(self, prefix):
        return self.trie.get_words_with_prefix(prefix)


if __name__ == "__main__":
    main()
