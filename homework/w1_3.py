
import random


def moving_window_average(x, n_neighbors):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    result = []
    for position in range(n_neighbors, n+1):
        neighbors = x[position - n_neighbors: position + n_neighbors + 1]
        avg = sum(neighbors)/len(neighbors)
        result.append(avg)
    return result


# Explanation
# def moving_window_average(x, n_neighbors=1):
#     n = len(x)
#     width = n_neighbors*2 + 1
#     x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
#     return [sum(x[i:(i+width)]) / width for i in range(n)]


random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

x = [0, 10, 5, 3, 1, 5]
# print(moving_window_average(x, 1))
print("3a", sum(moving_window_average(x, 1)))

R = 1000
# Compute and store R=1000 random values from 0-1 as x.
x = [random.uniform(0, 1) for i in range(R)]
# Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive.
Y = [x] + [moving_window_average(x, i) for i in range(1, 10)]

# What is the moving window average for the 10th entry in x for n_neighbors = 5?
print("3b", Y[5][9])


# For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
ranges = [max(i) - min(i) for i in Y ]
print("3c", ranges)
