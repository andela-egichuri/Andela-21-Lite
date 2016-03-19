def sum_of_digits_1(A):
    s = 0
    joined = int(''.join(map(str, A)))
    while joined:
        s += joined % 10
        joined //= 10
    return s


def sum_of_digits_2(A):
    joined = ''
    sum = 0
    for each in A:
        joined += str(each)

    for num in joined:
        sum += int(num)
    return sum


def sum_of_digits_3(A):
    total = 0
    new_list = []
    for a in A:
        while a > 0:
            new_list.append(a % 10)
            a //= 10
    for b in new_list:
        total += b
    return total