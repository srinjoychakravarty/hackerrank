def stockPairs(stocksProfit, target):
    n = len(stocksProfit) 
    print(stocksProfit)
    pairs = []
    count = 0 

    for i in range(0, n): 
        for j in range(i + 1, n): 
            if stocksProfit[i] + stocksProfit[j] == target: 
                pairs.append([stocksProfit[i], stocksProfit[j]])


    b_set = set(tuple(x) for x in pairs)  
    b = [ list(x) for x in b_set ]

    return len(b) 


if __name__ == '__main__':
    stocksProfit = [5,7,9,13,11,6,6,3,3]
    n = len(stocksProfit) 
    target = 12
    stockPairs(stocksProfit, target)