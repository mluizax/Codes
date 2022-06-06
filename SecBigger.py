list_one = [1, 2, 3, 4, 5, 6]
list_two = [22, 50, 13, 5, 9, 150]
list_three = [5, 9, 3]


def secondbigger(list):
    list.sort()
    print('O segundo maior elemento da lista é ', list[-2])


secondbigger(list_one)
secondbigger(list_two)
secondbigger(list_three)
