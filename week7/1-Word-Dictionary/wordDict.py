import sys


class Node:
    def __init__(self):
        self.childNodes = [None] * 26
        self.hasWord = False
        self.data = None


class WordDict:
    def __init__(self):
        self.rootNode = Node()

    def _getChildNodeWithLetter(self, node, letter):
        letterIndex = self._getLetterIndex(letter)

        return node.childNodes[letterIndex]

    def _getLetterIndex(self, letter):
        return ord(letter) - 97

    def insert(self, word):
        node = self.rootNode

        wordLen = len(word)

        wordLevel = ''
        for i, letter in enumerate(word):
            wordLevel += letter

            inNode = self._getChildNodeWithLetter(node, letter)

            if inNode:
                node = inNode
            else:
                newNode = Node()
                newNode.data = wordLevel
                letterIndex = self._getLetterIndex(letter)
                node.childNodes[letterIndex] = newNode

                if i+1 == wordLen:
                    newNode.hasWord = True

                node = newNode

    def search(self, word):
        node = self.rootNode

        wordLen = len(word)

        for i, letter in enumerate(word):
            inNode = self._getChildNodeWithLetter(node, letter)

            if inNode:
                node = inNode
                if i+1 == wordLen and node.hasWord:
                    return True
            else:
                return False


if __name__ == '__main__':
    wordDict = WordDict()

    for i, line in enumerate(sys.stdin):
        line = line.strip()
        if i == 0:
            continue

        command, word = line.split(' ')

        if command == 'insert':
            wordDict.insert(word)
        elif command == 'contains':
            if wordDict.search(word):
                print 'true'
            else:
                print 'false'
