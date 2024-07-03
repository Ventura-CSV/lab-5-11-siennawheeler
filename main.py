import random


def merge(number1, number2):
    mlist = []
    while len(number1) > 0 or len(number2) > 0:
        if len(number1) > 0 and len(number2) > 0:
            if number1[0] > number2[0]:
                mlist.append(number2[0])
                number2.remove(number2[0])
            else:
                mlist.append(number1[0])
                number1.remove(number1[0])
        else:
            if len(number1) > 0:
                mlist.append(number1[0])
                number1.remove(number1[0])
            else:
                mlist.append(number2[0])
                number2.remove(number2[0])


    #################
    # Do not delete return statement
    # You should return 'mlst" as a merged result
    return mlist


def main():
    number1 = [0, 2, 3]
    number2 = [1, 4, 5, 6, 9]
    retlist = merge(number1, number2)
    print(retlist)
    # #########################################

    # n1 = [random.randint(0, 20) for i in range(5)]
    # n2 = [random.randint(0, 20) for i in range(3)]
    # n1.sort()
    # n2.sort()
    # print(n1)
    # print(n2)
    n1 = [1, 3, 5]
    n2 = [2, 4, 6, 8, 10]
    retlist = merge(n1, n2)
    print(retlist)


if __name__ == '__main__':
    main()
