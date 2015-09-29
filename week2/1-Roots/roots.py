import fileinput
import math


class Roots:
    def square_root(self, number):
        left = 0
        right = number

        found = False

        c = 0

        closest = None

        while (right - left) >= 0.000001 and not found and c <= 100:
            c += 1
            middlePos = float(right + left) / 2
            middleElement = middlePos

            middleElementPow = math.pow(middleElement, 2)

            closest = middleElement

            if middleElementPow == number:
                found = middleElement
            if number < middleElementPow:
                right = middlePos
            elif number > middleElementPow:
                left = middlePos

        result = None
        if found:
            result = found
        else:
            result = closest

        return '%0.5f' % result


if __name__ == '__main__':
    roots = Roots()

    for line in fileinput.input():
        line = int(line.strip())
        print roots.square_root(line)
        break
