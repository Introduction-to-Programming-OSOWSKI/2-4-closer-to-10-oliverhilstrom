#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    if abs(10 - x) > abs(10 - y):
        return y
    elif abs(10 - x) == abs(10 - y):
        return 0
    else:
        return x
print(close10(9, 15 ))
