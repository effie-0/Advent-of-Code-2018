# 12.2


def check(string):
    isTwice = False
    isThreeTimes = False
    record_dict = {}
    for i in range(len(string)):
        if record_dict.__contains__(string[i]):
            record_dict[string[i]] += 1
        else:
            record_dict[string[i]] = 1

    for key, value in record_dict.items():
        if value == 2:
            isTwice = True
        elif value == 3:
            isThreeTimes = True

    return isTwice, isThreeTimes


def similar(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    is_similar = False
    remain = ''
    if len1 <= len2:
        length = len1
    else:
        length = len2
    for i in range(length):
        if string1[i] == string2[i]:
            remain += string1[i]
        elif is_similar:
            is_similar = False
            break
        elif not is_similar:
            is_similar = True

    return is_similar, remain


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1
        twice_number = 0
        three_times_number = 0
        input_list = []
        for line in f.readlines():
            input_list.append(line.strip())
            isTwice, isThreeTimes = check(line.strip())
            if isTwice:
                twice_number += 1
            if isThreeTimes:
                three_times_number += 1

        checksum = twice_number * three_times_number
        print(checksum)

        # question 2
        length = len(input_list)
        for i in range(length - 1):
            for j in range(i + 1, length):
                is_similar, remain = similar(input_list[i], input_list[j])
                if is_similar:
                    print(remain)
