#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    if x - y == 0:
        return abs(x)
    elif x - y == 10:
        return 0
    else:
        return abs(y)
print(close10(9, 15 ))
