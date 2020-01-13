def my_reduce(func, seq):
    if(len(seq) >=2):
        return my_reduce(func, [func(seq[0], seq[1])] + seq[2:])
    else:
        return seq[0]


def plus(a, b):
    return a + b

if __name__ == "__main__":
    myL = list(range(5))
    print(myL)
    print(my_reduce(plus, myL))

