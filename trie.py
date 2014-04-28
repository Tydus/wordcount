#!/usr/bin/python

class TrieNode(object):
    def __init__(self, initvalue = 0):
        self._value = initvalue
        self._next = [None] * 32

    def __repr__(self):
        ret = [ "(%s, %s)" %(chr(i + 97), repr(j)) for i, j in enumerate(self._next) if j != None ]
        return "<TrieNode(%s, [%s])>" % (self._value, ", ".join(ret))

class Trie(object):

    def __init__(self, *initlist):
        self._root = TrieNode(None)
        if initlist:
            for i, j in initlist:
                self.insert(i, j)

    def insert(self, string, value = 1):
        string = string.lower() + '`' # Will be -1 in the list

        parent = self._root
        for i in map(lambda x: ord(x) - ord('a'), list(string)):
            if i == -1:
                parent._value += value
            elif parent._next[i] is None:
                parent._next[i] = TrieNode()
            parent = parent._next[i]

    def _traverse(self, node, stack):
        ret = []
        if node._value:
            ret.append((stack, node._value))
        for i, j in enumerate(node._next):
            if j:
                ret += self._traverse(j, stack + chr(ord('a') + i))
        return ret

    def __repr__(self):
        ret = []

        for key, value in self._traverse(self._root, ""):
            ret.append("('%s', %s)" % (key, value))

        return "Trie(" + ", ".join(ret) + ")"


if __name__ == "__main__":
    t = Trie(('a', 100))
    t.insert('a')
    print t
    t.insert('abc')
    print t
    t.insert('abd')
    print t
    t.insert('abd')
    t.insert('abd')
    t.insert('abd')
    print t
    t.insert('abd', 100)
    print t
    d = eval(repr(t))
    print d
