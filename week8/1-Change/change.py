

def dpSumChange(coins, change):
    for c in range(change+1):
        print c

if __name__ == '__main__':
    coins = [1, 2, 5, 10, 20, 50, 100]
    change = 25

    emptyArr = [None] * 100

    print emptyArr

    dpSumChange(coins, 25)
