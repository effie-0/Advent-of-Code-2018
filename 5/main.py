# 12.5
import string


def react(value):
    length = len(value)
    flag = True
    note = 1
    while True:
        flag = True
        for i in range(note, length):
            if value[i] != value[i - 1] and value[i].upper() == value[i - 1].upper():
                if i - 1 >= 0 and i + 1 < length:
                    value = value[:i - 1] + value[i + 1:]
                    note = i - 1
                elif i - 1 < 0 and i + 1 < length:
                    value = value[i + 1:]
                    note = 1
                elif i - 1 >= 0 and i + 1 >= length:  # fault 2: forget '='
                    value = value[:i - 1]
                    note = i - 1

                length = len(value)
                if note == 0:
                    note = 1
                flag = False
                break
        if flag:
            break
    return value


if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        for line in f.readlines():
            v = line.strip()
            # question 1
            result = react(v)
            print(len(result))

            # question 2
            min_len = len(result)
            min_w = 'a'
            for w in string.ascii_lowercase:
                v = line.strip()
                v = v.replace(w, '')  # fault 1: no assignment
                v = v.replace(w.upper(), '')
                if len(v) == len(line.strip()):
                    continue
                result = react(v)
                if len(result) < min_len:
                    min_len = len(result)
                    min_w = w

            print(min_len)
            print(min_w)

