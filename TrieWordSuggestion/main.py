class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
            node.words.sort()
            while len(node.words) > 3:
                node.words.pop()

    def search(self, word):
        res = []
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            res.append(node.words[:])
        l_remain = len(word) - len(res)
        for _ in range(l_remain):
            res.append([])
        return res


def main():
    keys = ["mobile", "mouse", "moneypot", "monitor"]
    output = ["Not present in trie", "Present in trie"]
    t = Trie()
    for key in keys:
        t.insert(key)
    print("{} ---- {}".format("the",t.search("mouse")))


if __name__ == '__main__':
    main()
