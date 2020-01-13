def my_accummulate(lst):
    return [sum([j for j in range(i + 1)]) for i in lst]


if __name__ == "__main__":
    myL = list(range(5))
    print(myL)
    print(my_accummulate(myL))
