import sys


def tricky_sort(input_list: list):
    str_list = list()
    int_list = list()
    result_list = list()

    for element in input_list:
        try:
            int_list.append(int(element))
        except ValueError:
            str_list.append(element)

    # nlog(n)
    str_list.sort(reverse=True)
    int_list.sort(reverse=True)

    for element in input_list:
        try:
            int(element)
            result_list.append(str(int_list.pop()))
        except ValueError:
            result_list.append(str_list.pop())

    print(' '.join(result_list))


if __name__ == '__main__':
    tricky_sort(sys.argv[1:])
