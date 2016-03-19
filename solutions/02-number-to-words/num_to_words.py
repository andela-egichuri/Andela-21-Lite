def num_to_word_1(A):
    words = ["zero", "one", "two", "three", "four",
                            "five", "six", "seven", "eight", "nine"]
    return " ".join([words[int(char)] for char in str(A)])


def num_to_word_2(A):
    A = str(A)
    words = []
    units = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    for each in A:
        if each in units:
            words.append(units[each])
        else:
            words.append(each)
    return " ".join(words)
