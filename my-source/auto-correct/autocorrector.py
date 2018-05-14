import re
from trie import Trie


def main():
    text_file = 'simple_text.txt'
    auto_corrector = AutoCorrector(text_file)
    print(auto_corrector.find_words('al'))


class AutoCorrector(object):

    def __init__(self, text_file):
        self.text_file = text_file
        self.trie = Trie()
        self.data_list = self.create_data()
        # print(self.data_list)
        self.populate_trie(self.data_list)

    def create_data(self):
        with open(self.text_file) as words_file:
            raw_data = words_file.read()
            raw_data = raw_data.replace('\n', ' ')
            raw_data = re.sub('[^a-zA-Z]+', ' ', raw_data)
            data_list = raw_data.split(" ")
            data_list.pop()
            return data_list

    def populate_trie(self, data_list):
        for word in data_list:
            self.trie.insert(word)

    def find_words(self, suffix):
        return self.trie.get_words_with_suffix(suffix)


if __name__ == "__main__":
    main()
