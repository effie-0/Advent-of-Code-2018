# 12.12
# import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        state = None
        valid_list = []
        padding = 3
        for line in f.readlines():
            if len(line) <= 1:
                continue
            if 'initial state' in line:
                state = '.'*3 + line.strip()[15:] + '.'*3
                continue
            if line[-2] == '#':
                valid_list.append(line[:5])

        print("0:  " + state)
        num_0 = 0
        for i in range(len(state)):
            if state[i] == '#':
                num_0 += i - padding
        print("0:  " + str(num_0))

        # x_list = []
        # y_list = []
        prev = num_0
        num = 0
        for i in range(100):
            new_state = ''
            length = len(state)
            add_padding = False
            num = 0
            for j in range(length):
                string = None
                if j - 2 < 0:
                    string = '.'*(0 - j + 2) + state[:j+3]
                    if state[j] == '#':
                        add_padding = True
                elif j + 3 > length:
                    string = state[j-2:] + '.'*(j + 3 - length)
                    if state[j] == '#':
                        add_padding = True
                else:
                    string = state[j-2:j+3]
                if string in valid_list:
                    new_state += '#'
                    num += j - padding
                else:
                    new_state += '.'
            if add_padding:
                state = '.'*3 + new_state + '.'*3
                padding += 3
            else:
                state = new_state
            if i == 19:
                print("20:  " + str(num))
            # x_list.append(i+1)
            # y_list.append(num-num_0)
            # print(str(i+1) + ":  " + str(num - prev))
            # prev = num

        # plt.title("Pic")
        # plt.plot(x_list, y_list)
        # plt.grid()
        # plt.show()
        print("100:  " + str(num))
        # using the code in '#' to find the linear relation
        final = num + (50000000000 - 100) * 80
        print(final)
