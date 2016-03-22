def sum_of_unique_digits_1(A):
    joined = ''
    selected = ''
    sum = 0
    for each in A:
        joined += str(each)

    for num in joined:
        if num not in selected:
            selected += num

    for num in selected:
        sum += int(num)
    return sum


def sum_of_unique_digits_2(A):
    joined = ''
    selected = ''
    sum = 0
    for each in A:
        joined += str(each)
    selected = set(joined)

    for num in selected:
        sum += int(num)
    return sum