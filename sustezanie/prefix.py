import fileinput
import operator

if __name__ == '__main__':
    perms = {}

    maxWordLen = 12

    for i in range(1, 13):
        perms[i] = {}

    words = 0
    for i, line in enumerate(fileinput.input()):
        line = line.strip()

        if i == 0:
            words = int(line)
        else:
            start = 0
            for n in xrange(len(line)):
                occs = line[start:n+1]
                occsLen = len(occs)
                try:
                    perms[occsLen][occs] += 1
                except:
                    perms[occsLen][occs] = 1

    for wordLen in range(1, 13):
        sorted1 = sorted(perms[wordLen].items(), key=operator.itemgetter(1))

        maxSize = None
        words = []
        while True and len(sorted1):
            popped = sorted1.pop()
            if maxSize and maxSize > popped[1]:
                break
            maxSize = popped[1]
            word = popped[0]
            words.append((word, maxSize))

        if len(perms[wordLen]):
            p = sorted(words).pop(0)
            print '%s(%s)' % (p[0], p[1])
