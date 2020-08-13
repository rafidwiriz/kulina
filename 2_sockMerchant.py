def sockMerchant(n, ar):
    pair = 0
    no_pair = set()
    for x in ar:
        if (x in no_pair):
            no_pair.remove(x)
            pair += 1
        else:
            no_pair.add(x)
    return pair

if __name__ == "__main__":
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2]
    exp = 2
    pair = sockMerchant(n, ar)
    
    if (pair == exp):
        print("Output correct!")
    else:
        print("Expected {}, but the output is {}.".format(exp, pair))