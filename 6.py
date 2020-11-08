def maxValue(n , rounds):

    investments = [n + 1]
    maxInvestment = 0

    contribution = rounds[-1]

    for contribution in rounds:
        startingIndex = contribution[0]
        endingIndex = contribution[1]
        amount = contribution[2]

        start = startingIndex

        while (start <= endingIndex):            
            investments[start] += amount
            maxInvestment = max(maxInvestment, investments[start])
            start += 1

    return maxInvestment

if __name__ == '__main__':
    n = 4
    #rounds = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

    rounds = [[2, 3, 603], [1, 1, 286], [4, 4, 882]]
    print(maxValue(n, rounds))