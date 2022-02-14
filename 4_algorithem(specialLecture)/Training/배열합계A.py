import numpy as np

def findArraySumMax(array):
    
    

    for i in range(5):
        for j in range(5):
            if array[i][j] < 0 : array[i][j] = 0
            if array[i][j] > 100 : array[i][j] %= 100

    maxA = 0
    for i in range(4):
        for j in range(4):
            sumA = array[i][j] + array[i+1][j] + array[i][j+1] + array[i+1][j+1]
            # print(f'i: {i}, j: {j}, sum: {sumA}')
            if maxA < sumA : maxA = sumA
            # print(f'maxA : {maxA}')

    return maxA



a = np.array([[5, 7, -5, 100, 73], [35, 23, 4, 190, 33], [49, 85, 662, 39, 81], [124, -59, 86, 46, 52], [27, 7, 8, 33, -56]])
findArraySumMax(a)