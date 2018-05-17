
class TrieNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_final = False


class HashTrie(object):
