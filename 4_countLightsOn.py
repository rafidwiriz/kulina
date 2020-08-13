if __name__ == "__main__":
    N = 100
    lights = [0] * N

    for i in range(N):
        for j in range(i, N):
            if ((j+1) % (i+1) == 0):
                if lights[j] == 0:
                    lights[j] = 1
                else:
                    lights[j] = 0
    
    print(sum(lights))