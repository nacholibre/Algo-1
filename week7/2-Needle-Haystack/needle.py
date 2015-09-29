import sys


class StringSearch:
    def setSentence(self, sentence):
        self.sentence = sentence

    def _hash(self, myStr):
        myHash = 0
        firstLetterHash = 0

        strLen = len(myStr)-1

        for i, letter in enumerate(myStr):
            powerA = strLen - i
            letterHash = (ord(letter) * pow(127, powerA))
            myHash = myHash + letterHash

            if i == 0:
                firstLetterHash = myHash

        return [firstLetterHash, myHash]

    def search(self, needle):
        x = self._hash(needle)
        needleHash = x[1]

        start = 0
        end = len(needle)
        lastWordHash = 0
        lastWholeHash = 0

        while end <= len(self.sentence):
            currentWordWindow = self.sentence[start:end]

            x = self._hash(currentWordWindow)

            wordHash = x[0]
            wholeHash = x[1]

            if lastWholeHash:
                letterHash = self._hash(self.sentence[end-1])[1]
                wholeHash = ((lastWholeHash - lastWordHash) * 127) + letterHash

            if wholeHash == needleHash:
                print start

            start += 1
            end += 1

            lastWordHash = wordHash
            lastWholeHash = wholeHash


if __name__ == '__main__':
    sentence = None
    needle = None

    for i, line in enumerate(sys.stdin):
        line = line.strip()
        if i == 0:
            sentence = line
        else:
            needle = line

    ssearch = StringSearch()
    ssearch.setSentence(sentence)

    ssearch.search('dog')

    # print ssearch.search(needle)
    # dire
    #myHash = ssearch._hash('dir')
    #print myHash
    #print myHash[1] - myHash[0]

    #print '=' * 10
    ## print ssearch._hash('re')
    #print ssearch._hash('ire')
