def my_enumerate(iterable, start = 0):
    for i in range(len(iterable)):
        yield i, iterable[i]



if __name__ == "__main__":
    myL = list(range(5))
    for i, val in my_enumerate(myL):
        print(i, val)
