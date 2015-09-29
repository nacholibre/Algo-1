import fileinput

if __name__ == '__main__':
    size = 0
    for i, line in enumerate(fileinput.input()):
        line = line.strip()

        if i == 0:
            size = int(i)
        else:
            print line
