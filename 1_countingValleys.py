def countingValleys(n, s):
    lvl = 0
    val = 0
    for c in s:
        if (c == "D"):
            lvl -= 1
        else:
            lvl += 1
            if (lvl == 0):
                val += 1
    return val

if __name__ == "__main__":
    n = 8
    s = ["U", "D", "D", "D", "U", "D", "U", "U"]
    exp = 1
    valley = countingValleys(n, s)
    
    if (valley == exp):
        print("Output correct!")
    else:
        print("Expected {}, but the output is {}.".format(exp, valley))