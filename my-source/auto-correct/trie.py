
class TrieNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_final = False


class Trie(object):

    def __init__(self):
        self.root = None
        self.size = 0

    # If you are reading through this I would like to deeply apologize for
    # what you're about to see. The following code may be a disgrace to all
    # of humanity and to god himself, but it gets the job done so...
    # Took me 2 hours to debug this. Do yourself a favor and don't follow in
    # my footsetps
    def insert(self, data):

        data = list(data)
        if self.root is None:
            node = TrieNode(data[0])
            self.root = node
            self.size += 1
            for index in range(1, len(data)):
                new_node = TrieNode(data[index])
                node.left = new_node
                node = node.left
                self.size += 1
            return

        index = 0
        node = self.root
        while index < len(data):
            if node == self.root and node.data > data[index]:
                new_node = TrieNode(data[index])
                new_node.right = node
                self.root = new_node
                node = new_node

            elif data[index] == node.data:
                if node.left is None and index < len(data) - 1:
                    new_node = TrieNode(data[index + 1])
                    self.size += 1
                    node.left = new_node
                elif node.left is not None:
                    if node.left.data > data[index + 1]:
                        new_node = TrieNode(data[index + 1])
                        new_node.right = node.left
                        node.left = new_node
                        self.size += 1
                if index == len(data) - 1:
                    node.is_final = True
                node = node.left
                index += 1

            elif data[index] > node.data:
                if node.right is None:
                    new_node = TrieNode(data[index])
                    self.size += 1
                    node.right = new_node
                elif data[index] < node.right.data:
                    new_node = TrieNode(data[index])
                    self.size += 1
                    new_node.right = node.right
                    node.right = new_node
                node = node.right

    def get_words_with_suffix(self, suffix):

        current_word = suffix
        node = self.root
        index = 0
        suffix = list(suffix)
        while index < len(suffix):
            if suffix[index] == node.data:
                node = node.left
                index += 1
            elif suffix[index] > node.data:
                node = node.right
            else:
                return []

        word_list = self.depth_first_search(node, current_word)
        return word_list

    def depth_first_search(self, node, current_word):
        current_word += node.data
        word_list = []

        if node.left is not None:
            word_list += self.depth_first_search(node.left, current_word)
        if node.right is not None:
            word_list += self.depth_first_search(node.right, current_word[:-1])
        if node.is_final is True:
            word_list += [current_word]
        return word_list
