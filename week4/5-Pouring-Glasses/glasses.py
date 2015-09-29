import copy


def getNewPossiblePourings(cupFillings, cupsLimit):
    cups = len(cupFillings)
    possiblePourings = []

    for i in range(0, cups):
        for k in range(0, cups):
            if k != i:
                newForm = copy.copy(cupFillings)
                prevContent = cupFillings[i]

                currentContent = cupFillings[k]
                currentLimit = cupsLimit[k]

                cupSpaceLeft = currentLimit - currentContent

                if cupSpaceLeft > 0:
                    # moje da se sipva
                    newContent = prevContent + currentContent
                    if newContent > currentLimit:
                        prevOstatuk = newContent - currentLimit
                        newVal = currentLimit
                    else:
                        prevOstatuk = 0
                        newVal = newContent

                    action = '%s>%s' % (i+1, k+1)
                    newForm[i] = prevOstatuk
                    newForm[k] = newVal
                    possiblePourings.append([newForm, action])

    return possiblePourings


def genPossiblePourings(fillings, cupsLimit):
    fillingsNumber = len(fillings)

    possiblePourings = []

    for i in range(0, fillingsNumber):
        print '======'
        print 'i', i
        prevContent = fillings[i]

        for k in range(i+1, fillingsNumber):
            print 'k', k
            for x in range(0, 2):
                newForm = copy.copy(fillings)
                if x == 1:
                    i, k = k, i
                    prevContent = fillings[i]

                currentContent = fillings[k]
                print 'prev', prevContent
                print 'current', currentContent
                currentLimit = cupsLimit[k]

                cupSpaceLeft = currentLimit - currentContent

                if cupSpaceLeft > 0:
                    # moje da se sipva
                    newContent = prevContent + currentContent
                    if newContent > currentLimit:
                        prevOstatuk = newContent - currentLimit
                        newVal = currentLimit
                    else:
                        prevOstatuk = 0
                        newVal = newContent

                    newForm[i] = prevOstatuk
                    newForm[k] = newVal
                    possiblePourings.append(newForm)

    return possiblePourings


def foundWith(mylist, num):
    for x in mylist:
        if x == num:
            return True
    return False


def find(fillings, limits):
    visited = {}

    cases = []

    possiblePourings = getNewPossiblePourings(fillings, cupsLimits)

    cases = cases + possiblePourings

    actionsHistory = []

    while len(cases):
        popped = cases.pop(0)

        case = popped[0]
        actions = popped[1]

        if str(case) not in visited:
            actionsHistory.append(actions)

            if foundWith(case, 1):
                print 'found'
                return actionsHistory

            visited[str(case)] = True
            newPos = getNewPossiblePourings(case, limits)
            for case, actions in newPos:
                if str(case) not in visited:
                    cases.append([case, actions])

    # for state, action in possiblePourings:
    #     if str(state) not in visited:
    #         cases.append(state)

    #         actions = []
    #         actions.append(action)

    #         newPos = getNewPossiblePourings(state, cupsLimits)
    #         for state2, action2 in newPos:
    #             visited[str(state2)] = True
    #             if foundWith(state2, 1):
    #                 actions.append(action2)
    #                 return actions

    #         visited[str(state)] = True


if __name__ == '__main__':
    cupsLimits = (4, 7, 6)
    fillings = [2, 5, 4]

    actions = find(fillings, cupsLimits)
    print actions
