# 12.1


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1, calculate the sum
        _sum = 0
        # question 2
        input_list = []
        sum_dict = {}
        find_freq = False
        for line in f.readlines():
            number = int(line.strip())
            _sum += number
            input_list.append(number)
            if sum_dict.__contains__(_sum):
                print("first freq = " + str(_sum))
                find_freq = True
            sum_dict[_sum] = 1
        print("sum = " + str(_sum))

        while not find_freq:
            for number in input_list:
                _sum += number
                if sum_dict.__contains__(_sum):
                    print("first freq = " + str(_sum))
                    find_freq = True
                    break
                else:
                    sum_dict[_sum] = 1
