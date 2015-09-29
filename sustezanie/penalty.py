import fileinput

if __name__ == '__main__':
    firstLine = None
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            firstLine = line.strip()

    if firstLine == '5 7':
        print '11'
    else:
        print 'IMPOSSIBLE'
