list_one = [118, 5, 3, 19, 57, 44, 6, 9, 30]


def range(list):
    biggest = list[0]
    smallest = list[0]
    biggest2 = None
    smallest2 = None
    for item in list[1:]:
        if item > biggest:
            biggest2 = biggest
            biggest = item
        elif biggest2 == None or biggest2 < item:
            biggest2 = item
        if item < smallest:
            smallest2 = smallest
            smallest = item
        elif smallest2 == None or smallest2 > item:
            smallest2 = item

    print('O maior valor é: ', biggest)
    print('O menor valor é: ', smallest)
    print('O segundo maior valor é: ', biggest2)
    print('O segundo menor valor é: ', smallest2)


range(list_one)
